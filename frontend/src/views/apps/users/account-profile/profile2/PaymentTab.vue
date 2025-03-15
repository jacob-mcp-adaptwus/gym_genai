<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const textcardname = ref('Selena Litten');
const textcardnumber = ref('4012 8888 8888 1881');
const textdate = ref('10/22');
const textcode = ref('123');
const textmail = ref('demo@company.paypal.com');

const payment_choose = ref('visa');
</script>

<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-radio-group v-model="payment_choose" inline>
          <v-radio color="primary" label="Visa Credit/Debit Card" value="visa"></v-radio>
          <v-radio color="primary" label="Paypal" value="paypal"></v-radio>
        </v-radio-group>
      </v-col>
    </v-row>
    <v-row v-if="payment_choose === 'visa'">
      <v-col cols="12" md="6">
        <v-label class="mb-2">Card name</v-label>
        <v-text-field
          type="text"
          color="primary"
          single-line
          density="comfortable"
          v-model="textcardname"
          placeholder="Name on Card"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Card number</v-label>
        <v-text-field
          type="text"
          color="primary"
          single-line
          density="comfortable"
          v-model="textcardnumber"
          placeholder="Enter Card Number"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Expiry Date</v-label>
        <v-text-field
          type="text"
          color="primary"
          single-line
          density="comfortable"
          v-model="textdate"
          placeholder="Enter Expiry Date"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">CCV Code</v-label>
        <v-text-field
          type="text"
          color="primary"
          density="comfortable"
          single-line
          v-model="textcode"
          placeholder="Enter Code"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12">
        <div class="d-flex align-center ga-4">
          <SvgSprite name="custom-lock-outline" class="text-primary" style="width: 40px; height: 40px" />
          <div class="mt-1">
            <h5 class="text-subtitle-1 mb-0">Secure Checkout</h5>
            <span class="text-subtitle-2 text-disabled font-weight-medium">Secure by Google.</span>
          </div>
        </div>
        <v-btn color="primary" variant="outlined" size="large" rounded="md" class="mt-6 text-subtitle-1">
          <template v-slot:prepend>
            <SvgSprite name="custom-credit-outline" class="text-primary" style="width: 16px; height: 16px" />
          </template>
          Add New Card
        </v-btn>
      </v-col>
    </v-row>
    <div v-else>
      <v-row>
        <v-col cols="12">
          <v-label class="mb-2">Paypal mail</v-label>
          <v-text-field
            variant="outlined"
            single-line
            density="comfortable"
            color="primary"
            placeholder="Enter Mail"
            v-model="textmail"
            hide-details
          ></v-text-field>
        </v-col>
      </v-row>
    </div>
  </div>
</template>
