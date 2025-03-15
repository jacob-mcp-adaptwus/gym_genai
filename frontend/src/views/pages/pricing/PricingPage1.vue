<script setup lang="ts">
import { ref, shallowRef } from 'vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

const page = ref({ title: 'Price 1' });
const breadcrumbs = ref([
  {
    title: 'Pages',
    disabled: false,
    href: '#'
  },
  {
    title: 'Price 1',
    disabled: true,
    href: '#'
  }
]);

const plans = shallowRef([
  {
    active: false,
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
    title: 'Premium',
    description: '08 Services',
    price: {
      monthly: 599,
      yearly: 7089
    },
    permission: [0, 1, 2, 3, 4, 5, 6, 7]
  }
]);

const planList = ref([
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
    <v-col cols="12" md="4" sm="6" v-for="(plan, index) in plans" v-bind:key="index">
      <v-card elevation="0">
        <v-card variant="outlined" class="text-center">
          <v-card-text :class="plan.active ? 'pt-6' : 'pt-12'">
            <div class="pa-6 rounded-md" :class="plan.active ? 'bg-lightprimary' : 'bg-transparent'">
              <v-chip variant="flat" size="small" v-if="plan.active" class="mb-6" color="success" rounded="md">Popular</v-chip>
              <h1 class="mb-0 text-h4">{{ plan.title }}</h1>
              <p class="pb-5 text-h6 mb-0">{{ plan.description }}</p>
              <h2 class="text-h2 font-weight-bold mb-0" style="font-size: 40px !important" v-if="switch1 == true">
                <span>$</span>{{ plan.price.monthly }}
              </h2>
              <h2 class="text-h2 font-weight-bold mb-0" style="font-size: 40px !important" v-if="switch1 == false">
                <span>$</span>{{ plan.price.yearly }}
              </h2>
              <span class="text-h6 text-lightText">Lifetime</span>
              <v-btn
                :variant="plan.active ? 'flat' : 'outlined'"
                :color="plan.active ? 'primary' : 'secondary'"
                class="mt-6 mb-3"
                rounded="md"
                block
                >Order Now</v-btn
              >
            </div>
            <v-list class="PricingList" :class="plan.active ? 'mt-5' : ''" aria-label="price list" aria-busy="true">
              <v-list-item
                class="px-0"
                :disabled="!plan.permission.includes(index)"
                v-for="(list, index) in planList"
                :key="index"
                density="compact"
                :class="!plan.permission.includes(index) ? 'text-decoration-line-through text-disabled' : ''"
              >
                {{ list }}
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
