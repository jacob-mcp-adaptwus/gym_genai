<script setup lang="ts">
import { ref, computed, onMounted, shallowRef } from 'vue';
import { useCustomers } from '@/stores/apps/customers';

import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import type { Header, Item } from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

const page = ref({ title: 'Customer list' });

const breadcrumbs = shallowRef([
  {
    title: 'Customer',
    disabled: false,
    href: '#'
  },
  {
    title: 'List',
    disabled: true,
    href: '#'
  }
]);

const store = useCustomers();

const getCustomers = computed(() => {
  return store.getCustomers;
});

onMounted(() => {
  store.fetchCustomers();
});

const searchField = ref('name');
const searchValue = ref('');

const headers: Header[] = [
  { text: 'Customer name', value: 'name', sortable: true },
  { text: 'Contact', value: 'date', sortable: true },
  { text: 'Age', value: 'orders', sortable: true },
  { text: 'Country', value: 'location', sortable: true },
  { text: 'Status', value: 'status', sortable: true },
  { text: 'Action', value: 'operation' }
];
const items = ref(getCustomers);
const themeColor = ref('rgb(var(--v-theme-primary))');
const { deleteCustomer } = store;

const itemsSelected = ref<Item[]>([]);

const dialog = ref(false);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" md="12">
      <v-card elevation="0" variant="outlined" class="bg-surface overflow-hidden" rounded="lg">
        <v-card-item>
          <v-row justify="space-between" class="align-center">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                placeholder="Search 200 records..."
                v-model="searchValue"
                density="comfortable"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 14px; height: 14px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-dialog v-model="dialog" class="customer-modal">
                  <template v-slot:activator="{ props }">
                    <v-btn variant="flat" color="primary" rounded="md" v-bind="props">
                      <template v-slot:prepend>
                        <SvgSprite name="custom-plus" style="width: 20px; height: 20px" />
                      </template>
                      Add customer
                    </v-btn>
                  </template>
                  <v-card>
                    <perfect-scrollbar style="max-height: calc(100vh - 48px)">
                      <v-card-title class="pa-5">
                        <span class="text-h5">New Customer</span>
                      </v-card-title>
                      <v-divider></v-divider>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col md="3" cols="12" class="text-center">
                              <v-avatar size="72" variant="outlined" color="primary" class="dashed">
                                <img src="@/assets/images/users/avatar-1.png" width="72" alt="profile" />
                                <input type="file" aria-label="upload" class="preview-upload" />
                              </v-avatar>
                            </v-col>
                            <v-col md="9" cols="12">
                              <v-row>
                                <v-col cols="12">
                                  <v-label class="mb-2">First name</v-label>
                                  <v-text-field
                                    single-line
                                    placeholder="Enter first name"
                                    hide-details
                                    variant="outlined"
                                    required
                                    density="comfortable"
                                    rounded="0"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                  <v-label class="mb-2">Email</v-label>
                                  <v-text-field
                                    single-line
                                    type="email"
                                    hide-details
                                    placeholder="Enter customer email"
                                    required
                                    variant="outlined"
                                    density="comfortable"
                                    rounded="0"
                                  ></v-text-field>
                                </v-col>
                                <v-col cols="12">
                                  <v-label class="mb-2">Status</v-label>
                                  <v-autocomplete
                                    :items="['Single', 'Relationship', 'Complicated']"
                                    label="Single"
                                    rounded="0"
                                    color="primary"
                                    single-line
                                    density="comfortable"
                                    hide-details
                                    variant="outlined"
                                  ></v-autocomplete>
                                </v-col>
                                <v-col cols="12">
                                  <v-label class="mb-2">Location</v-label>
                                  <v-textarea
                                    placeholder="Enter location"
                                    hide-details
                                    rows="2"
                                    variant="outlined"
                                    density="comfortable"
                                  ></v-textarea>
                                </v-col>
                                <v-col cols="12">
                                  <div class="d-flex justify-space-between ga-2">
                                    <div class="pb-4">
                                      <h6 class="text-subtitle-1 mb-1">Make Contact Info Public</h6>
                                      <p class="text-caption text-lightText mb-0 me-5">
                                        Means that anyone viewing your profile will be able to see your contacts details
                                      </p>
                                    </div>
                                    <v-switch
                                      color="primary"
                                      aria-label="switch"
                                      class="switchRight"
                                      :model-value="true"
                                      hide-details
                                    ></v-switch>
                                  </div>
                                  <v-divider></v-divider>
                                </v-col>
                                <v-col cols="12" class="pt-0">
                                  <div class="d-flex justify-space-between ga-2">
                                    <div class="pb-4 pt-1">
                                      <h6 class="text-subtitle-1 mb-1">Available to hire</h6>
                                      <p class="text-caption text-lightText mb-0 me-5">
                                        Toggling this will let your teammates know that you are available for acquiring new projects
                                      </p>
                                    </div>
                                    <v-switch
                                      color="primary"
                                      aria-label="switch"
                                      class="switchRight"
                                      :model-value="false"
                                      hide-details
                                    ></v-switch>
                                  </div>
                                </v-col>
                              </v-row>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="error" rounded="md" variant="text" @click="dialog = false"> Cancel </v-btn>
                        <v-btn color="primary" rounded="md" variant="flat" @click="dialog = false"> Add </v-btn>
                      </v-card-actions>
                    </perfect-scrollbar>
                  </v-card>
                </v-dialog>
                <v-btn icon variant="text" aria-label="download" rounded="md" size="small">
                  <SvgSprite name="custom-document-2" class="text-lightText" style="width: 24px; height: 24px" />
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
            :rows-per-page="10"
            v-model:items-selected="itemsSelected"
          >
            <template #item-name="{ name, email }">
              <div class="player-wrapper">
                <h6 class="text-subtitle-1 mb-0">{{ name }}</h6>
                <small class="text-h6 text-lightText">{{ email }}</small>
              </div>
            </template>
            <template #item-status="{ status }">
              <v-chip color="success" v-if="status === 1" size="small"> Relationship </v-chip>
              <v-chip color="error" v-if="status === 2" size="small"> Complicated </v-chip>
              <v-chip color="info" v-if="status === 3" size="small"> Single </v-chip>
            </template>
            <template #item-operation="item">
              <div class="operation-wrapper">
                <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md">
                  <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
                </v-btn>
                <v-btn icon color="primary" aria-label="edit" variant="text" rounded="md">
                  <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                </v-btn>
                <v-btn icon color="error" aria-label="trash" variant="text" @click="deleteCustomer(item.name)" rounded="md">
                  <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                </v-btn>
              </div>
            </template>
          </EasyDataTable>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.customer-modal {
  width: calc(100% - 48px);
  min-width: 340px;
  max-width: 820px;
}
</style>
