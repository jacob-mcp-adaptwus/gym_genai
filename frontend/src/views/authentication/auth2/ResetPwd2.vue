<script setup lang="ts">
import AuthResetPwd from '../authForms/AuthResetPwd.vue';
import leftImg from '@/assets/images/auth/img-auth-sideimg.png';
</script>

<template>
  <v-row class="bg-surface position-relative" no-gutters>
    <v-col cols="12" lg="7" md="6" class="d-md-block d-none">
      <v-img :src="leftImg" alt="banner" height="100%" cover />
    </v-col>
    <!---Reset pwd Part-->
    <v-col cols="12" lg="5" md="6" class="d-flex align-center">
      <v-container>
        <div class="d-flex align-center justify-center" style="min-height: calc(100vh - 148px)">
          <v-row justify="center">
            <v-col cols="12">
              <div class="pa-sm-10 pa-6 loginBox">
                <h3 class="text-h3 mb-2">Reset Password</h3>
                <p class="text-h6 text-lightText">Please choose your new password</p>

                <!---Reset pwd Form-->
                <AuthResetPwd />
                <!---Reset pwd Form-->
              </div>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-col>
    <!---Reset pwd Part-->
  </v-row>
</template>
<style lang="scss">
.loginBox {
  max-width: 475px;
  margin: 0 auto;
}
</style>
