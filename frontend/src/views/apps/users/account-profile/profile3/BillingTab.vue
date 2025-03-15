<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

import visaImg from '@/assets/images/pages/visa.png';
import discoverImg from '@/assets/images/pages/discover.png';
import masterImg from '@/assets/images/pages/mastercard.png';

const bills = ref([
  {
    title: 'Bill Due',
    color: 'error',
    subtitle: '$150.00',
    moveto: 'Pay Now'
  },
  {
    title: 'Total Credits',
    color: 'warning',
    subtitle: '1570 GB',
    moveto: 'Full Report'
  },
  {
    title: 'Plan',
    color: 'success',
    subtitle: 'Basic',
    moveto: 'Upgrade ?'
  }
]);

const methods = ref([
  {
    img: visaImg,
    name: 'Visa card',
    excode: '5269 07XX XXXX 8110',
    default: true,
    divider: true
  },
  {
    img: discoverImg,
    name: 'Discover',
    excode: '6109 07XX XXXX 8020',
    default: false,
    divider: true
  },
  {
    img: masterImg,
    name: 'Mastercard',
    excode: '7278 07XX XXXX 4290',
    default: false,
    divider: false
  }
]);

const billhistory = ref([
  {
    orderno: '12877227695',
    date: '26 Feb 2021 9:16 am',
    price: '56.32',
    wait: true
  },
  {
    orderno: '12901477937',
    date: '30 Jan 2021 2:54 pm',
    price: '75.56',
    wait: false
  },
  {
    orderno: '12767886919',
    date: '22 Jan 2021 12:01 pm',
    price: '34.23',
    wait: false
  }
]);
</script>

<template>
  <v-row>
    <v-col cols="12" md="4" sm="6" v-for="(bill, i) in bills" :key="i">
      <div :class="'pa-5 rounded-lg v-alert--border v-alert--border-start  position-relative bg-light' + bill.color">
        <div :class="'v-alert__border bg-' + bill.color"></div>
        <span>{{ bill.title }}</span>
        <h2 class="text-h2 mb-3 font-weight-medium">{{ bill.subtitle }}</h2>
        <span :class="'text-subtitle-1 cursor-pointer font-weight-medium text-decoration-none d-flex align-center text-' + bill.color">
          {{ bill.moveto }}
          <SvgSprite name="custom-arrow-right" class="ms-1" style="width: 16px; height: 16px" />
        </span>
      </div>
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="12">
      <v-card variant="flat" rounded="lg" class="mt-3">
        <v-card variant="outlined" class="overflow-hidden" rounded="lg">
          <v-list aria-label="title" aria-busy="true">
            <v-list-item class="d-sm-flex d-block">
              <template v-slot:title>
                <h5 class="text-subtitle-1 mt-1 mb-3 mb-sm-0">Payment Methods</h5>
              </template>
              <template v-slot:append>
                <v-btn size="small" color="primary" rounded="md" variant="flat" class="ms-2"> Add New Method </v-btn>
              </template>
            </v-list-item>
          </v-list>
          <v-divider></v-divider>
          <v-card-text class="pa-0">
            <v-list lines="two" density="compact" aria-label="method list" aria-busy="true">
              <template v-for="(method, i) in methods" :key="i">
                <v-list-item>
                  <template v-slot:prepend>
                    <img :src="method.img" :alt="method.img" width="60" class="me-3" />
                  </template>
                  <template v-slot:title>
                    <div class="d-none d-sm-block">
                      <h5 class="text-subtitle-1 mt-1 mb-0">{{ method.name }}</h5>
                      <span class="text-subtitle-2 text-disabled font-weight-medium">Ending in {{ method.excode }}</span>
                    </div>
                  </template>
                  <template v-slot:append>
                    <div class="d-sm-flex align-center mt-3">
                      <v-chip color="primary" size="small" variant="tonal" v-if="method.default"> Default </v-chip>
                      <v-chip color="secondary" size="small" variant="tonal" v-else> make default </v-chip>
                      <v-divider inset vertical class="mx-4" style="height: 20px"></v-divider>
                      <v-btn size="small" rounded="md" variant="flat" color="primary">Edit</v-btn>
                    </div>
                  </template>
                </v-list-item>
                <v-divider v-if="method.divider"></v-divider>
              </template>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>

    <v-col cols="12">
      <v-card variant="flat" rounded="lg" class="overflow-hidden">
        <v-card variant="outlined" rounded="lg" class="overflow-hidden">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Billing History</h5>
          </div>

          <v-divider></v-divider>

          <v-table class="text-no-wrap bordered-table invoice-table" hover>
            <thead class="bg-containerBg">
              <tr>
                <th class="text-start text-uppercase text-caption font-weight-bold">Order No.</th>
                <th class="text-start text-uppercase text-caption font-weight-bold">Date</th>
                <th class="text-start text-uppercase text-caption font-weight-bold">Price</th>
                <th class="text-start text-uppercase text-caption font-weight-bold">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="history in billhistory" :key="history.orderno">
                <td>{{ history.orderno }}</td>
                <td>{{ history.date }}</td>
                <td>${{ history.price }}</td>
                <td>
                  <v-chip color="warning" size="small" v-if="history.wait">Awaiting</v-chip>
                  <v-chip color="success" size="small" v-else>Paid</v-chip>
                </td>
              </tr>
            </tbody>
          </v-table>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
