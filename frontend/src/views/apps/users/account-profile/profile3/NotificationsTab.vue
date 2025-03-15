<script setup lang="ts">
import { ref } from 'vue';

const sub1 = ref(true);
const sub2 = ref(false);
const sub3 = ref(false);
const sub4 = ref(false);

const checkbox1 = ref(false);
</script>

<template>
  <v-row>
    <v-col cols="12" md="8">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Subscription Preference Center</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <h5 class="text-subtitle-1 mb-2">I would like to receive:</h5>
            <v-list density="compact" aria-label="notification list" aria-busy="true">
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Product Announcements and Updates</v-list-item-title>
                <template v-slot:append>
                  <v-checkbox color="primary" aria-label="checkbox" hide-details density="compact" v-model="sub1"> </v-checkbox>
                </template>
              </v-list-item>
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Events and Meetups</v-list-item-title>
                <template v-slot:append>
                  <v-checkbox color="primary" aria-label="checkbox" hide-details density="compact" v-model="sub2"> </v-checkbox>
                </template>
              </v-list-item>
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">User Research Surveys</v-list-item-title>
                <template v-slot:append>
                  <v-checkbox color="primary" aria-label="checkbox" hide-details density="compact" v-model="sub3"> </v-checkbox>
                </template>
              </v-list-item>
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Hatch Startup Program</v-list-item-title>
                <template v-slot:append>
                  <v-checkbox color="primary" aria-label="checkbox" hide-details density="compact" v-model="sub4"> </v-checkbox>
                </template>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
    <v-col cols="12" md="4">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Opt me out instead</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-list density="compact" aria-label="notification list" aria-busy="true">
              <v-list-item class="pa-0">
                <v-list-item-title class="text-h6 text-lightText">Unsubscribe me from all of the above</v-list-item-title>
                <template v-slot:append>
                  <v-checkbox v-model="checkbox1" aria-label="checkbox" hide-details density="compact"> </v-checkbox>
                </template>
              </v-list-item>
            </v-list>
            <v-btn color="primary" rounded="md" variant="flat" class="mt-4">Update My Prefereces</v-btn>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
