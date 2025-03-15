<script setup lang="ts">
import { ref, shallowRef } from 'vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import KanbanList from '@/components/apps/kanban/KanbanList.vue';

const page = ref({ title: 'Kanban' });

const breadcrumbs = shallowRef([
  {
    title: 'Applications',
    disabled: false,
    href: '#'
  },
  {
    title: 'Kanban',
    disabled: true,
    href: '#'
  }
]);
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col lg="12">
      <KanbanList />
    </v-col>
  </v-row>
</template>
