<script setup lang="ts">
import { ref } from 'vue';
// assets
import app1 from '@/assets/images/landing/chat.png';
import app2 from '@/assets/images/landing/e-commerce.png';
import app3 from '@/assets/images/landing/mail.png';
import app4 from '@/assets/images/landing/social.png';

const tab = ref(null);
</script>
<template>
  <div class="spacer bg-primary pb-0 elementSection">
    <v-container fluid class="py-0">
      <v-row class="justify-center mb-0">
        <v-col md="6" cols="12">
          <div class="text-center">
            <h2 class="text-h2 mb-sm-4 mb-2">Working Conceptual Apps</h2>
            <p class="text-h6 mb-0">Each App is carefully crafted to achieve the best feature rich working concept for your project</p>
          </div>
        </v-col>
        <v-col md="12" cols="12" class="pa-sm-3 pa-0"></v-col>
      </v-row>
      <v-row class="justify-end mt-0">
        <v-col lg="4" md="5">
          <v-tabs v-model="tab" class="app-tab pb-md-11" color="white" hide-slider direction="vertical">
            <v-tab value="one" rounded="md">
              <div class="text-start py-5 px-2">
                <h4 class="text-h4">Chat</h4>
                <p class="text-body-1 mb-0">Power your web apps with the conceptual chat app of Able Pro Dashboard Template.</p>
              </div>
            </v-tab>
            <v-tab value="two" rounded="md">
              <div class="text-start py-5 px-2">
                <h4 class="text-h4">E-commerce</h4>
                <p class="text-body-1 mb-0">
                  Collection, Filter, Product Detail, Add New Product, and Checkout pages makes your e-commerce app complete.
                </p>
              </div>
            </v-tab>
            <v-tab value="three" rounded="md">
              <div class="text-start py-5 px-2">
                <h4 class="text-h4">Inbox</h4>
                <p class="text-body-1 mb-0">
                  Compose Message, List Message (email), Detailed Inbox pages well suited for any conversation based web apps.
                </p>
              </div>
            </v-tab>
            <v-tab value="four" rounded="md">
              <div class="text-start py-5 px-2">
                <h4 class="text-h4">User Management</h4>
                <p class="text-body-1 mb-0">
                  Detailed pages for User Management like Profile settings, role, account settings, social profile and more to explore.
                </p>
              </div>
            </v-tab>
          </v-tabs>
        </v-col>
        <v-col lg="6" md="7" sm="12" cols="12" class="pb-0">
          <v-window v-model="tab" class="app-content">
            <v-window-item value="one">
              <v-img :src="app1" alt="chat app" />
            </v-window-item>

            <v-window-item value="two">
              <v-img :src="app2" alt="ecommerce" />
            </v-window-item>

            <v-window-item value="three">
              <v-img :src="app3" alt="mail" />
            </v-window-item>

            <v-window-item value="four">
              <v-img :src="app4" alt="social profile" />
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<style lang="scss">
.app-tab {
  .v-slide-group__content {
    .v-btn {
      height: unset;
      .v-btn__content {
        white-space: unset;
      }
    }
  }
  .v-tab-item--selected {
    &.v-tab--selected {
      background-color: rgba(var(--v-theme-surface), 0.1);
      box-shadow: var(--v-card-shadow);
    }
  }
}
.app-content {
  margin-bottom: -100px;
  @media (max-width: 959px) {
    margin-bottom: 0;
    padding-bottom: 40px;
  }
  @media (max-width: 599px) {
    padding-bottom: 36px;
  }
}
</style>
