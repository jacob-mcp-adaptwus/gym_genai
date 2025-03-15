<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const textlname = ref('Schorl');
const textfname = ref('Delaney');
const textemail = ref('demo@company.com');
const textphone = ref('000-00-00000');
const textcompany = ref('company.ltd');
const textsite = ref('www.company.com');
</script>

<template>
  <div>
    <div class="d-flex flex-row">
      <img src="@/assets/images/users/avatar-1.png" class="rounded-md" width="80" alt="user-img" />
      <div class="ms-4 d-flex align-center text-subtitle-2 text-medium-emphasis font-weight-medium">
        <SvgSprite name="custom-info-circle-outline" class="me-2" style="width: 16px; height: 16px" /> Image size Limit should be 125kb Max.
      </div>
    </div>
    <v-row class="mt-6">
      <v-col cols="12" md="6">
        <v-label class="mb-2">First name</v-label>
        <v-text-field
          type="text"
          single-line
          color="primary"
          v-model="textfname"
          density="comfortable"
          placeholder="Enter First Name"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Last name</v-label>
        <v-text-field
          type="text"
          single-line
          color="primary"
          v-model="textlname"
          density="comfortable"
          placeholder="Enter Last Name"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Email Address</v-label>
        <v-text-field
          type="email"
          single-line
          color="primary"
          v-model="textemail"
          density="comfortable"
          placeholder="Enter Email Address"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Phone Number</v-label>
        <v-text-field
          type="text"
          color="primary"
          single-line
          density="comfortable"
          v-model="textphone"
          placeholder="Enter Phone Number"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Company name</v-label>
        <v-text-field
          type="text"
          color="primary"
          density="comfortable"
          single-line
          v-model="textcompany"
          placeholder="Enter Company Name"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
      <v-col cols="12" md="6">
        <v-label class="mb-2">Site Information</v-label>
        <v-text-field
          type="url"
          color="primary"
          density="comfortable"
          v-model="textsite"
          placeholder="Enter Site Information"
          variant="outlined"
          hide-details
        >
        </v-text-field>
      </v-col>
    </v-row>
  </div>
</template>
