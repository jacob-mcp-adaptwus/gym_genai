<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import CardHeaderFooter from '@/components/shared/CardHeaderFooter.vue';

// theme breadcrumb
const page = ref({ title: 'Action Bar' });
const breadcrumbs = ref([
  {
    title: 'Layouts',
    disabled: false,
    href: '#'
  },
  {
    title: 'Action Bar',
    disabled: true,
    href: '#'
  }
]);
</script>

<template>
  <!-- ----------------------------------------------------- -->
  <!-- Action Bar -->
  <!-- ----------------------------------------------------- -->
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <!-- Right align Action Bar -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="Simple Action Bar">
        <v-label class="mb-2">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>

        <template v-slot:footer>
          <div class="text-end w-100">
            <v-btn color="error" variant="text" rounded="md">Cancel</v-btn>
            <v-btn color="primary" variant="flat" rounded="md">Submit</v-btn>
          </div>
        </template>
      </CardHeaderFooter>
    </v-col>
    <!-- Left Align Action Bar -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="Left Align Action Bar">
        <v-label class="mb-2">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>

        <template v-slot:footer>
          <div class="text-start w-100">
            <v-btn color="error" variant="text" rounded="md">Cancel</v-btn>
            <v-btn color="primary" variant="flat" rounded="md">Submit</v-btn>
          </div>
        </template>
      </CardHeaderFooter>
    </v-col>
    <!-- Action Button with Link -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="Action Button with Link">
        <v-label class="mb-2">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>

        <template v-slot:footer>
          <div class="text-end w-100">
            <v-btn color="error" variant="text" class="me-3" rounded="md">Cancel</v-btn>
            <span class="text-caption">or</span>
            <v-btn color="primary" variant="flat" class="ms-4" rounded="md">Submit</v-btn>
          </div>
        </template>
      </CardHeaderFooter>
    </v-col>
    <!-- Horizontal Form -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="Horizontal Form">
        <v-row>
          <v-col cols="12" sm="4" class="text-sm-end pb-sm-3 pb-0">
            <v-label class="mb-sm-2 mt-sm-3">Name</v-label>
          </v-col>
          <v-col cols="12" sm="8">
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

        <template v-slot:footer>
          <div class="text-center w-100">
            <v-btn color="error" variant="text" rounded="md">Cancel</v-btn>
            <v-btn color="primary" variant="flat" rounded="md">Submit</v-btn>
          </div>
        </template>
      </CardHeaderFooter>
    </v-col>
    <!-- With side action button -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="With side action button">
        <v-label class="mb-2">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>

        <template v-slot:footer>
          <div class="d-flex align-center justify-space-between w-100">
            <v-btn color="error" aria-label="delete" variant="text" icon rounded="md">
              <SvgSprite name="custom-trash-fill" style="width: 20px; height: 20px" />
            </v-btn>
            <div>
              <v-btn color="error" variant="text" rounded="md">Cancel</v-btn>
              <v-btn color="primary" variant="flat" rounded="md">Submit</v-btn>
            </div>
          </div>
        </template>
      </CardHeaderFooter>
    </v-col>
    <!-- Top & BOttom Action Bars -->
    <v-col cols="12" md="6">
      <CardHeaderFooter title="Top & Bottom Actions Bars">
        <v-label class="mb-2">Name</v-label>
        <v-text-field
          hint="Please enter your full name"
          persistent-hint
          variant="outlined"
          persistent-placeholder
          placeholder="Enter full name"
          density="comfortable"
          color="primary"
        ></v-text-field>

        <template v-slot:footer>
          <v-btn color="error" variant="text" rounded="md">Cancel</v-btn>
          <v-btn color="primary" variant="flat" rounded="md">Submit</v-btn>
        </template>
      </CardHeaderFooter>
    </v-col>
  </v-row>
</template>
