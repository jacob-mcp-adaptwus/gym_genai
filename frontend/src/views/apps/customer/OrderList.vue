<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useCustomers } from '@/stores/apps/customers';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import type { Header, Item } from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

// theme breadcrumb
const page = ref({ title: 'Order List' });
const breadcrumbs = ref([
  {
    title: 'Customer',
    disabled: false,
    href: '#'
  },
  {
    title: 'Order List',
    disabled: true,
    href: '#'
  }
]);

const store = useCustomers();

const getOrders = computed(() => {
  return store.getOrders;
});

onMounted(() => {
  store.fetchOrders();
});

const searchField = ref('name');
const searchValue = ref('');

const headers: Header[] = [
  { text: 'ID', value: 'id', sortable: true },
  { text: 'Customer name', value: 'name', sortable: true },
  { text: 'Branch', value: 'company', sortable: true },
  { text: 'Payment Type', value: 'type', sortable: true },
  { text: 'Quantity', value: 'qty', sortable: true },
  { text: 'Registered', value: 'date', sortable: true },
  { text: 'Status', value: 'status', sortable: true },
  { text: 'Action', value: 'operation' }
];
const items = ref(getOrders);
const themeColor = ref('rgb(var(--v-theme-primary))');
const { deleteOrder } = store;
const itemsSelected = ref<Item[]>([]);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" md="12">
      <v-card elevation="0" variant="outlined" class="bg-surface overflow-hidden">
        <v-card-item>
          <v-row justify="space-between" class="align-center">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                density="comfortable"
                placeholder="Search Order"
                v-model="searchValue"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn icon variant="text" aria-label="copy" rounded="md">
                  <SvgSprite name="custom-copy" style="width: 16px; height: 16px" />
                </v-btn>
                <v-btn icon variant="text" aria-label="print" rounded="md">
                  <SvgSprite name="custom-printer-outline" style="width: 16px; height: 16px" />
                </v-btn>
                <v-btn icon variant="text" aria-label="filter" rounded="md">
                  <SvgSprite name="custom-filter" style="width: 16px; height: 16px" />
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </v-card-item>
        <v-divider></v-divider>
        <v-card-text class="pa-0">
          <EasyDataTable
            :headers="headers"
            :items="items"
            table-class-name="customize-table invoice-table"
            :theme-color="themeColor"
            :search-field="searchField"
            :search-value="searchValue"
            :rows-per-page="5"
            v-model:items-selected="itemsSelected"
          >
            <template #item-id="{ id }">
              <div class="player-wrapper">
                <h5 class="text-h5">#{{ id }}</h5>
              </div>
            </template>
            <template #item-name="{ name }">
              <div class="player-wrapper">
                <h5 class="text-h5">{{ name }}</h5>
              </div>
            </template>
            <template #item-status="{ status }">
              <v-chip color="success" v-if="status === 1" size="small"> Complete </v-chip>
              <v-chip color="error" v-if="status === 2" size="small"> Processing </v-chip>
              <v-chip color="primary" v-if="status === 3" size="small"> Confirm </v-chip>
            </template>
            <template #item-operation="item">
              <div class="operation-wrapper">
                <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md">
                  <SvgSprite name="custom-eye" style="width: 18px; height: 18px" />
                </v-btn>
                <v-btn icon color="primary" aria-label="trash" variant="text" rounded="md" @click="deleteOrder(item.id)">
                  <SvgSprite name="custom-trash" style="width: 18px; height: 18px" />
                </v-btn>
              </div>
            </template>
          </EasyDataTable>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
