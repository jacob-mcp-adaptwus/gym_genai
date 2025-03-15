<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

// theme breadcrumb
const page = ref({ title: 'Sticky Bar' });
const breadcrumbs = ref([
  {
    title: 'Layouts',
    disabled: false,
    href: '#'
  },
  {
    title: 'Sticky Bar',
    disabled: true,
    href: '#'
  }
]);

const checkbox1 = ref(true);
const checkbox2 = ref(false);
const checkbox3 = ref(false);
const checkbox4 = ref(false);
const checkbox5 = ref(false);
const checkbox6 = ref(false);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <v-card variant="outlined" elevation="0" class="bg-surface">
        <v-toolbar
          flat
          class="px-2 position-sticky stickyHeader bg-containerBg"
          rounded="md"
          color="inherit"
          density="comfortable"
          style="border-bottom-left-radius: 0 !important; border-bottom-right-radius: 0 !important"
        >
          <v-toolbar-title class="text-h5">Sticky Action Bar:</v-toolbar-title>
          <template v-slot:append>
            <v-btn variant="text" color="error" class="me-3" size="small" rounded="md">Cancel</v-btn>
            <v-btn variant="flat" color="primary" size="small" rounded="md">Submit</v-btn>
          </template>
        </v-toolbar>
        <v-divider></v-divider>
        <v-card-text>
          <div class="pb-0 pb-sm-6">
            <v-row class="pb-4 pb-sm-0">
              <v-col cols="3" lg="4">
                <div class="d-flex align-center justify-end">
                  <v-btn icon color="secondary" aria-label="profile" rounded="md" variant="flat">
                    <SvgSprite name="custom-profile-outline" style="width: 24px; height: 24px" />
                  </v-btn>
                </div>
              </v-col>
              <v-col cols="9" lg="6" class="ps-0">
                <h3 class="text-h3 mb-0 mt-n1">Personal Information</h3>
                <span class="text-caption">Sticky Action Bar Lorem Ipsum is simply</span>
              </v-col>
            </v-row>
          </div>
          <v-divider></v-divider>
          <v-row class="pt-0 pt-sm-7 mb-4 mb-md-0">
            <v-col sm="3" lg="4"></v-col>
            <v-col cols="12" lg="6" sm="9">
              <h5 class="text-h5 mb-2">A. Personal Info:</h5>
            </v-col>
          </v-row>

          <v-row class="d-flex align-center">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Name :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
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
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Email :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
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
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Password :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
              <v-text-field
                hint="Please enter your Password"
                persistent-hint
                variant="outlined"
                persistent-placeholder
                placeholder="Enter password"
                density="comfortable"
                type="password"
                color="primary"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-divider class="mt-9"></v-divider>
          <v-row class="pt-0 pt-sm-7 mb-4 mb-sm-0">
            <v-col sm="3" lg="4"></v-col>
            <v-col lg="8" cols="12" sm="9">
              <h5 class="text-h5 mb-2">B. Educational Info:</h5>
            </v-col>
          </v-row>
          <v-row class="d-flex align-center">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Degree Name :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
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
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Passing Year :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
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
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">College Name :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
              <v-text-field
                hint="Please enter College name"
                persistent-hint
                variant="outlined"
                persistent-placeholder
                placeholder="Enter College name"
                density="comfortable"
                color="primary"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end mb-0 mb-sm-5">Work Experience :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
              <v-text-field
                hint="Please enter Work Experience"
                persistent-hint
                variant="outlined"
                persistent-placeholder
                placeholder="Enter Work Experience"
                density="comfortable"
                color="primary"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end">Language :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
              <div class="d-flex ga-4">
                <v-checkbox
                  density="compact"
                  v-model="checkbox1"
                  hide-details
                  color="primary"
                  label="English"
                  class="flex-grow-0"
                ></v-checkbox>
                <v-checkbox
                  density="compact"
                  v-model="checkbox2"
                  hide-details
                  color="primary"
                  label="French"
                  class="flex-grow-0"
                ></v-checkbox>
                <v-checkbox
                  density="compact"
                  v-model="checkbox3"
                  hide-details
                  color="primary"
                  label="Dutch"
                  class="flex-grow-0"
                ></v-checkbox>
              </div>
            </v-col>
          </v-row>

          <v-row class="d-flex align-center mt-sm-2 mt-5">
            <v-col cols="12" sm="3" lg="4" class="py-0">
              <v-label class="d-flex justify-start justify-sm-end">Hobby :</v-label>
            </v-col>
            <v-col cols="12" sm="9" lg="6">
              <div class="d-flex ga-2 flex-wrap">
                <v-checkbox
                  density="compact"
                  v-model="checkbox4"
                  hide-details
                  color="primary"
                  label="Reading"
                  class="flex-grow-0"
                ></v-checkbox>
                <v-checkbox
                  density="compact"
                  v-model="checkbox5"
                  hide-details
                  color="primary"
                  label="Dancing"
                  class="flex-grow-0"
                ></v-checkbox>
                <v-checkbox
                  density="compact"
                  v-model="checkbox6"
                  hide-details
                  color="primary"
                  label="Swimming"
                  class="flex-grow-0"
                ></v-checkbox>
              </div>
            </v-col>
          </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-row>
            <v-col cols="12" sm="3" lg="4" class="d-none d-sm-block"></v-col>
            <v-col cols="12" sm="9" lg="8" class="text-sm-start text-center">
              <v-btn variant="text" color="error" rounded="md">Cancel</v-btn>
              <v-btn variant="flat" color="primary" class="me-2" rounded="md">Submit</v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.stickyHeader {
  top: 60px;
  z-index: 2;
}
</style>
