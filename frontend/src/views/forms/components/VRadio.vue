<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Radio' });
const subContent = ref({ content: 'Radio buttons allow the user to select one option from a set.' });
const path = ref({ filepath: 'src/views/forms/components/radio' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/radio-buttons/' });

const radioGroup = ref('1');
const radioGroup3 = ref('1');
const radioColumn = ref('1');
const radioInline = ref('1');
const radioColors = ref('success');

// radio color data
const radioColor = ref(['primary', 'secondary', 'success', 'warning', 'info', 'error']);
</script>

// ===============================|| Ui Radio ||=============================== //
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic Radio -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic Radio">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row radio-group-space">
              <v-radio-group inline hide-details v-model="radioGroup">
                <v-radio color="primary" value="1" label="Female"></v-radio>
                <v-radio color="primary" value="2" label="Male"></v-radio>
                <v-radio disabled color="primary" value="3" label="Other"></v-radio>
              </v-radio-group>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Radio with Label -->
        <v-col cols="12" md="6">
          <UiParentCard title="Density">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row radio-group-space">
              <v-radio-group hide-details v-model="radioGroup3" inline>
                <v-radio label="Compact" color="primary" value="1" density="compact"></v-radio>
                <v-radio label="Comfortable" color="primary" value="2" density="comfortable"></v-radio>
                <v-radio label="Default" color="primary" value="3"></v-radio>
              </v-radio-group>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Direction -->
        <v-col cols="12" md="6">
          <UiParentCard title="Direction">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row radio-group-space">
              <v-radio-group v-model="radioColumn" column>
                <v-radio label="Option 1" color="primary" value="1"></v-radio>
                <v-radio label="Option 2" color="primary" value="2"></v-radio>
              </v-radio-group>
              <v-radio-group v-model="radioInline" inline>
                <v-radio label="Option 1" color="primary" value="1"></v-radio>
                <v-radio label="Option 2" color="primary" value="2"></v-radio>
              </v-radio-group>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With Colors -->
        <v-col cols="12" md="6">
          <UiParentCard title="With Colors">
            <div class="d-flex ga-4 align-center flex-column flex-sm-row radio-group-space">
              <v-radio-group v-model="radioColors" inline>
                <v-radio v-for="btn in radioColor" :key="btn" :color="btn" :label="btn" :value="btn" hide-details></v-radio>
              </v-radio-group>
            </div>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.radio-group-space {
  .v-selection-control-group {
    gap: 10px;
  }
}
</style>
