<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';

const invoices = ref([
  {
    name: 'Logo Design',
    quantity: 6,
    amount: 200
  },
  {
    name: 'Landing Page',
    quantity: 7,
    amount: 100
  },
  {
    name: 'Admin Template',
    quantity: 5,
    amount: 150
  }
]);
</script>

<template>
  <UiChildCard title="Customer">
    <template v-slot:action>
      <h5 class="text-subtitle-1">Placed on 12.07.2018 10:00</h5>
    </template>

    <div class="d-flex align-center flex-column flex-sm-row text-medium-emphasis ga-4">
      <div class="d-flex align-center">
        <SvgSprite name="custom-calendar-outline" class="text-lightText" style="width: 16px; height: 16px" />
        <span class="text-subtitle-1 font-weight-medium ms-2">Sophia Hale</span>
      </div>
      <div class="d-flex align-center">
        <SvgSprite name="custom-mobile-outline" class="text-lightText" style="width: 16px; height: 16px" />
        <span class="text-subtitle-1 font-weight-medium ms-2">070 123 4567</span>
      </div>
      <div class="d-flex align-center">
        <SvgSprite name="custom-mail-outline" class="text-lightText" style="width: 16px; height: 16px" />
        <span class="text-subtitle-1 font-weight-medium ms-2">example@mail.com</span>
      </div>
    </div>
    <v-divider class="my-4"></v-divider>
    <v-row>
      <v-col cols="12" sm="4">
        <h4 class="mb-2 text-h4">Payment method</h4>
        <span class="text-subtitle-2 text-medium-emphasis font-weight-medium">Credit Card</span>
        <div class="mt-3 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Transaction ID :</span>
          <span class="text-medium-emphasis">000001-TXT</span>
        </div>
        <div class="text-subtitle-1">
          <span class="font-weight-semibold me-2">Amount :</span>
          <span class="text-medium-emphasis">$2500</span>
        </div>
      </v-col>
      <v-col cols="12" sm="4">
        <h4 class="mb-2 text-h4">Shipping method</h4>
        <span class="text-subtitle-2 text-medium-emphasis font-weight-medium">Carrier</span>
        <div class="mt-3 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Tracking Code :</span>
          <span class="text-medium-emphasis">FX-012345-6</span>
        </div>
        <div class="text-subtitle-1">
          <span class="font-weight-semibold me-2">Date :</span>
          <span class="text-medium-emphasis">12.15.2018</span>
        </div>
      </v-col>
      <v-col cols="12" sm="4">
        <div class="mt-3 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Fulfillment status :</span>
          <span class="text-subtitle-1 text-medium-emphasis">Delivered</span>
        </div>
        <div class="text-subtitle-1">
          <span class="font-weight-semibold me-2">Payment status :</span>
          <v-chip color="success" variant="tonal" size="small">Paid</v-chip>
        </div>
      </v-col>
    </v-row>
    <v-divider class="my-4"></v-divider>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <h4 class="mb-2 text-h4">Billing address</h4>
        <div class="mt-3 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">First name :</span>
          <span class="text-medium-emphasis">Joseph</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">Last name :</span>
          <span class="text-medium-emphasis">William</span>
        </div>
        <div class="mt-5 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Address :</span>
          <span class="text-medium-emphasis">4898 Joanne Lane street</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">City :</span>
          <span class="text-medium-emphasis">Boston</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">Country :</span>
          <span class="text-medium-emphasis">United States</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">State :</span>
          <span class="text-medium-emphasis">Massachusetts</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">Zip code :</span>
          <span class="text-medium-emphasis">02110</span>
        </div>
        <div class="mt-5 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Phone :</span>
          <span class="text-medium-emphasis">+1 (070) 123-4567</span>
        </div>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <h4 class="mb-2 text-h4">Shipping address</h4>
        <div class="mt-3 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">First name :</span>
          <span class="text-medium-emphasis">Sara</span>
        </div>
        <div class="text-subtitle-1">
          <span class="font-weight-semibold me-2">Last name :</span>
          <span class="text-medium-emphasis">Soudan</span>
        </div>
        <div class="mt-5 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Address :</span>
          <span class="text-medium-emphasis">4898 Joanne Lane street</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">City :</span>
          <span class="text-medium-emphasis">Boston</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">Country :</span>
          <span class="text-medium-emphasis">United States</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">State :</span>
          <span class="text-medium-emphasis">Massachusetts</span>
        </div>
        <div class="text-subtitle-1 mb-2">
          <span class="font-weight-semibold me-2">Zip code :</span>
          <span class="text-medium-emphasis">02110</span>
        </div>
        <div class="mt-5 mb-2 text-subtitle-1">
          <span class="font-weight-semibold me-2">Phone :</span>
          <span class="text-medium-emphasis">+1 (070) 123-4567</span>
        </div>
      </v-col>
    </v-row>
  </UiChildCard>
  <!-- shopping list -->
  <v-card elevation="0" class="mt-6" rounded="lg">
    <v-card variant="outlined">
      <v-card-item class="py-3">
        <v-card-title class="text-h5">Products</v-card-title>
      </v-card-item>
      <v-divider></v-divider>
      <v-table class="text-no-wrap bordered-table rounded-0">
        <thead class="bg-containerBg">
          <tr>
            <th class="text-start text-uppercase text-caption font-weight-bold">Description</th>
            <th class="text-start text-uppercase text-caption font-weight-bold">Quantity</th>
            <th class="text-start text-uppercase text-caption font-weight-bold">Amount</th>
            <th class="text-start text-uppercase text-caption font-weight-bold">Total</th>
            <th class="text-start"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="invoice in invoices" :key="invoice.name">
            <td class="py-3">
              <h5 class="text-subtitle-1">{{ invoice.name }}</h5>
              <p class="mt-1">lorem ipsum dolor sit amat, connecter adieu siccing eliot</p>
            </td>
            <td class="py-3">{{ invoice.quantity }}</td>
            <td class="py-3">${{ invoice.amount }}</td>
            <td class="py-3">${{ invoice.amount * invoice.quantity }}</td>
            <td class="py-3">
              <v-btn color="primary" aria-label="trash" variant="text" icon rounded="md">
                <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>
      <v-divider></v-divider>
      <v-card-text>
        <v-sheet class="bg-containerBg pa-6" rounded="lg">
          <v-row class="justify-end">
            <v-col cols="6" sm="3" lg="2" class="text-end">
              <h5 class="py-2 text-subtitle-1">Sub Total :</h5>
              <h5 class="py-2 text-subtitle-1">Taxes (10%) :</h5>
              <h5 class="py-2 text-subtitle-1 text-no-wrap">Discount (5%) :</h5>
              <h5 class="py-2 text-subtitle-1 text-primary mt-7">Total</h5>
            </v-col>
            <v-col cols="6" sm="3" lg="2" class="text-end">
              <h5 class="py-2 text-subtitle-1 text-disabled">$2,650.00</h5>
              <h5 class="py-2 text-subtitle-1 text-disabled">$265.00</h5>
              <h5 class="py-2 text-subtitle-1 text-disabled">$145.75</h5>
              <h5 class="py-2 text-subtitle-1 text-primary mt-7">$2,769.25</h5>
            </v-col>
          </v-row>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-card>
</template>
