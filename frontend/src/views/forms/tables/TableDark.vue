<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiTableCard from '@/components/shared/UiTableCard.vue';

// theme breadcrumb
const page = ref({ title: 'Dark Table' });
const breadcrumbs = ref([
  {
    title: 'Tables',
    disabled: false,
    href: '#'
  },
  {
    title: 'Dark Table',
    disabled: true,
    href: '#'
  }
]);

// table data

const desserts = ref([
  {
    name: 'Frozen Yogurt',
    calories: 159,
    fat: 6.0,
    carbs: 24,
    protein: 4.0
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
    fat: 9.0,
    carbs: 37,
    protein: 4.3
  },
  {
    name: 'Eclair',
    calories: 262,
    fat: 16.0,
    carbs: 24,
    protein: 6
  },
  {
    name: 'Cupcake',
    calories: 305,
    fat: 3.7,
    carbs: 67,
    protein: 4.3
  },
  {
    name: 'Gingerbread',
    calories: 356,
    fat: 16.0,
    carbs: 49,
    protein: 3.9
  }
]);
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Table Dark -->
  <!-- ---------------------------------------------------- -->
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <UiTableCard title="Dark Table">
        <v-table theme="dark" class="rounded-0">
          <thead>
            <tr>
              <th class="text-start text-uppercase text-caption font-weight-bold">Dessert (100g serving)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Calories</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Fat (g)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Carbs (g)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Protein (g)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Protein (g)</th>
              <th class="text-start text-uppercase text-caption font-weight-bold">Protein (g)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in desserts" :key="item.name" class="text-lighttext">
              <td class="text-subtitle-1 font-weight-regular">{{ item.name }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.calories }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.fat }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.carbs }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.protein }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.protein }}</td>
              <td class="text-subtitle-1 font-weight-regular">{{ item.protein }}</td>
            </tr>
          </tbody>
        </v-table>
      </UiTableCard>
    </v-col>
  </v-row>
</template>
