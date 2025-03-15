<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import WidgetCharts from './Lists/WidgetCharts.vue';
import RecievableCard from './Lists/RecievableCard.vue';
import OrderTab from './Lists/OrderTab.vue';

// theme breadcrumb
const page = ref({ title: 'List' });
const breadcrumbs = ref([
  {
    title: 'Invoice',
    disabled: false,
    href: '#'
  },
  {
    title: 'List',
    disabled: true,
    href: '#'
  }
]);
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" lg="8">
      <WidgetCharts />
    </v-col>
    <v-col cols="12" lg="4">
      <RecievableCard />
    </v-col>
    <v-col cols="12">
      <OrderTab />
    </v-col>
  </v-row>
</template>
