<script setup lang="ts">
import { ref } from 'vue';

const email1 = ref(true);
const email2 = ref(false);
const email3 = ref(true);
const email4 = ref(false);
const email5 = ref(true);
const email6 = ref(true);
const email7 = ref(false);
const email8 = ref(true);

const checkbox1 = ref(true);
const checkbox2 = ref(true);
const checkbox3 = ref(false);
const checkbox4 = ref(false);
const checkbox5 = ref(false);
</script>

<template>
  <v-row>
    <v-col cols="12" md="6">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Email Settings</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <h5 class="text-subtitle-1 mb-2">Setup Email Notification</h5>
            <v-list density="compact" aria-label="setup list" aria-busy="true">
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Email Notification</v-list-item-title>
                <template v-slot:append>
                  <v-switch color="primary" v-model="email1" aria-label="switch" hide-details inset> </v-switch>
                </template>
              </v-list-item>
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Send Copy To Personal Email</v-list-item-title>
                <template v-slot:append>
                  <v-switch color="primary" v-model="email2" aria-label="switch" hide-details inset> </v-switch>
                </template>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
      <v-card variant="outlined" class="mt-6" rounded="lg">
        <div class="pa-5">
          <h5 class="text-subtitle-1 mb-0">Updates from system notification</h5>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <h5 class="text-subtitle-1 mb-1">Email you with?</h5>
          <v-list density="compact" aria-label="email list" aria-busy="true">
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">News about PCT-themes products and feature updates</v-list-item-title>
              <template v-slot:append>
                <v-checkbox color="primary" hide-details aria-label="checkbox" v-model="checkbox1"> </v-checkbox>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Tips on getting more out of PCT-themes</v-list-item-title>
              <template v-slot:append>
                <v-checkbox color="primary" hide-details aria-label="checkbox" v-model="checkbox2"> </v-checkbox>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Things you missed since you last logged into PCT-themes</v-list-item-title>
              <template v-slot:append>
                <v-checkbox color="primary" hide-details aria-label="checkbox" v-model="checkbox3"> </v-checkbox>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">News about products and other services</v-list-item-title>
              <template v-slot:append>
                <v-checkbox color="primary" hide-details aria-label="checkbox" v-model="checkbox4"> </v-checkbox>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Tips and Document business products</v-list-item-title>
              <template v-slot:append>
                <v-checkbox color="primary" hide-details aria-label="checkbox" v-model="checkbox5"> </v-checkbox>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" md="6">
      <v-card variant="outlined" rounded="lg">
        <div class="pa-5">
          <h5 class="text-subtitle-1 mb-0">Activity Related Emails</h5>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <h5 class="text-subtitle-1 mb-1">When to email?</h5>
          <v-list density="compact" aria-label="activity list" aria-busy="true" class="pb-5">
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Have new notifications</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email3" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">You're sent a direct message</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email4" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Someone adds you as a connection</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email5" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
          </v-list>
          <v-divider></v-divider>

          <h5 class="text-subtitle-1 mb-1 mt-6">When to escalate emails?</h5>
          <v-list density="compact" aria-label="email list" aria-busy="true">
            <v-list-item class="pa-0" disabled>
              <v-list-item-title class="text-h6 text-lightText">Upon new order</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email6" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
            <v-list-item class="pa-0" disabled>
              <v-list-item-title class="text-h6 text-lightText">New membership approval</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email7" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
            <v-list-item class="pa-0">
              <v-list-item-title class="text-h6 text-lightText">Member registration</v-list-item-title>
              <template v-slot:append>
                <v-switch color="primary" v-model="email8" aria-label="switch" hide-details inset> </v-switch>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-col>
    <V-col cols="12" class="text-end">
      <v-btn color="secondary" rounded="md" variant="outlined" class="me-3"> Cancel </v-btn>
      <v-btn color="primary" rounded="md" variant="flat"> Update profile </v-btn>
    </V-col>
  </v-row>
</template>
