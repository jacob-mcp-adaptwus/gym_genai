<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import Logo from '@/layouts/dashboard/logo/LogoMain.vue';
import TextSlider from './TextSlider.vue';

// assets
import facebookImg from '@/assets/images/icons/facebook.svg';
import twitterImg from '@/assets/images/icons/twitter.svg';
import googleImg from '@/assets/images/icons/google.svg';

const tab = ref('0');

function changeTab(e: string) {
  tab.value = e;
}

const otp = ref('');
</script>
<template>
  <v-row class="bg-surface position-relative ma-0 overflow-hidden">
    <v-col cols="12" lg="7" md="6">
      <v-row class="pa-8 justify-center">
        <v-col cols="12">
          <Logo />
        </v-col>
        <v-col cols="12" sm="10" md="11" lg="6" style="height: calc(100vh - 168px)" class="d-flex align-center justify-center">
          <v-row>
            <v-col cols="12">
              <v-window v-model="tab">
                <v-window-item value="tab-1">
                  <div>
                    <div class="text-center">
                      <h3 class="text-h3">Welcome to the Able Pro</h3>
                      <p class="text-h6">Sign up or login with your work email.</p>
                      <v-list aria-label="social list" aria-busy="true">
                        <v-list-item
                          color="secondary"
                          variant="tonal"
                          href="#"
                          rounded="md"
                          class="mb-2 d-flex align-center justify-center"
                          @click="changeTab('tab-2')"
                        >
                          <div class="me-2 d-inline-block">
                            <SvgSprite name="custom-mail-outline" />
                          </div>
                          Continue with work Email
                        </v-list-item>
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
                    </div>
                  </div>
                </v-window-item>
                <v-window-item value="tab-2">
                  <div class="text-center mb-6">
                    <h3 class="text-h3">Welcome to the Able Pro</h3>
                    <p class="text-h6">Sign up or login with your work email.</p>
                  </div>
                  <v-label class="mb-2">Enter your work email to continue</v-label>
                  <v-text-field hide-details placeholder="Enter email address" variant="outlined" density="comfortable"></v-text-field>
                  <v-row class="mt-3">
                    <v-col cols="6">
                      <v-btn color="secondary" variant="outlined" rounded="md" @click="changeTab('tab-1')" block>Back</v-btn>
                    </v-col>
                    <v-col cols="6">
                      <v-btn color="primary" variant="flat" rounded="md" @click="changeTab('tab-3')" block>Continue</v-btn>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item value="tab-3">
                  <div class="text-center mb-6">
                    <h3 class="text-h3">What’s your purpose for use Able</h3>
                    <p class="text-h6">Your setup experience will be streamlined accordingly</p>
                  </div>
                  <div class="notification-dropdown">
                    <v-list class="d-flex v-row" aria-label="list" aria-busy="true">
                      <v-col cols="6">
                        <v-list-item class="text-center pa-10 text-lightText" color="secondary" rounded="md" value="personal">
                          <SvgSprite name="custom-user" style="width: 48px; height: 48px" />
                          <h5 class="text-h5 mt-2">Personal</h5>
                        </v-list-item>
                      </v-col>
                      <v-col cols="6">
                        <v-list-item class="text-center pa-10 text-lightText" color="secondary" rounded="md" value="business">
                          <SvgSprite name="custom-home-circle" style="width: 48px; height: 48px" />
                          <h5 class="text-h5 mt-2">Business</h5>
                        </v-list-item>
                      </v-col>
                    </v-list>
                  </div>
                  <v-row class="mt-3">
                    <v-col cols="6">
                      <v-btn color="secondary" variant="outlined" rounded="md" @click="changeTab('tab-2')" block>Back</v-btn>
                    </v-col>
                    <v-col cols="6">
                      <v-btn color="primary" variant="flat" rounded="md" @click="changeTab('tab-4')" block>Continue</v-btn>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item value="tab-4">
                  <div class="text-center mb-6">
                    <h3 class="text-h3">Tell us About Yourself</h3>
                    <p class="text-h6">Tell us a bit about yourself</p>
                  </div>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-label class="mb-2">First name</v-label>
                      <v-text-field
                        aria-label="name"
                        variant="outlined"
                        density="comfortable"
                        placeholder="First name"
                        hide-details
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-label class="mb-2">Last name</v-label>
                      <v-text-field
                        aria-label="name"
                        variant="outlined"
                        density="comfortable"
                        placeholder="Last name"
                        hide-details
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-label class="mb-2">Email id</v-label>
                      <v-text-field
                        aria-label="mail id"
                        type="email"
                        variant="outlined"
                        density="comfortable"
                        placeholder="Email id"
                        hide-details
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-label class="mb-2">Password</v-label>
                      <v-text-field
                        aria-label="password"
                        type="password"
                        variant="outlined"
                        density="comfortable"
                        placeholder="Password"
                        hide-details
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-label class="mb-2">Confirm Password</v-label>
                      <v-text-field
                        aria-label="password"
                        type="password"
                        variant="outlined"
                        density="comfortable"
                        placeholder="Confirm Password"
                        hide-details
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row class="mt-3">
                    <v-col cols="6">
                      <v-btn color="secondary" variant="outlined" rounded="md" @click="changeTab('tab-3')" block>Back</v-btn>
                    </v-col>
                    <v-col cols="6">
                      <v-btn color="primary" variant="flat" rounded="md" @click="changeTab('tab-5')" block>Continue</v-btn>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item value="tab-5">
                  <div class="text-center mb-6">
                    <h3 class="text-h3">Please confirm your email id</h3>
                    <p class="text-h6">Lorem Ipsum is simply dummy text of the printing and typesetting industry of Lorem Ipsum.</p>
                  </div>
                  <v-otp-input type="number" v-model="otp" length="4" class="mb-5" rounded="md" single-line height="60"></v-otp-input>
                  <v-row class="mt-3">
                    <v-col cols="6">
                      <v-btn color="secondary" variant="outlined" rounded="md" @click="changeTab('tab-4')" block>Back</v-btn>
                    </v-col>
                    <v-col cols="6">
                      <v-btn color="primary" variant="flat" rounded="md" @click="changeTab('tab-6')" block>Continue</v-btn>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item value="tab-6">
                  <v-alert
                    type="success"
                    variant="tonal"
                    class="mb-4 border-solid border-success border-thin border-opacity-25"
                    icon="false"
                    rounded="md"
                  >
                    <template v-slot:prepend>
                      <v-icon class="text-16" icon="$checkboxMarkedCircleOutline"></v-icon>
                    </template>
                    <div>All steps completed - you can now Login</div>
                  </v-alert>
                  <v-btn variant="flat" to="/auth/login1" color="primary" block>Login</v-btn>
                </v-window-item>
              </v-window>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" class="text-center">
          <p class="text-h6 mb-0">
            By signing up, you confirm to have read Able pro
            <a href="/pages/privacy-policy" class="text-primary">Privacy Policy</a>
            and agree to the
            <a href="/auth/login3" class="text-primary">Terms of Service</a>
            .
          </p>
        </v-col>
      </v-row>
    </v-col>
    <v-col cols="12" lg="5" md="6" class="d-md-flex d-none align-center bg-darkprimary" style="height: 100%">
      <v-row class="justify-center">
        <v-col cols="11" lg="8" md="10">
          <TextSlider />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.notification-dropdown {
  .v-list-item--active {
    &.text-lightText {
      color: rgb(var(--v-theme-primary)) !important;
    }
  }
}
</style>
