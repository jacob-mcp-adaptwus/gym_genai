<script setup lang="ts">
import { ref } from 'vue';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// theme breadcrumb
const page = ref({ title: 'Layouts' });
const breadcrumbs = ref([
  {
    title: 'Forms',
    disabled: false,
    href: '#'
  },
  {
    title: 'Layouts',
    disabled: true,
    href: '#'
  }
]);

const checkbox1 = ref(true);
const checkbox2 = ref(false);
const checkbox3 = ref(false);
const checkbox4 = ref(true);
const checkbox5 = ref(false);
const checkbox6 = ref(false);
const checkbox7 = ref(true);
const checkbox8 = ref(false);
const checkbox9 = ref(false);
const checkbox10 = ref(true);
const checkbox11 = ref(false);
const checkbox12 = ref(false);
</script>

// ===============================|| Ui Layouts ||=============================== //
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" lg="6">
      <UiParentCard title="Simple Form Layout">
        <v-label class="mb-1">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>
        <v-label class="mb-1 mt-5">Email</v-label>
        <v-text-field
          hint="Please enter your Email"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter email"
          density="comfortable"
          type="email"
          color="primary"
        ></v-text-field>
        <v-label class="mb-1 mt-5">Password</v-label>
        <v-text-field
          persistent-hint
          variant="outlined"
          hide-details
          type="password"
          persistent-placeholder
          placeholder="Enter password"
          density="comfortable"
          color="primary"
        ></v-text-field>
        <v-label class="mb-1 mt-5">Language</v-label>
        <div>
          <v-checkbox density="compact" v-model="checkbox1" hide-details color="primary" label="English"></v-checkbox>
          <v-checkbox density="compact" v-model="checkbox2" hide-details color="primary" label="French"></v-checkbox>
          <v-checkbox density="compact" v-model="checkbox3" hide-details color="primary" label="Dutch"></v-checkbox>
        </div>
      </UiParentCard>
    </v-col>
    <v-col cols="12" lg="6">
      <UiParentCard title="Horizontal Form Layout">
        <h5 class="mb-8 text-h5">A. Personal Info:</h5>
        <v-row class="align-center">
          <v-col cols="12" lg="4" sm="3" class="py-sm-0 pt-0 pb-0">
            <v-label class="mb-0 mb-sm-5">Name</v-label>
          </v-col>
          <v-col cols="12" lg="8" sm="9" class="py-sm-3 pt-1">
            <v-text-field
              hint="Please enter your full name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter full name"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row class="align-center mt-2">
          <v-col cols="12" lg="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="mb-0 mb-sm-5">Email</v-label>
          </v-col>
          <v-col cols="12" lg="8" sm="9" class="py-sm-3 pt-1">
            <v-text-field
              hint="Please enter your Email"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter email"
              density="comfortable"
              type="email"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <h5 class="mt-7 mb-8 text-h5">B. Educational Info:</h5>
        <v-row class="align-center">
          <v-col cols="12" lg="4" sm="3" class="py-sm-0 pt-0 pb-0">
            <v-label class="mb-0 mb-sm-5">Degree Name</v-label>
          </v-col>
          <v-col cols="12" lg="8" sm="9" class="py-sm-3 pt-1">
            <v-text-field
              hint="Please enter your Degree name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter Degree name"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row class="align-center mt-2">
          <v-col cols="12" lg="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="mb-0 mb-sm-5">Passing Year</v-label>
          </v-col>
          <v-col cols="12" lg="8" sm="9" class="py-sm-3 pt-1">
            <v-text-field
              hint="Please enter Passing Year"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter Passing Year"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row class="mt-2">
          <v-col cols="12" lg="4" sm="3" class="py-sm-5 pt-5 pb-0">
            <v-label>Language</v-label>
          </v-col>
          <v-col cols="12" lg="8" sm="9" class="py-sm-3 pt-1">
            <div class="d-flex ga-4">
              <v-checkbox
                density="compact"
                v-model="checkbox4"
                hide-details
                color="primary"
                label="English"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox
                density="compact"
                v-model="checkbox5"
                hide-details
                color="primary"
                label="French"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox density="compact" v-model="checkbox6" hide-details color="primary" label="Dutch" class="flex-grow-0"></v-checkbox>
            </div>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
    <v-col cols="12" lg="6">
      <UiParentCard title="Control Divider">
        <v-label class="mb-1">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>
        <v-divider class="my-4"></v-divider>
        <v-label class="mb-1">Email</v-label>
        <v-text-field
          hint="Please enter your Email"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter email"
          density="comfortable"
          type="email"
          color="primary"
        ></v-text-field>
        <v-divider class="my-4"></v-divider>
        <v-label class="mb-1">Password</v-label>
        <v-text-field
          persistent-hint
          variant="outlined"
          hide-details
          type="password"
          persistent-placeholder
          placeholder="Enter password"
          density="comfortable"
          color="primary"
        ></v-text-field>
        <v-divider class="my-4"></v-divider>
        <v-label class="mb-2">Language</v-label>
        <div>
          <v-checkbox density="compact" v-model="checkbox7" hide-details color="primary" label="English"></v-checkbox>
          <v-checkbox density="compact" v-model="checkbox8" hide-details color="primary" label="French"></v-checkbox>
          <div class="d-flex">
            <v-checkbox density="compact" v-model="checkbox9" hide-details color="primary" label="Dutch"></v-checkbox>
          </div>
        </div>
      </UiParentCard>
    </v-col>
    <v-col cols="12" lg="6">
      <UiParentCard title="Input Label Alignment">
        <h5 class="mb-6 text-h5">A. Personal Info:</h5>
        <v-row class="d-flex align-center">
          <v-col cols="12" md="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Name</v-label>
          </v-col>
          <v-col cols="12" md="6" sm="7">
            <v-text-field
              hint="Please enter your full name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter full name"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row class="d-flex align-center mt-2">
          <v-col cols="12" md="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Email</v-label>
          </v-col>
          <v-col cols="12" md="6" sm="7">
            <v-text-field
              hint="Please enter your Email"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter email"
              density="comfortable"
              type="email"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-divider class="mt-6"></v-divider>
        <h4 class="mt-6 mb-6 text-h5">B. Educational Info:</h4>
        <v-row class="d-flex align-center">
          <v-col cols="12" md="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Degree Name</v-label>
          </v-col>
          <v-col cols="12" md="6" sm="7">
            <v-text-field
              hint="Please enter your Degree name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter Degree name"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row class="d-flex align-center mt-2">
          <v-col cols="12" md="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Passing Year</v-label>
          </v-col>
          <v-col cols="12" md="6" sm="7">
            <v-text-field
              hint="Please enter Passing Year"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter Passing Year"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row class="d-flex align-center">
          <v-col cols="12" md="4" sm="3" class="py-sm-0 pt-5 pb-0">
            <v-label class="d-flex justify-start justify-sm-end">Language</v-label>
          </v-col>
          <v-col cols="12" md="8" sm="9">
            <div class="d-flex ga-4">
              <v-checkbox
                density="compact"
                v-model="checkbox10"
                hide-details
                color="primary"
                label="English"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox
                density="compact"
                v-model="checkbox11"
                hide-details
                color="primary"
                label="French"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox
                density="compact"
                v-model="checkbox12"
                hide-details
                color="primary"
                label="Dutch"
                class="flex-grow-0"
              ></v-checkbox>
            </div>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
