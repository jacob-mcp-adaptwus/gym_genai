<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// theme breadcrumb
const page = ref({ title: 'Create Invoice' });
const breadcrumbs = ref([
  {
    title: 'Customer',
    disabled: false,
    href: '#'
  },
  {
    title: 'Create Invoice',
    disabled: true,
    href: '#'
  }
]);

const textinvoice = ref('');
const textcustomer = ref('');
const textcustomermail = ref('');
const textcustomerno = ref('');
const textcustomeradd = ref('');
const textdate = ref('23/09/2022');
const textterms = ref('I acknowledge terms and conditions.');

const status = ref(['Pending', 'Refund', 'Paid']);
const textstatus = ref<string>('Pending');

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
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <UiParentCard title="Create Invoice">
        <v-row>
          <v-col cols="12" md="4">
            <v-label class="text-subtitle-1 text-lightText mb-2">Invoice Number<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textinvoice"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="Invoice #"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-divider class="my-6"></v-divider>
        <v-row>
          <v-col cols="12" md="4">
            <v-label class="text-subtitle-1 text-lightText mb-2">Customer Name<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textcustomer"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="Alex Z."
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-label class="text-subtitle-1 text-lightText mb-2">Customer Email<span class="ms-1">*</span></v-label>
            <v-text-field
              type="email"
              color="primary"
              v-model="textcustomermail"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="alex@company.com"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-label class="text-subtitle-1 text-lightText mb-2">Customer Contact Numer<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textcustomerno"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="+00 0000 0000"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-label class="text-subtitle-1 text-lightText mb-2">Customer Address<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textcustomeradd"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="Enter Address"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-divider class="my-6"></v-divider>
        <v-row>
          <v-col cols="12" md="6">
            <v-label class="text-subtitle-1 text-lightText mb-2">Invoice Date<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textdate"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="Enter Address"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-label class="text-subtitle-1 text-lightText mb-2">Status<span class="ms-1">*</span></v-label>
            <v-select
              color="primary"
              :items="status"
              density="comfortable"
              role="link"
              variant="outlined"
              v-model="textstatus"
              hide-details
            >
            </v-select>
          </v-col>
        </v-row>
        <v-divider class="mt-6"></v-divider>

        <v-table class="text-no-wrap bordered-table" hover>
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
                <v-btn color="error" variant="text" aria-label="trash" icon rounded="md">
                  <SvgSprite name="custom-trash" style="width: 18px; height: 18px" />
                </v-btn>
              </td>
            </tr>
          </tbody>
        </v-table>
        <v-divider class="my-6"></v-divider>
        <v-btn color="primary" variant="text">+ Add Item</v-btn>
        <v-divider class="my-6"></v-divider>
        <v-sheet class="bg-containerBg pa-6" rounded="lg">
          <v-row class="justify-end">
            <v-col cols="6" sm="3" md="2" class="text-end">
              <h5 class="py-2 text-subtitle-1">Sub Total :</h5>
              <h5 class="py-2 text-subtitle-1 text-no-wrap">Taxes (10%) :</h5>
              <h5 class="py-2 text-subtitle-1 text-no-wrap">Discount (5%) :</h5>
              <h5 class="py-2 text-subtitle-1 text-primary mt-7">Total</h5>
            </v-col>
            <v-col cols="6" sm="3" md="2" class="text-end">
              <h5 class="py-2 text-subtitle-1 text-disabled">$2,650.00</h5>
              <h5 class="py-2 text-subtitle-1 text-disabled">$265.00</h5>
              <h5 class="py-2 text-subtitle-1 text-disabled">$145.75</h5>
              <h5 class="py-2 text-subtitle-1 text-primary mt-7">$2,769.25</h5>
            </v-col>
          </v-row>
        </v-sheet>
        <v-divider class="my-6"></v-divider>
        <v-row>
          <v-col cols="12">
            <v-label class="text-subtitle-1 text-lightText mb-2">Terms and Condition:<span class="ms-1">*</span></v-label>
            <v-text-field
              type="text"
              color="primary"
              v-model="textterms"
              hide-details
              variant="outlined"
              density="comfortable"
              persistent-placeholder
              placeholder="Alex Z."
            ></v-text-field>
          </v-col>
        </v-row>
        <v-divider class="my-6"></v-divider>
        <div class="text-end">
          <v-btn color="primary" rounded="md" variant="flat">Add Invoice</v-btn>
        </div>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
