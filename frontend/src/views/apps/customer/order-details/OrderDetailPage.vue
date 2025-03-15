<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import DetailsTab from './DetailsTab.vue';
import InvoiceTab from './InvoiceTab.vue';
import StatusTab from './StatusTab.vue';

// theme breadcrumb
const page = ref({ title: 'Order Details' });
const breadcrumbs = ref([
  {
    title: 'Customer',
    disabled: false,
    href: '#'
  },
  {
    title: 'Order Details',
    disabled: true,
    href: '#'
  }
]);

const tab2 = ref(null);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <!-- customer detail table -->
      <v-tabs v-model="tab2" color="primary">
        <v-tab value="11">
          <SvgSprite name="custom-document-text-outline" class="v-icon--start" style="width: 16px; height: 16px" /> Details
        </v-tab>
        <v-tab value="22">
          <SvgSprite name="custom-wallet-outline" class="v-icon--start" style="width: 16px; height: 16px" /> Invoice
        </v-tab>
        <v-tab value="33"> <SvgSprite name="custom-page-outline" class="v-icon--start" style="width: 16px; height: 16px" /> Status </v-tab>
      </v-tabs>
      <v-divider class="mb-6"></v-divider>
      <v-card-text class="px-0 py-0 mx-n6 mb-n6">
        <v-window v-model="tab2" class="px-6 pb-6">
          <v-window-item value="11">
            <!-- Details tab -->
            <DetailsTab />
          </v-window-item>

          <v-window-item value="22">
            <InvoiceTab />
          </v-window-item>

          <v-window-item value="33">
            <StatusTab />
          </v-window-item>
        </v-window>
      </v-card-text>
    </v-col>
  </v-row>
</template>
