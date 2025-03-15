<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

// tabs import
import ProfileTab from './ProfileTab.vue';
import BillingTab from './BillingTab.vue';
import SecurityTab from './SecurityTab.vue';
import NotificationsTab from './NotificationsTab.vue';

// theme breadcrumb
const page = ref({ title: 'Profile 03' });
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
    title: 'Profile 03',
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
              <v-tab variant="text" value="tab-profile">Profile</v-tab>
              <v-tab variant="text" value="tab-billing">Billing</v-tab>
              <v-tab variant="text" value="tab-security">Security</v-tab>
              <v-tab variant="text" value="tab-notifications">Notifications</v-tab>
            </v-tabs>
            <v-divider class="mx-6"></v-divider>
            <div class="pt-6">
              <v-window v-model="tab" class="px-6 pb-6">
                <v-window-item value="tab-profile">
                  <ProfileTab />
                </v-window-item>

                <v-window-item value="tab-billing">
                  <BillingTab />
                </v-window-item>

                <v-window-item value="tab-security">
                  <SecurityTab />
                </v-window-item>

                <v-window-item value="tab-notifications">
                  <NotificationsTab />
                </v-window-item>
              </v-window>
            </div>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
