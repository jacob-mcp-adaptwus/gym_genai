<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Checkbox' });
const subContent = ref({ content: 'Checkboxes allow the user to select one or more items from a set.' });
const path = ref({ filepath: 'src/views/forms/components/checkbox' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/checkboxes/' });

const checkbox = ref(false);
const checkbox2 = ref(true);
const checkbox3 = ref(true);
const checkbox4 = ref(false);
const checkbox5 = ref(true);
const checkbox6 = ref(true);
const checkbox7 = ref(true);
const checkbox8 = ref(true);
const checkbox9 = ref(false);
const checkbox10 = ref(true);
const checkbox11 = ref(true);
const checkbox12 = ref(false);
const checked = ref(true);
const unchecked = ref(false);
const includeFiles = ref(true);
const enabled = ref(false);

// checks color data
const checksColor = ref([
  {
    color: 'primary',
    value: true
  },
  {
    color: 'secondary',
    value: true
  },
  {
    color: 'success',
    value: true
  },
  {
    color: 'warning',
    value: true
  },
  {
    color: 'info',
    value: true
  },
  {
    color: 'error',
    value: true
  }
]);
</script>

// ===============================|| Ui Checkbox ||=============================== //
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic checkboxes -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic Checkboxes">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row">
              <v-checkbox-btn aria-label="checkbox" color="success" hide-details v-model="checkbox"></v-checkbox-btn>
              <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox2"></v-checkbox-btn>
              <v-checkbox-btn aria-label="checkbox" v-model="checkbox3" hide-details disabled></v-checkbox-btn>
              <v-checkbox-btn aria-label="checkbox" color="secondary" hide-details v-model="checkbox4" disabled></v-checkbox-btn>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With label -->
        <v-col cols="12" md="6">
          <UiParentCard title="With label">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row">
              <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checked" label="Checked"></v-checkbox-btn>
              <v-checkbox-btn
                aria-label="checkbox"
                color="primary"
                disabled
                hide-details
                v-model="unchecked"
                label="Unchecked"
              ></v-checkbox-btn>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With Colors -->
        <v-col cols="12" md="6">
          <UiParentCard title="With Colors">
            <div class="d-flex ga-4 align-center flex-wrap">
              <v-checkbox-btn
                aria-label="checkbox"
                v-for="(btn, index) in checksColor"
                :key="index"
                :color="btn.color"
                hide-details
                v-model="btn.value"
              ></v-checkbox-btn>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Density -->
        <v-col cols="12" md="6">
          <UiParentCard title="Density">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row">
              <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox5" density="compact"></v-checkbox-btn>
              <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox6" density="comfortable"></v-checkbox-btn>
              <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox7"></v-checkbox-btn>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="States">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row">
              <div>
                <h6 class="text-h6 text-center">On</h6>
                <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox8"></v-checkbox-btn>
              </div>
              <div>
                <h6 class="text-h6 text-center">Off</h6>
                <v-checkbox-btn aria-label="checkbox" color="primary" hide-details v-model="checkbox9"></v-checkbox-btn>
              </div>
              <div>
                <h6 class="text-h6 text-center">Indeterminate</h6>
                <v-checkbox-btn
                  aria-label="checkbox"
                  color="primary"
                  aria-checked="true"
                  class="justify-center"
                  hide-details
                  v-model="checkbox10"
                  indeterminate
                ></v-checkbox-btn>
              </div>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="Model as boolean">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row">
              <div>
                <v-checkbox-btn
                  aria-label="checkbox"
                  color="primary"
                  hide-details
                  v-model="checkbox11"
                  :label="`Checkbox 1: ${checkbox11.toString()}`"
                ></v-checkbox-btn>
                <v-checkbox-btn
                  aria-label="checkbox"
                  color="primary"
                  hide-details
                  v-model="checkbox12"
                  :label="`Checkbox 2: ${checkbox12.toString()}`"
                ></v-checkbox-btn>
              </div>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With Inline Textfield -->
        <v-col cols="12">
          <UiParentCard title="With Inline Textfield">
            <div class="d-flex">
              <v-checkbox-btn aria-label="checkbox" v-model="includeFiles" class="pe-2"></v-checkbox-btn>
              <v-text-field variant="outlined" single-line label="Include files" hide-details></v-text-field>
            </div>
            <div class="d-flex mt-3">
              <v-checkbox-btn aria-label="checkbox" v-model="enabled" class="pe-2"></v-checkbox-btn>
              <v-text-field
                variant="outlined"
                single-line
                :disabled="!enabled"
                hide-details
                label="I only work if you check the box"
              ></v-text-field>
            </div>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
