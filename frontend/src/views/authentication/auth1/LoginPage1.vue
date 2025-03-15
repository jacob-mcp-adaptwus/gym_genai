<script setup>
import { onMounted } from 'vue';
import { userManager } from '@/config/cognito';

// Redirect to Cognito login page on component mount
onMounted(async () => {
  try {
    await userManager.signinRedirect();
  } catch (error) {
    console.error('Login redirect error:', error);
  }
});
</script>

<template>
  <v-row class="bg-containerBg position-relative" no-gutters>
    <div class="bg-blur">
      <div class="round-1"></div>
      <div class="round-2"></div>
    </div>
    <v-col cols="12" lg="12" class="d-flex align-center">
      <v-container>
        <div class="d-flex align-center justify-center" style="min-height: calc(100vh - 148px)">
          <v-row justify="center">
            <v-col cols="12" md="12">
              <v-card elevation="0" variant="outlined" rounded="lg" class="loginBox bg-surface">
                <v-card-text class="pa-sm-10 pa-6">
                  <div class="text-center">
                    <v-progress-circular
                      indeterminate
                      color="primary"
                      size="64"
                    ></v-progress-circular>
                    <h3 class="text-h5 mt-4">Redirecting to login...</h3>
                    <p class="text-body-1 text-medium-emphasis mt-2">
                      Please wait while we redirect you to the login page
                    </p>
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

<style lang="scss">
.loginBox {
  max-width: 475px;
  margin: 0 auto;
}
</style>