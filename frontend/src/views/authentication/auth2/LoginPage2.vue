<script setup lang="ts">
import Logo from '@/layouts/dashboard/logo/LogoMain.vue';
import AuthLogin from '../authForms/AuthLogin.vue';
// assets
import facebookImg from '@/assets/images/icons/facebook.svg';
import twitterImg from '@/assets/images/icons/twitter.svg';
import googleImg from '@/assets/images/icons/google.svg';

import leftImg from '@/assets/images/auth/img-auth-sideimg.png';
</script>

<template>
  <v-row class="bg-surface position-relative" no-gutters>
    <v-col cols="12" lg="7" md="6" class="d-md-block d-none">
      <v-img :src="leftImg" alt="banner" height="100%" cover />
    </v-col>
    <!---Login Part-->
    <v-col cols="12" lg="5" md="6" class="d-flex align-center">
      <v-container>
        <div class="d-flex align-center justify-center" style="min-height: calc(100vh - 148px)">
          <v-row justify="center">
            <v-col cols="12" md="12">
              <div class="pa-sm-10 pa-6 loginBox">
                <div class="text-center">
                  <Logo class="mb-5" />
                  <v-list aria-label="social list" aria-busy="true">
                    <v-list-item color="secondary" variant="tonal" href="#" rounded="md" class="mb-2">
                      <v-img
                        :src="facebookImg"
                        alt="social icon"
                        class="me-2 d-inline-flex"
                        style="vertical-align: middle"
                        width="9"
                        height="16"
                      />
                      Sign in with facebook
                    </v-list-item>
                    <v-list-item color="secondary" variant="tonal" href="#" rounded="md" class="mb-2">
                      <v-img
                        :src="twitterImg"
                        alt="social icon"
                        class="me-2 d-inline-flex"
                        style="vertical-align: middle"
                        width="16"
                        height="13"
                      />
                      Sign in with twitter
                    </v-list-item>
                    <v-list-item color="secondary" variant="tonal" href="#" rounded="md" class="mb-2">
                      <v-img
                        :src="googleImg"
                        alt="social icon"
                        class="me-2 d-inline-flex"
                        style="vertical-align: middle"
                        width="16"
                        height="16"
                      />
                      Sign in with google
                    </v-list-item>
                  </v-list>
                  <v-row>
                    <v-col cols="12" class="d-flex align-center">
                      <v-divider />
                      <div class="orbtn">OR</div>
                      <v-divider />
                    </v-col>
                  </v-row>
                </div>
                <!---Login Form-->
                <AuthLogin />
                <!---Login Form-->
              </div>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-col>
    <!---Login Part-->
  </v-row>
</template>
<style lang="scss">
.loginBox {
  max-width: 475px;
  margin: 0 auto;
}
</style>
