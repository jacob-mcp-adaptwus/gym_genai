<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

const page = ref({ title: 'Add New product' });
const breadcrumbs = ref([
  {
    title: 'Ecommerce',
    disabled: false,
    href: '#'
  },
  {
    title: 'Add New product',
    disabled: true,
    href: '#'
  }
]);

const items = ref(['100', '200', '300', '400']);
const items1 = ref(['1', '2', '3']);
const items2 = ref(['In stock', 'Out of stock']);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col>
      <v-card variant="outlined" class="bg-surface" rounded="lg">
        <v-card-text>
          <v-row>
            <v-col md="6" cols="12">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div>
                    <v-label class="mb-2">Product Name</v-label>
                    <v-text-field
                      color="primary"
                      single-line
                      density="comfortable"
                      variant="outlined"
                      placeholder="Enter product name"
                    ></v-text-field>
                  </div>
                  <div>
                    <v-label class="mb-2">Product Description</v-label>
                    <v-textarea
                      color="primary"
                      single-line
                      density="comfortable"
                      variant="outlined"
                      rows="3"
                      placeholder="Enter product description"
                    ></v-textarea>
                  </div>
                  <div>
                    <v-label class="mb-2">Category</v-label>
                    <v-text-field
                      color="primary"
                      single-line
                      density="comfortable"
                      variant="outlined"
                      rows="3"
                      placeholder="Enter your category"
                    ></v-text-field>
                  </div>
                  <div>
                    <v-label class="mb-2">Price</v-label>
                    <v-autocomplete
                      model-value="200"
                      :items="items"
                      aria-label="autocomplete"
                      color="primary"
                      variant="outlined"
                      hide-details
                      density="comfortable"
                    >
                      <template v-slot:prepend-inner> $ </template>
                    </v-autocomplete>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col md="6" cols="12">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div class="mb-5">
                    <v-label class="mb-2">Qty</v-label>
                    <v-autocomplete
                      model-value="1"
                      aria-label="autocomplete"
                      :items="items1"
                      color="primary"
                      variant="outlined"
                      hide-details
                      density="comfortable"
                    >
                    </v-autocomplete>
                  </div>
                  <div class="mb-5">
                    <v-label class="mb-2">Status</v-label>
                    <v-autocomplete
                      aria-label="autocomplete"
                      model-value="In stock"
                      :items="items2"
                      color="primary"
                      variant="outlined"
                      hide-details
                      density="comfortable"
                    >
                    </v-autocomplete>
                  </div>
                  <p class="text-h6 text-lightText mb-2">
                    <span class="text-error">* </span>Recommended resolution is 640*640 with file size
                  </p>
                  <v-btn variant="outlined" color="secondary" rounded="md">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-upload-outline-1" style="width: 18px; height: 18px" />
                    </template>
                    Click to upload
                  </v-btn>
                  <div class="d-flex justify-end ga-4 mt-16 pt-8">
                    <v-btn variant="outlined" color="secondary" rounded="md" to="/ecommerce/productlist"> Cancel </v-btn>
                    <v-btn variant="flat" color="primary" rounded="md"> Add new product </v-btn>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
