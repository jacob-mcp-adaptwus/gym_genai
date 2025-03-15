<script setup lang="ts">
import { ref, shallowRef } from 'vue';

const signing = ref(['Basic form', 'Firebase - Auth', 'Facebook', 'Twitter', 'Gmail', 'JWT', 'AUTH0']);

const textFname = ref('Asoka_Tana_16');
const textEmail = ref('user@tana.com');
const textLanguage = ref('New York');
const textSigning = ref<string>('Facebook');

const secure = ref(true);
const login = ref(true);
const approve = ref(true);

const recognizes = shallowRef([
  { text: 'Cent Desktop', subtext: '4351 Deans Lane, Chelmsford', active: true },
  { text: 'Imho Tablet', subtext: '4185 Michigan Avenue', active: false, time: ' 5 days ago' },
  { text: 'Albs Mobile', subtext: '3462 Fairfax Drive, Montcalm', active: false, time: ' 1 month ago' }
]);

const activeSessions = shallowRef([
  { text: 'Cent Desktop', subtext: '4351 Deans Lane, Chelmsford' },
  { text: 'Moon Tablet', subtext: '4185 Michigan Avenue' }
]);
</script>

<template>
  <v-row>
    <v-col cols="12">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">General Settings</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Username</v-label>
                <v-text-field
                  color="primary"
                  single-line
                  aria-label="username"
                  variant="outlined"
                  density="comfortable"
                  type="text"
                  hide-details
                  v-model="textFname"
                  hint="Your Profile URL: https://pc.com/Ashoka_Tano_16"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Account Email</v-label>
                <v-text-field
                  color="primary"
                  single-line
                  variant="outlined"
                  density="comfortable"
                  aria-label="email"
                  type="email"
                  hide-details
                  v-model="textEmail"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Language</v-label>
                <v-text-field
                  color="primary"
                  density="comfortable"
                  single-line
                  variant="outlined"
                  aria-label="language"
                  hide-details
                  v-model="textLanguage"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Signing Using</v-label>
                <v-select
                  color="primary"
                  single-line
                  density="comfortable"
                  role="link"
                  :items="signing"
                  label="Signing Using"
                  variant="outlined"
                  v-model="textSigning"
                  hide-details
                >
                </v-select>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
    <v-col cols="12" md="6">
      <v-card variant="flat" class="overflow-hidden" rounded="lg">
        <v-card variant="outlined" class="overflow-hidden" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Advance Settings</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text class="pa-0">
            <v-list aria-label="setting list" aria-busy="true">
              <v-list-item border class="py-3">
                <h5 class="text-h6 mb-0">Secure Browsing</h5>
                <p class="text-caption text-lightText mb-0">Browsing Securely ( https ) when it's necessary</p>
                <template v-slot:append>
                  <v-switch color="primary" aria-label="switch" v-model="secure" hide-details inset> </v-switch>
                </template>
              </v-list-item>
              <v-list-item border class="py-3">
                <h5 class="text-h6 mb-0">Login Notifications</h5>
                <p class="text-caption text-lightText mb-0">Notify when login attempted from other place</p>
                <template v-slot:append>
                  <v-switch color="primary" aria-label="switch" v-model="login" hide-details inset> </v-switch>
                </template>
              </v-list-item>
              <v-list-item border class="py-3">
                <h5 class="text-h6 mb-0">Login Aprrovals</h5>
                <p class="text-caption text-lightText mb-0">Approvals is not required when login from unrecognized devices.</p>
                <template v-slot:append>
                  <v-switch color="primary" aria-label="switch" v-model="approve" hide-details inset> </v-switch>
                </template>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
    <v-col cols="12" md="6">
      <v-card variant="outlined" class="overflow-hidden" rounded="lg">
        <div class="pa-5">
          <h5 class="text-subtitle-1 mb-0">Recognized Devices</h5>
        </div>
        <v-divider></v-divider>
        <v-card-text class="pa-0">
          <v-list lines="two" aria-label="device list" aria-busy="true">
            <v-list-item class="device-content" v-for="(recognize, i) in recognizes" :key="i" color="primary" border>
              <v-list-recognize-title class="text-h6 mb-0">
                {{ recognize.text }}
              </v-list-recognize-title>
              <p class="text-caption text-lightText mb-0">
                {{ recognize.subtext }}
              </p>
              <template v-slot:append>
                <span v-if="recognize.active">
                  <v-badge dot color="success" inline></v-badge>
                  <span class="d-none d-sm-inline-block">Active</span>
                </span>
                <span v-else>
                  <v-badge dot color="lightText" inline></v-badge>
                  <span class="d-none d-sm-inline-block"> Active {{ recognize.time }}</span>
                </span>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card variant="outlined" class="overflow-hidden" rounded="lg">
        <div class="pa-5">
          <h5 class="text-subtitle-1 mb-0">Active sessions</h5>
        </div>
        <v-divider></v-divider>
        <v-card-text class="pa-0">
          <v-list lines="two" aria-label="session list" aria-busy="true">
            <v-list-item v-for="(activeSession, i) in activeSessions" :key="i" color="primary" border>
              <h5 class="text-h5 mb-0">{{ activeSession.text }}</h5>
              <p class="text-caption text-lightText mb-0">{{ activeSession.subtext }}</p>
              <template v-slot:append>
                <v-btn variant="text" color="primary" rounded="md" class="ms-4"> Logout </v-btn>
              </template>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
      <div class="text-end mt-6">
        <v-btn color="secondary" rounded="md" variant="outlined" class="me-3">Cancel</v-btn>
        <v-btn color="primary" rounded="md">Update Profile</v-btn>
      </div>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.device-content {
  .v-list-item__append {
    align-self: center;
  }
}
</style>
