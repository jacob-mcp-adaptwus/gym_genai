// src/config/cognito.ts

import { UserManager } from 'oidc-client-ts';
import type { UserManagerSettings } from 'oidc-client-ts';

// Get the current domain with port for local development
const domain = window.location.origin;

// Cognito Configuration
const cognitoConfig: UserManagerSettings = {
    authority: import.meta.env.VITE_COGNITO_AUTHORITY,
    client_id: import.meta.env.VITE_COGNITO_CLIENT_ID,
    redirect_uri: `${domain}/auth/callback`,
    response_type: "code",
    scope: "openid",
    post_logout_redirect_uri: `${domain}/auth/login1`,
    silent_redirect_uri: `${domain}/silent-renew.html`,
    automaticSilentRenew: true,
    loadUserInfo: true,
    monitorSession: true,
    filterProtocolClaims: true,
    response_mode: "query"
};
// Create UserManager instance
export const userManager = new UserManager(cognitoConfig);

// Sign out helper function
// Sign out helper function
export const signOutRedirect = async () => {
  try {
      // Get the current user
      const user = await userManager.getUser();
      
      // Construct the Cognito domain - note the formatting
      const cognitoDomain = `https://us-east-2${import.meta.env.VITE_COGNITO_DOMAIN}.auth.us-east-2.amazoncognito.com`;
      
      // Build the logout URL
      const logoutUrl = new URL('/logout', cognitoDomain);
      
      // Add required parameters
      logoutUrl.searchParams.append('client_id', import.meta.env.VITE_COGNITO_CLIENT_ID);
      logoutUrl.searchParams.append('logout_uri', `${domain}/auth/login1`);
      
      // Add id_token_hint if available
      if (user?.id_token) {
          logoutUrl.searchParams.append('id_token_hint', user.id_token);
      }
      
      console.log('Logout URL:', logoutUrl.toString());
      
      // Clear local session
      // await userManager.signoutRedirect();
      
      // Redirect to Cognito logout
      //window.location.href = logoutUrl.toString();
  } catch (error) {
      console.error('Logout error:', error);
      // Fallback to login page
      //window.location.href = `${domain}/auth/login1`;
  }
};

// Helper function to get current user
export const getCurrentUser = async () => {
    try {
        const user = await userManager.getUser();
        return user;
    } catch (error) {
        console.error('Error getting user:', error);
        return null;
    }
};

// Helper function to check if user is authenticated
export const isAuthenticated = async () => {
    const user = await getCurrentUser();
    return !!user && !user.expired;
};

// Add a debug function to help troubleshoot
export const debugCognitoConfig = () => {
    console.log('Current Cognito Config:', {
        ...cognitoConfig,
        authority: cognitoConfig.authority,
        client_id: cognitoConfig.client_id,
        redirect_uri: cognitoConfig.redirect_uri,
        scope: cognitoConfig.scope
    });
};