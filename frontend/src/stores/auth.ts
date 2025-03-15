// src/stores/auth.ts

import { defineStore } from 'pinia';
import { router } from '@/router';
import { userManager, getCurrentUser } from '@/config/cognito';
import { User } from 'oidc-client-ts';

interface AuthState {
  user: any | null;
  cognitoUser: User | null;
  returnUrl: string | null;
  loading: boolean;
  error: string | null;
}

export const useAuthStore = defineStore({
  id: 'auth',
  state: (): AuthState => ({
    user: null,
    cognitoUser: null,
    returnUrl: null,
    loading: false,
    error: null
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.cognitoUser && !state.cognitoUser.expired,
  },
  
  actions: {
    async login(username: string, password: string) {
      try {
        this.loading = true;
        this.error = null;

        // Store current URL as return URL
        if (router.currentRoute.value.query.returnUrl) {
          this.returnUrl = router.currentRoute.value.query.returnUrl as string;
        }

        await userManager.signinRedirect({
          extraQueryParams: {
            username,
            password,
          }
        });
      } catch (error: any) {
        console.error('Login error:', error);
        this.error = error.message || 'Failed to login';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async handleLoginCallback() {
      try {
        this.loading = true;
        this.error = null;
        
        // Get the current user after callback
        const user = await userManager.signinRedirectCallback();
        // console.log('Callback user:', user); // Debug log
        
        if (!user) {
          throw new Error('No user data received');
        }

        // Store the Cognito user
        this.cognitoUser = user;
        
        // Store basic user info
        this.user = {
          id: user.profile.sub,
          email: user.profile.email,
          name: user.profile.name || user.profile.email,
        };

        // Navigate to returnUrl or default route
        const returnUrl = this.returnUrl || '/dashboard/default';
        this.returnUrl = null;
        
        await router.push(returnUrl);
      } catch (error: any) {
        console.error('Login callback error:', error);
        // Check for specific error types
        if (error.message.includes('login_required')) {
          this.error = 'Please log in again';
        } else if (error.message.includes('invalid_grant')) {
          this.error = 'Invalid credentials';
        } else {
          this.error = error.message || 'Authentication failed';
        }
        
        // Redirect to login page with error
        router.push({
          path: '/auth/login1',
          query: { error: this.error }
        });
        
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async logout() {
      try {
        this.loading = true;
        this.error = null;

        //lohgout is broken need to fix this at some point
        //await userManager.signoutRedirect();
        
        // Clear state
        this.user = null;
        this.cognitoUser = null;
        
        router.push('/');
      } catch (error: any) {
        console.error('Logout error:', error);
        this.error = error.message || 'Failed to logout';
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async checkAuth() {
      try {
        const user = await getCurrentUser();
        if (user && !user.expired) {
          this.cognitoUser = user;
          this.user = {
            id: user.profile.sub,
            email: user.profile.email,
            name: user.profile.name || user.profile.email,
          };
          return true;
        }
        return false;
      } catch (error) {
        console.error('Check auth error:', error);
        return false;
      }
    }
  }
});