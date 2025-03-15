//src/views/authentication/authForms/AuthLogin.vue

<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useAuthStore } from '@/stores/auth';
import { Form } from 'vee-validate';
// Import assets
import facebookImg from '@/assets/images/icons/facebook.svg';
import twitterImg from '@/assets/images/icons/twitter.svg';
import googleImg from '@/assets/images/icons/google.svg';

const checkbox = ref(false);
const valid = ref(false);
const show1 = ref(false);
const password = ref('');
const username = ref('');
const loading = ref(false);
const errorMessage = ref('');

// Password validation rules
const passwordRules = ref([
  (v: string) => !!v || 'Password is required',
  (v: string) => v === v.trim() || 'Password cannot start or end with spaces',
  (v: string) => v.length <= 10 || 'Password must be less than 10 characters'
]);

// Email validation rules
const emailRules = ref([
  (v: string) => !!v.trim() || 'E-mail is required',
  (v: string) => {
    const trimmedEmail = v.trim();
    return !/\s/.test(trimmedEmail) || 'E-mail must not contain spaces';
  },
  (v: string) => /.+@.+\..+/.test(v.trim()) || 'E-mail must be valid'
]);

async function validate(values: any, { setErrors }: any) {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    // Trim the username before validation
    const trimmedUsername = username.value.trim();
    username.value = trimmedUsername;

    const authStore = useAuthStore();
    await authStore.login(trimmedUsername, password.value);
    
    // The login method will redirect to Cognito, so we don't need to handle success here
  } catch (error: any) {
    console.error('Login error:', error);
    setErrors({ 
      apiError: error.message || 'Failed to login. Please try again.' 
    });
  } finally {
    loading.value = false;
  }
}

// Updated social login handler
const handleSocialLogin = async (provider: 'google' | 'facebook' | 'twitter') => {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const authStore = useAuthStore();
    // Instead of passing empty credentials, we'll use userManager's signinRedirect
    await authStore.login(username.value, password.value);
    
  } catch (error: any) {
    console.error(`${provider} login error:`, error);
    errorMessage.value = `Failed to login with ${provider}. Please try again.`;
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="d-flex justify-space-between align-center mt-4">
    <h3 class="text-h3 text-center mb-0">Login</h3>
    <router-link to="/auth/register1" class="text-primary text-decoration-none">Don't Have an account?</router-link>
  </div>
  
  <Form @submit="validate" class="mt-7 loginForm" v-slot="{ errors, isSubmitting }">
    <div class="mb-6">
      <v-label>Email Address</v-label>
      <v-text-field
        aria-label="email address"
        v-model="username"
        :rules="emailRules"
        class="mt-2"
        density="comfortable"
        required
        hide-details="auto"
        variant="outlined"
        color="primary"
        :disabled="loading"
        @input="username = $event.trim()"
      ></v-text-field>
    </div>
    
    <div>
      <v-label>Password</v-label>
      <v-text-field
        aria-label="password"
        v-model="password"
        :rules="passwordRules"
        required
        variant="outlined"
        density="comfortable"
        color="primary"
        hide-details="auto"
        :type="show1 ? 'text' : 'password'"
        class="pwdInput mt-2"
        :disabled="loading"
        @input="password = $event.trim()"
      >
        <template v-slot:append-inner>
          <v-btn color="secondary" aria-label="icon" icon rounded variant="text">
            <SvgSprite 
              name="custom-eye-invisible" 
              style="width: 20px; height: 20px" 
              v-if="!show1" 
              @click="show1 = !show1" 
            />
            <SvgSprite 
              name="custom-eye" 
              style="width: 20px; height: 20px" 
              v-if="show1" 
              @click="show1 = !show1" 
            />
          </v-btn>
        </template>
      </v-text-field>
    </div>

    <div class="d-flex align-center mt-4 mb-7 mb-sm-0">
      <v-checkbox
        v-model="checkbox"
        :rules="[(v: any) => !!v || 'You must agree to continue!']"
        label="Keep me sign in"
        required
        color="primary"
        class="ms-n2"
        hide-details
      ></v-checkbox>
      <div class="ms-auto">
        <router-link to="/auth/forgot-pwd1" class="text-darkText link-hover">Forgot Password?</router-link>
      </div>
    </div>

    <!-- Display any API errors -->
    <v-alert
      v-if="errorMessage || errors.apiError"
      color="error"
      class="mt-3"
      variant="tonal"
    >
      {{ errorMessage || errors.apiError }}
    </v-alert>

    <v-btn
      color="primary"
      :loading="isSubmitting || loading"
      block
      class="mt-5"
      variant="flat"
      size="large"
      rounded="md"
      :disabled="!valid"
      type="submit"
    >
      Login
    </v-btn>

    <!-- Social Login Section -->
    <div class="text-center mt-6">
      <v-divider class="mb-4">
        <span class="px-3">Or continue with</span>
      </v-divider>
      
      <v-list aria-label="social list" aria-busy="true">
        <v-list-item color="secondary" variant="tonal" @click="handleSocialLogin('google')" rounded="md" class="mb-2">
          <v-img
            :src="googleImg"
            alt="social icon"
            class="me-2 d-inline-flex"
            style="vertical-align: middle"
            width="16"
            height="16"
          />
          Sign in with Google
        </v-list-item>
        <v-list-item color="secondary" variant="tonal" @click="handleSocialLogin('facebook')" rounded="md" class="mb-2">
          <v-img
            :src="facebookImg"
            alt="social icon"
            class="me-2 d-inline-flex"
            style="vertical-align: middle"
            width="9"
            height="16"
          />
          Sign in with Facebook
        </v-list-item>
      </v-list>
    </div>
  </Form>
</template>

<style lang="scss" scoped>
.loginForm {
  position: relative;
  
  .v-divider {
    border-color: rgba(0, 0, 0, 0.12);
    margin: 24px 0;
    
    span {
      background: white;
      color: rgba(0, 0, 0, 0.6);
      font-size: 14px;
    }
  }
}
</style>