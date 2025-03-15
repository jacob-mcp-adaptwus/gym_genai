<script setup lang="ts">
import { ref, shallowRef } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

const page = ref({ title: 'Price 2' });
const breadcrumbs = ref([
  {
    title: 'Pages',
    disabled: false,
    href: '#'
  },
  {
    title: 'Price 2',
    disabled: true,
    href: '#'
  }
]);

const plans = shallowRef([
  {
    active: false,
    value: 'price1',
    title: 'Basic',
    description: '03 Services',
    price: {
      monthly: 69,
      yearly: 729
    },
    permission: [0, 1, 2]
  },
  {
    active: true,
    value: 'price2',
    title: 'Standard',
    description: '05 Services',
    price: {
      monthly: 129,
      yearly: 1449
    },
    permission: [0, 1, 2, 3, 4]
  },
  {
    active: false,
    value: 'price3',
    title: 'Premium',
    description: '08 Services',
    price: {
      monthly: 599,
      yearly: 7089
    },
    permission: [0, 1, 2, 3, 4, 5, 6, 7]
  }
]);

const pricingdata = ref([
  'One End Product', // 0
  'No attribution required', // 1
  'TypeScript', // 2
  'Figma Design Resources', // 3
  'Create Multiple Products', // 4
  'Create a SaaS Project', // 5
  'Resale Product', // 6
  'Separate sale of our UI Elements?' // 7
]);

const switch1 = ref(true);

const pricing = ref('price1');
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row class="align-center">
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="8" sm="12">
          <h5 class="text-h5 mb-0">Quality is never an accident. It is always the result of interlligent effort</h5>
          <p class="mb-0 text-h6 text-lightText">It makes no difference what the price is, it all makes senses to us.</p>
        </v-col>
        <v-col cols="12" md="4" sm="12">
          <div class="d-flex align-center justify-md-end">
            <h6 class="text-subtitle-1 text-lightText mb-0 me-2">Billed Yearly</h6>
            <v-switch color="primary" aria-label="switch" v-model="switch1" hide-details> </v-switch>
            <h6 class="text-subtitle-1 text-lightText mb-0 ms-2">Billed Monthly</h6>
          </div>
        </v-col>
      </v-row>
    </v-col>
    <v-col cols="12" xl="8" lg="7" md="6">
      <v-card variant="outlined" class="bg-surface">
        <v-card-text>
          <v-list class="PricingList" aria-label="price list" aria-busy="true" v-if="pricing == 'price3'">
            <v-list-item v-for="(plan, index) in pricingdata" v-bind:key="index" class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              {{ plan }}
            </v-list-item>
          </v-list>
          <v-list class="PricingList" aria-label="price list" aria-busy="true" v-if="pricing == 'price2'">
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              One End Product
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              No attribution required
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              TypeScript
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Figma Design Resources
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Create Multiple Products
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Create a SaaS Project
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Resale Product
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Separate sale of our UI Elements?
            </v-list-item>
          </v-list>
          <v-list class="PricingList" aria-label="price list" aria-busy="true" v-if="pricing == 'price1'">
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              One End Product
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              No attribution required
            </v-list-item>
            <v-list-item class="ps-0" density="compact" border>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              TypeScript
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Figma Design Resources
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Create Multiple Products
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Create a SaaS Project
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Resale Product
            </v-list-item>
            <v-list-item class="ps-0 text-decoration-line-through text-disabled" density="compact" border disabled>
              <SvgSprite name="custom-square-check-outline" class="text-success me-2" style="width: 16px; height: 16px" />
              Separate sale of our UI Elements?
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" xl="4" lg="5" md="6">
      <v-card variant="outlined" class="bg-surface">
        <v-card-text>
          <v-radio-group v-model="pricing" hide-details>
            <v-row>
              <v-col cols="12" sm="12" v-for="(plan, index) in plans" v-bind:key="index">
                <div class="py-5 px-4 border payment-method price-radio-btns rounded-md">
                  <v-radio :value="plan.value" color="primary" class="label-op-1">
                    <template v-slot:label>
                      <div class="d-flex align-center w-100">
                        <div class="flex-1-1">
                          <div class="d-flex justify-space-between flex-wrap">
                            <h5 class="text-h5 mb-0">
                              {{ plan.title }}
                              <v-chip variant="flat" size="small" v-if="plan.active" class="ms-3" color="success" rounded="lg"
                                >Popular</v-chip
                              >
                            </h5>
                            <div>
                              <h4 class="text-h4 font-weight-bold mb-0" v-if="switch1 == true">
                                <span>$</span>{{ plan.price.monthly }}<span class="text-h6 text-lightText"> /Lifetime</span>
                              </h4>
                              <h4 class="text-h4 font-weight-bold mb-0" v-if="switch1 == false">
                                <span>$</span>{{ plan.price.yearly }}<span class="text-h6 text-lightText"> /Lifetime</span>
                              </h4>
                            </div>
                          </div>
                          <span class="d-block text-h6 text-lightText">{{ plan.description }}</span>
                        </div>
                      </div>
                    </template>
                  </v-radio>
                </div>
              </v-col>
            </v-row>
          </v-radio-group>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
