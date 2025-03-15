<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useEcomStore } from '@/stores/apps/eCommerce';
import type { Header, Item } from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';
import { format, isValid } from 'date-fns';

const store = useEcomStore();
onMounted(() => {
  store.fetchProducts();
});
const getProducts = computed(() => {
  return store.products;
});

const searchField = ref('name');
const searchValue = ref('');

const headers: Header[] = [
  { text: '#', value: 'image' },
  { text: 'Product detail', value: 'name', sortable: true },
  { text: 'Created', value: 'created', sortable: true },
  { text: 'Price', value: 'offerPrice', sortable: true },
  { text: 'Sale price', value: 'salePrice', sortable: true },
  { text: 'status', value: 'isStock' },
  { text: 'Action', value: 'operation' }
];
const items = ref(getProducts);
const themeColor = ref('rgb(var(--v-theme-primary))');

const itemsSelected = ref<Item[]>([]);

const isValidDate = (date: string | number | Date) => {
  // Check if the date is valid
  return isValid(new Date(date));
};
</script>

<template>
  <v-row class="mt-0">
    <v-col cols="12" md="12">
      <v-card variant="outlined" class="bg-surface overflow-hidden" rounded="lg">
        <v-card-item>
          <v-row justify="space-between" class="align-center">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                density="comfortable"
                placeholder="Search Product"
                v-model="searchValue"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn variant="flat" rounded="md" color="primary" to="/ecommerce/add-product">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-plus" style="width: 18px; height: 18px" />
                  </template>
                  Add product
                </v-btn>
                <v-btn icon variant="text" aria-label="download" rounded="md">
                  <SvgSprite name="custom-download-outline" class="text-lightText" style="width: 20px; height: 20px" />
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
            <template #item-image="{ image }">
              <div class="player-wrapper">
                <img alt="product" width="32" class="rounded-md bg-gray100" :src="image" />
              </div>
            </template>
            <template #item-name="{ name }">
              <div class="player-wrapper">
                <h5 class="text-subtitle-1 mb-0">{{ name }}</h5>
              </div>
            </template>
            <template #item-created="{ date }">
              <div class="player-wrapper">
                {{ isValidDate(date) ? format(new Date(date), 'E, MMM d') : 'Mon, Mar 10' }}
              </div>
            </template>
            <template #item-offerPrice="{ offerPrice }">
              <div class="player-wrapper">
                <span class="text-h6">${{ offerPrice }}</span>
              </div>
            </template>
            <template #item-salePrice="{ salePrice }">
              <div class="player-wrapper">
                <span class="text-h6">${{ salePrice }}</span>
              </div>
            </template>
            <template #item-isStock="{ isStock }">
              <div class="player-wrapper">
                <v-chip color="success" v-if="isStock" size="small"> In Stock </v-chip>
                <v-chip color="error" v-else size="small"> Out of Stock </v-chip>
              </div>
            </template>

            <template #item-operation>
              <div class="operation-wrapper">
                <v-btn icon variant="text" aria-label="view" rounded="md">
                  <SvgSprite name="custom-eye" class="text-lightText" style="width: 18px; height: 18px" />
                </v-btn>
              </div>
            </template>
          </EasyDataTable>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
