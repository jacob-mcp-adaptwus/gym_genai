<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiTableCard from '@/components/shared/UiTableCard.vue';

// theme breadcrumb
const page = ref({ title: 'Fixed Header Table' });
const breadcrumbs = ref([
  {
    title: 'Tables',
    disabled: false,
    href: '#'
  },
  {
    title: 'Fixed Header Table',
    disabled: true,
    href: '#'
  }
]);

// table data

const tableData = ref([
  {
    name: 'India',
    code: 'IN',
    population: '1,324,171,354',
    size: '3,287,263',
    density: '402.82'
  },
  {
    name: 'China',
    code: 'CN',
    population: '1,403,500,365',
    size: '9,596,961',
    density: '146.24'
  },
  {
    name: 'Italy',
    code: 'IT',
    population: '60,483,973',
    size: '301,340',
    density: '200.72'
  },
  {
    name: 'United States',
    code: 'US',
    population: '327,167,434',
    size: '9,833,520',
    density: '33.27'
  },
  {
    name: 'Canada',
    code: 'CA',
    population: '37,602,103',
    size: '9,984,670',
    density: '3.77'
  }
]);
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Table Header Fixed -->
  <!-- ---------------------------------------------------- -->
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <UiTableCard title="Header Fixed Table">
        <v-table fixed-header height="300px" style="height: 300px; overflow-y: auto" tabindex="0" class="bordered-table rounded-0" hover>
          <thead>
            <tr>
              <th class="text-start text-uppercase text-caption font-weight-bold bg-containerBg">name</th>
              <th class="text-start text-uppercase text-caption font-weight-bold bg-containerBg">ISO code</th>
              <th class="text-start text-uppercase text-caption font-weight-bold bg-containerBg">Population</th>
              <th class="text-start text-uppercase text-caption font-weight-bold bg-containerBg">size(km<sup>2</sup>)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold bg-containerBg">density</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in tableData" :key="item.name" class="text-lighttext">
              <td class="text-subtitle-1 font-weight-regular">{{ item.name }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.code }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.population }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.size }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.density }}</td>
            </tr>
          </tbody>
        </v-table>
      </UiTableCard>
    </v-col>
  </v-row>
</template>
