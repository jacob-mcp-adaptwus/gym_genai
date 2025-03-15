<script setup lang="ts">
import { ref } from 'vue';
import user1 from '@/assets/images/users/avatar-1.png';
const textName = ref('John Doe');
const textEmail = ref('name@example.com');
const textCompany = ref('Materially Inc.');
const textCountry = ref('USA');
const textPhone = ref('4578-420-410 ');
const textBirthday = ref('31/01/2001');
</script>

<template>
  <v-row>
    <v-col cols="12" md="4">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-6">
            <h5 class="text-subtitle-1 mb-0">Profile Picture</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text class="text-center">
            <img :src="user1" width="100" class="rounded-md" alt="profile" />
            <p class="text-subtitle-2 text-disabled font-weight-medium my-4">Upload/Change Your Profile Image</p>
            <v-btn color="primary" rounded="md" variant="flat" size="small">Upload Avatar</v-btn>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
    <v-col cols="12" md="8">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="px-5 py-6">
            <h5 class="text-subtitle-1 mb-0">Edit Account Details</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col cols="12">
                <v-label class="mb-2">Name</v-label>
                <v-text-field
                  type="text"
                  v-model="textName"
                  placeholder="Enter Name"
                  single-line
                  density="comfortable"
                  hint="Helper Text"
                  color="primary"
                  variant="outlined"
                  persistent-hint
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-label class="mb-2">Email Address</v-label>
                <v-text-field
                  type="email"
                  v-model="textEmail"
                  single-line
                  density="comfortable"
                  placeholder="Enter your email"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Company</v-label>
                <v-text-field
                  type="text"
                  v-model="textCompany"
                  single-line
                  density="comfortable"
                  placeholder="Enter company name"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Country</v-label>
                <v-text-field
                  type="text"
                  v-model="textCountry"
                  single-line
                  density="comfortable"
                  placeholder="Enter Country"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Phone Number</v-label>
                <v-text-field
                  type="text"
                  v-model="textPhone"
                  single-line
                  density="comfortable"
                  placeholder="Enter phone number"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-label class="mb-2">Birthday</v-label>
                <v-text-field
                  type="text"
                  v-model="textBirthday"
                  single-line
                  density="comfortable"
                  placeholder="Enter birthday date"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
            </v-row>
            <v-btn color="primary" rounded="md" variant="flat" class="mt-5">Change Details</v-btn>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
