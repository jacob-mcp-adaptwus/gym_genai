<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import TabCard from './Dashboard/TabCard.vue';
import InvoiceStatus from './Dashboard/InvoiceStatus.vue';
import RecentInvoice from './Dashboard/RecentInvoice.vue';
import TotalExpense from './Dashboard/TotalExpense.vue';
import NotificationInvoice from './Dashboard/NotificationInvoice.vue';

// theme breadcrumb
const page = ref({ title: 'My Dashboard' });
const breadcrumbs = ref([
  {
    title: 'Invoice',
    disabled: false,
    href: '#'
  },
  {
    title: 'Invoice Summary',
    disabled: true,
    href: '#'
  }
]);
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" xl="9" lg="7">
      <TabCard />
    </v-col>
    <v-col cols="12" xl="3" lg="5">
      <InvoiceStatus />
    </v-col>
    <v-col cols="12" lg="4" md="6">
      <RecentInvoice />
    </v-col>
    <v-col cols="12" lg="4" md="6">
      <TotalExpense />
    </v-col>
    <v-col cols="12" lg="4" md="6">
      <NotificationInvoice />
    </v-col>
  </v-row>
</template>
