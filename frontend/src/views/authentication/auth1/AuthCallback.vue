// src/views/authentication/auth1/AuthCallback.vue

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRoute } from 'vue-router';

const loading = ref(true);
const error = ref<string | null>(null);
const route = useRoute();

onMounted(async () => {
  const authStore = useAuthStore();
  
  try {
    // Log the current URL for debugging
    // console.log('Callback URL:', window.location.href);
    
    // Check for error in URL
    if (route.query.error) {
      throw new Error(route.query.error as string);
    }

    // Process the callback
    await authStore.handleLoginCallback();
  } catch (err: any) {
    console.error('Callback error:', err);
    error.value = err.message || 'Authentication failed. Please try again.';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <v-row class="bg-containerBg position-relative" no-gutters>
    <div class="bg-blur">
      <div class="round-1"></div>
      <div class="round-2"></div>
    </div>
    <v-col cols="12" class="d-flex align-center">
      <v-container>
        <div class="d-flex align-center justify-center" style="min-height: calc(100vh - 148px)">
          <v-row justify="center">
            <v-col cols="12" lg="12">
              <v-card elevation="0" variant="outlined" rounded="lg" class="loginBox bg-surface">
                <v-card-text class="pa-sm-10 pa-4">
                  <!-- Show loading state -->
                  <div v-if="loading" class="text-center">
                    <v-progress-circular
                      indeterminate
                      color="primary"
                      size="64"
                    ></v-progress-circular>
                    <h3 class="text-h5 mt-4">Completing your sign in...</h3>
                    <p class="text-body-1 text-medium-emphasis mt-2">
                      Please wait while we verify your credentials
                    </p>
                  </div>

                  <!-- Show error if any -->
                  <div v-else-if="error" class="text-center">
                    <v-alert
                      type="error"
                      variant="tonal"
                      class="mb-4"
                    >
                      {{ error }}
                    </v-alert>
                    <v-btn
                      color="primary"
                      to="/auth/login1"
                      variant="flat"
                      rounded="md"
                      class="mt-4"
                    >
                      Back to Login
                    </v-btn>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped>
.loginBox {
  max-width: 475px;
  margin: 0 auto;
}
</style>