<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

import ProfileBanner from './ProfileBanner.vue';
import UserBackRight from './UserBackRight.vue';
import UserBackLeft from './UserBackLeft.vue';
import UserDetails from './UserDetails.vue';
import InformationTab from './InformationTab.vue';
import PaymentTab from './PaymentTab.vue';
import ChangePasswordTab from './ChangePasswordTab.vue';
import SettingTab from './SettingTab.vue';

const tab = ref('one');
function changeTab(e: string) {
  tab.value = e;
}
</script>

<template>
  <v-row class="mt-0">
    <v-col cols="12">
      <v-card class="profile-banner overflow-hidden" variant="flat" color="lightprimary" rounded="lg">
        <v-card-item class="pb-4 pt-2 px-6">
          <div class="d-flex justify-space-between align-center flex-wrap ga-4">
            <ProfileBanner />
            <v-btn variant="flat" color="primary" rounded="md" class="editBtn" @click="changeTab('one')">Edit your profile</v-btn>
          </div>
        </v-card-item>
        <UserBackLeft />
        <UserBackRight />
      </v-card>
    </v-col>
    <v-col cols="12" xl="3" md="4">
      <v-card variant="outlined" class="bg-surface" rounded="lg">
        <v-card-item>
          <div class="text-end">
            <v-menu class="rounded-md" elevation="24" rounded="md">
              <template v-slot:activator="{ props }">
                <v-btn icon color="secondary" aria-label="menu" size="small" v-bind="props" variant="tonal" rounded="md">
                  <SvgSprite name="custom-more-outline" style="width: 20px; height: 20px" />
                </v-btn>
              </template>
              <v-list elevation="24" aria-label="menu" aria-busy="true" density="compact" rounded="md">
                <v-list-item value="Edit" color="secondary" @click="changeTab('one')">
                  <v-list-item-title class="text-h6">Edit</v-list-item-title>
                </v-list-item>
                <v-list-item value="Delete" color="secondary" disabled>
                  <v-list-item-title class="text-h6">Delete</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
          <UserDetails />
          <v-tabs v-model="tab" color="primary" hide-slider density="compact" direction="vertical">
            <v-tab value="one" selected-class="bg-lightprimary" rounded="md" hide-slider>
              <SvgSprite name="custom-user-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Personal information
            </v-tab>
            <v-tab value="two" selected-class="bg-lightprimary" rounded="md" hide-slider
              ><SvgSprite name="custom-payment-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Payment
            </v-tab>
            <v-tab value="three" selected-class="bg-lightprimary" rounded="md" hide-slider
              ><SvgSprite name="custom-lock-2" class="v-icon--start" style="width: 18px; height: 18px" /> Change password
            </v-tab>
            <v-tab value="four" selected-class="bg-lightprimary" rounded="md" hide-slider
              ><SvgSprite name="custom-setup-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Settings
            </v-tab>
          </v-tabs>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="12" xl="9" md="8">
      <v-window v-model="tab">
        <v-window-item value="one">
          <InformationTab />
        </v-window-item>

        <v-window-item value="two">
          <PaymentTab />
        </v-window-item>

        <v-window-item value="three">
          <ChangePasswordTab />
        </v-window-item>

        <v-window-item value="four">
          <SettingTab />
        </v-window-item>
      </v-window>
    </v-col>
  </v-row>
</template>

<style>
.editBtn {
  @media (max-width: 600px) {
    width: 100%;
  }
}
</style>
