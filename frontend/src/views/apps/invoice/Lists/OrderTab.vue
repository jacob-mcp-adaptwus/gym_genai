<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import type { Header, Item } from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

import user1 from '@/assets/images/users/avatar-5.png';
import user2 from '@/assets/images/users/avatar-4.png';
import user3 from '@/assets/images/users/avatar-7.png';
import user4 from '@/assets/images/users/avatar-1.png';
import user5 from '@/assets/images/users/avatar-2.png';

const searchField = ref('name');
const searchValue = ref('');

const headers: Header[] = [
  { text: 'Invoice ID', value: 'id', sortable: true },
  { text: 'User Name', value: 'name', sortable: true },
  { text: 'Create date', value: 'date', sortable: true },
  { text: 'Due date', value: 'due', sortable: true },
  { text: 'Quantity', value: 'qty', sortable: true },
  { text: 'Status', value: 'status', sortable: true },
  { text: 'Action', value: 'operation' }
];
const items = ref([
  {
    id: 1,
    name: 'Tessi Eneas',
    image: user1,
    mail: 'tass23@gmail.com',
    date: '05/01/2023',
    due: '06/02/2023',
    qty: '1000',
    status: 1
  },
  {
    id: 2,
    name: 'Abey Boseley',
    image: user2,
    mail: 'aabsl32@gmail.com',
    date: '7/15/2023',
    due: '2/15/2023',
    qty: '2030',
    status: 2
  },
  {
    id: 3,
    name: 'Shelba Thews',
    image: user3,
    mail: 'slbt37@gmail.com',
    date: '7/6/2023',
    due: '7/8/2023',
    qty: '3000',
    status: 3
  },
  {
    id: 4,
    name: 'Salvatore Boncore',
    image: user4,
    mail: 'sabf231@gmail.com',
    date: '2/8/2023',
    due: '3/30/2023',
    qty: '2000',
    status: 2
  },
  {
    id: 5,
    name: 'Mickie Melmoth',
    image: user5,
    mail: 'mmsht23@gmail.com',
    date: '5/5/2023',
    due: '7/11/2023',
    qty: '3000',
    status: 1
  }
]);
const items1 = ref([
  {
    id: 1,
    name: 'Tessi Eneas',
    image: user1,
    mail: 'tass23@gmail.com',
    date: '05/01/2023',
    due: '06/02/2023',
    qty: '1000',
    status: 1
  },
  {
    id: 5,
    name: 'Mickie Melmoth',
    image: user5,
    mail: 'mmsht23@gmail.com',
    date: '5/5/2023',
    due: '7/11/2023',
    qty: '3000',
    status: 1
  }
]);
const items2 = ref([
  {
    id: 2,
    name: 'Abey Boseley',
    image: user2,
    mail: 'aabsl32@gmail.com',
    date: '7/15/2023',
    due: '2/15/2023',
    qty: '2030',
    status: 2
  },
  {
    id: 4,
    name: 'Salvatore Boncore',
    image: user4,
    mail: 'sabf231@gmail.com',
    date: '2/8/2023',
    due: '3/30/2023',
    qty: '2000',
    status: 2
  }
]);
const items3 = ref([
  {
    id: 3,
    name: 'Shelba Thews',
    image: user3,
    mail: 'slbt37@gmail.com',
    date: '7/6/2023',
    due: '7/8/2023',
    qty: '3000',
    status: 3
  }
]);
const themeColor = ref('rgb(var(--v-theme-primary))');
const itemsSelected = ref<Item[]>([]);

// tabs data
const tab = ref(0);

function deleteRow(index: number) {
  items.value.splice(index, 1);
}
function deleteRow1(index: number) {
  items1.value.splice(index, 1);
}
function deleteRow2(index: number) {
  items2.value.splice(index, 1);
}
function deleteRow3(index: number) {
  items3.value.splice(index, 1);
}
</script>
<template>
  <v-card variant="outlined" class="bg-surface overflow-hidden" rounded="lg">
    <v-card-item>
      <v-tabs v-model="tab" color="primary">
        <v-tab value="1" class="font-weight-medium">
          All
          <v-chip color="primary" class="ms-2 font-weight-medium" size="small"> 5 </v-chip>
        </v-tab>
        <v-tab value="2" class="font-weight-medium">
          Paid
          <v-chip color="success" class="ms-2 font-weight-medium" size="small"> 2 </v-chip>
        </v-tab>
        <v-tab value="3" class="font-weight-medium">
          Unpaid
          <v-chip color="warning" class="ms-2 font-weight-medium" size="small"> 2 </v-chip>
        </v-tab>
        <v-tab value="4" class="font-weight-medium">
          Cancelled
          <v-chip color="error" class="ms-2 font-weight-medium" size="small"> 1 </v-chip>
        </v-tab>
      </v-tabs>
      <v-divider></v-divider>
    </v-card-item>
    <v-window v-model="tab">
      <v-window-item value="1">
        <div class="px-6">
          <v-row justify="space-between" class="align-center mb-3">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                placeholder="Search 5 records..."
                v-model="searchValue"
                density="comfortable"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn color="primary" variant="flat" rounded="md" to="/app/invoice/create">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-plus" style="width: 18px; height: 18px" />
                  </template>
                  Add invoice
                </v-btn>
                <v-btn icon variant="text" aria-label="download" color="secondary" rounded="md" size="small">
                  <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </div>
        <v-divider></v-divider>
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
          <template #item-name="{ name, image, mail }">
            <div class="player-wrapper d-flex align-center">
              <v-avatar size="32">
                <img :src="image" width="32" alt="profile" />
              </v-avatar>
              <div class="ms-2">
                <h5 class="text-subtitle-1 mb-0">{{ name }}</h5>
                <p class="text-h6 text-lightText mb-0">{{ mail }}</p>
              </div>
            </div>
          </template>
          <template #item-status="{ status }">
            <v-chip color="success" v-if="status === 1" size="small"> Paid </v-chip>
            <v-chip color="info" v-if="status === 2" size="small"> Unpaid </v-chip>
            <v-chip color="error" v-if="status === 3" size="small"> Cancelled </v-chip>
          </template>
          <template #item-operation>
            <div class="operation-wrapper">
              <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md" to="/app/invoice/details">
                <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">View</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="primary" aria-label="edit" variant="text" rounded="md">
                <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Edit</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="error" aria-label="trash" variant="text" rounded="md" @click="deleteRow">
                <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Delete</span>
                </v-tooltip>
              </v-btn>
            </div>
          </template>
        </EasyDataTable>
      </v-window-item>

      <v-window-item value="2">
        <div class="px-6">
          <v-row justify="space-between" class="align-center mb-3">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                placeholder="Search 5 records..."
                v-model="searchValue"
                density="comfortable"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn color="primary" variant="flat" rounded="md" to="/app/invoice/create">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-plus" style="width: 20px; height: 20px" />
                  </template>
                  Add invoice
                </v-btn>
                <v-btn icon variant="text" aria-label="download" rounded="md" color="secondary" size="small">
                  <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </div>
        <v-divider></v-divider>
        <EasyDataTable
          :headers="headers"
          :items="items1"
          table-class-name="customize-table invoice-table"
          :theme-color="themeColor"
          :search-field="searchField"
          :search-value="searchValue"
          :rows-per-page="5"
          v-model:items-selected="itemsSelected"
        >
          <template #item-name="{ name, image, mail }">
            <div class="player-wrapper d-flex align-center">
              <v-avatar size="32">
                <img :src="image" width="32" alt="profile" />
              </v-avatar>
              <div class="ms-2">
                <h5 class="text-subtitle-1 mb-0">{{ name }}</h5>
                <p class="text-h6 text-lightText mb-0">{{ mail }}</p>
              </div>
            </div>
          </template>
          <template #item-status="{ status }">
            <v-chip color="success" label v-if="status === 1" size="small"> Paid </v-chip>
            <v-chip color="info" label v-if="status === 2" size="small"> Unpaid </v-chip>
            <v-chip color="error" label v-if="status === 3" size="small"> Cancelled </v-chip>
          </template>
          <template #item-operation>
            <div class="operation-wrapper">
              <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md" to="/app/invoice/details">
                <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">View</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="primary" aria-label="edit" variant="text" rounded="md">
                <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Edit</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="error" aria-label="trash" variant="text" rounded="md" @click="deleteRow1">
                <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Delete</span>
                </v-tooltip>
              </v-btn>
            </div>
          </template>
        </EasyDataTable>
      </v-window-item>

      <v-window-item value="3">
        <div class="px-6">
          <v-row justify="space-between" class="align-center mb-3">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                placeholder="Search 5 records..."
                v-model="searchValue"
                density="comfortable"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn color="primary" variant="flat" rounded="md" to="/app/invoice/create">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-plus" style="width: 20px; height: 20px" />
                  </template>
                  Add invoice
                </v-btn>
                <v-btn icon variant="text" aria-label="download" rounded="md" color="secondary" size="small">
                  <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </div>
        <v-divider></v-divider>
        <EasyDataTable
          :headers="headers"
          :items="items2"
          table-class-name="customize-table invoice-table"
          :theme-color="themeColor"
          :search-field="searchField"
          :search-value="searchValue"
          :rows-per-page="5"
          v-model:items-selected="itemsSelected"
        >
          <template #item-name="{ name, image, mail }">
            <div class="player-wrapper d-flex align-center">
              <v-avatar size="32">
                <img :src="image" width="32" alt="profile" />
              </v-avatar>
              <div class="ms-2">
                <h5 class="text-subtitle-1 mb-0">{{ name }}</h5>
                <p class="text-h6 text-lightText mb-0">{{ mail }}</p>
              </div>
            </div>
          </template>
          <template #item-status="{ status }">
            <v-chip color="success" label v-if="status === 1" size="small"> Paid </v-chip>
            <v-chip color="info" label v-if="status === 2" size="small"> Unpaid </v-chip>
            <v-chip color="error" label v-if="status === 3" size="small"> Cancelled </v-chip>
          </template>
          <template #item-operation>
            <div class="operation-wrapper">
              <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md" to="/app/invoice/details">
                <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">View</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="primary" aria-label="edit" variant="text" rounded="md">
                <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Edit</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="error" aria-label="trash" variant="text" rounded="md" @click="deleteRow2">
                <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Delete</span>
                </v-tooltip>
              </v-btn>
            </div>
          </template>
        </EasyDataTable>
      </v-window-item>

      <v-window-item value="4">
        <div class="px-6">
          <v-row justify="space-between" class="align-center mb-2">
            <v-col cols="12" md="3">
              <v-text-field
                type="text"
                variant="outlined"
                persistent-placeholder
                placeholder="Search 5 records..."
                v-model="searchValue"
                density="comfortable"
                hide-details
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
            <v-col cols="12" md="3">
              <div class="d-flex ga-2 justify-end">
                <v-btn color="primary" variant="flat" rounded="md" to="/app/invoice/create">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-plus" style="width: 20px; height: 20px" />
                  </template>
                  Add invoice
                </v-btn>
                <v-btn icon variant="text" aria-label="download" rounded="md" color="secondary" size="small">
                  <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
                </v-btn>
              </div>
            </v-col>
          </v-row>
        </div>
        <v-divider></v-divider>
        <EasyDataTable
          :headers="headers"
          :items="items3"
          table-class-name="customize-table invoice-table"
          :theme-color="themeColor"
          :search-field="searchField"
          :search-value="searchValue"
          :rows-per-page="5"
          v-model:items-selected="itemsSelected"
        >
          <template #item-name="{ name, image, mail }">
            <div class="player-wrapper d-flex align-center">
              <v-avatar size="32">
                <img :src="image" width="32" alt="profile" />
              </v-avatar>
              <div class="ms-2">
                <h5 class="text-subtitle-1 mb-0">{{ name }}</h5>
                <p class="text-h6 text-lightText mb-0">{{ mail }}</p>
              </div>
            </div>
          </template>
          <template #item-status="{ status }">
            <v-chip color="success" label v-if="status === 1" size="small"> Paid </v-chip>
            <v-chip color="info" label v-if="status === 2" size="small"> Unpaid </v-chip>
            <v-chip color="error" label v-if="status === 3" size="small"> Cancelled </v-chip>
          </template>
          <template #item-operation>
            <div class="operation-wrapper">
              <v-btn icon color="secondary" aria-label="view" variant="text" rounded="md" to="/app/invoice/details">
                <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">View</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="primary" aria-label="edit" variant="text" rounded="md">
                <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Edit</span>
                </v-tooltip>
              </v-btn>
              <v-btn icon color="error" aria-label="trash" variant="text" rounded="md" @click="deleteRow3">
                <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                <v-tooltip activator="parent" aria-label="tooltip" location="bottom" content-class="smallTooltip">
                  <span class="text-caption">Delete</span>
                </v-tooltip>
              </v-btn>
            </div>
          </template>
        </EasyDataTable>
      </v-window-item>
    </v-window>
  </v-card>
</template>
