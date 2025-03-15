<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

// tabs import
import ProfileTab from './ProfileTab.vue';
import PersonalDetailsTab from './PersonalDetailsTab.vue';
import MyAccountTab from './MyAccountTab.vue';
import ChangePassword from './ChangePassword.vue';
import SettingsTab from './SettingsTab.vue';

// theme breadcrumb
const page = ref({ title: 'Profile 01' });
const breadcrumbs = ref([
  {
    title: 'Users',
    disabled: false,
    href: '#'
  },
  {
    title: 'Account',
    disabled: false,
    href: '#'
  },
  {
    title: 'Profile 01',
    disabled: true,
    href: '#'
  }
]);

// tabs data
const tab = ref('tab-profile');
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <v-card-text class="px-0 pb-0">
            <v-tabs v-model="tab" class="mx-6" color="primary">
              <v-tab value="tab-profile"
                ><SvgSprite name="custom-user-outline" class="v-icon--start" style="width: 18px; height: 18px" />Profile</v-tab
              >
              <v-tab value="tab-personal"
                ><SvgSprite name="custom-document-text-outline" class="v-icon--start" style="width: 18px; height: 18px" />Personal</v-tab
              >
              <v-tab value="tab-account"
                ><SvgSprite name="custom-file-text-outline" class="v-icon--start" style="width: 18px; height: 18px" />My Account</v-tab
              >
              <v-tab value="tab-password"
                ><SvgSprite name="custom-lock-2" class="v-icon--start" style="width: 18px; height: 18px" />Change Password</v-tab
              >
              <v-tab value="tab-setting"
                ><SvgSprite name="custom-setup-outline" class="v-icon--start" style="width: 18px; height: 18px" />Settings</v-tab
              >
            </v-tabs>
            <v-divider class="mx-6" />
            <div class="pt-6">
              <v-window v-model="tab" class="px-6 pb-6">
                <v-window-item value="tab-profile">
                  <ProfileTab />
                </v-window-item>

                <v-window-item value="tab-personal">
                  <PersonalDetailsTab />
                </v-window-item>

                <v-window-item value="tab-account">
                  <MyAccountTab />
                </v-window-item>

                <v-window-item value="tab-password">
                  <ChangePassword />
                </v-window-item>

                <v-window-item value="tab-setting">
                  <SettingsTab />
                </v-window-item>
              </v-window>
            </div>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
