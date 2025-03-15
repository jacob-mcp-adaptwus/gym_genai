<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Switch' });
const subContent = ref({ content: 'Switches toggle the state of a single setting on or off.' });
const path = ref({ filepath: 'src/views/forms/components/switch' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/switches/' });

const model = ref(true);
</script>

// ===============================|| Ui Switch ||=============================== //
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic Switch -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic Switch">
            <div class="d-sm-flex justify-space-between">
              <v-switch color="primary" aria-label="switch" :model-value="true" hide-details></v-switch>

              <v-switch color="primary" aria-label="switch" :model-value="false" hide-details></v-switch>
              <v-switch color="primary" aria-label="switch" :model-value="true" disabled hide-details></v-switch>

              <v-switch color="primary" aria-label="switch" :model-value="false" disabled hide-details></v-switch>
              <v-switch loading="error" aria-label="loading switch" :model-value="true" hide-details></v-switch>

              <v-switch :model-value="false" aria-label="switch" loading="error" hide-details></v-switch>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With Label -->
        <v-col cols="12" md="6">
          <UiParentCard title="With Label">
            <div class="d-flex justify-space-around">
              <v-switch color="primary" aria-label="switch" :model-value="true" label="Label" hide-details></v-switch>

              <v-switch color="primary" aria-label="switch" disabled label="Disabled" :model-value="false" hide-details></v-switch>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Inset -->
        <v-col cols="12" md="6">
          <UiParentCard title="Inset">
            <v-switch
              v-model="model"
              aria-label="switch"
              hide-details
              color="primary"
              inset
              :label="`Switch: ${model.toString()}`"
            ></v-switch>
          </UiParentCard>
        </v-col>
        <!-- Inset Colors -->
        <v-col cols="12" md="6">
          <UiParentCard title="Inset Colors">
            <div class="d-flex ga-4 flex-column flex-sm-row">
              <v-switch aria-label="switch" color="primary" :model-value="true" hide-details inset></v-switch>
              <v-switch aria-label="switch" color="secondary" :model-value="true" hide-details inset></v-switch>
              <v-switch aria-label="switch" color="success" :model-value="true" hide-details inset></v-switch>
              <v-switch aria-label="switch" color="error" :model-value="true" hide-details inset></v-switch>
              <v-switch aria-label="switch" color="warning" :model-value="true" hide-details inset></v-switch>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Colors -->
        <v-col cols="12" md="6">
          <UiParentCard title="Colors">
            <div class="d-flex ga-4 flex-column flex-sm-row">
              <v-switch aria-label="switch" color="primary" :model-value="true" hide-details></v-switch>
              <v-switch aria-label="switch" color="secondary" :model-value="true" hide-details></v-switch>
              <v-switch aria-label="switch" color="success" :model-value="true" hide-details></v-switch>
              <v-switch aria-label="switch" color="error" :model-value="true" hide-details></v-switch>
              <v-switch aria-label="switch" color="warning" :model-value="true" hide-details></v-switch>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Density -->
        <v-col cols="12" md="6">
          <UiParentCard title="Density">
            <div class="d-flex ga-4 flex-column flex-sm-row">
              <v-switch aria-label="switch" color="primary" :model-value="true" density="compact" hide-details></v-switch>
              <v-switch aria-label="switch" color="primary" :model-value="true" density="comfortable" hide-details></v-switch>
              <v-switch aria-label="switch" color="primary" :model-value="true" hide-details></v-switch>
            </div>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
