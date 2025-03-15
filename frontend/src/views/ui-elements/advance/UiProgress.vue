<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Progress' });
const subContent = ref({
  content: 'Progress indicators commonly known as spinners, express an unspecified wait time or display the length of a process.'
});
const path = ref({ filepath: 'src/views/ui-elements/advance/progress' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/progress-circular/' });

// progress data
const pcolors = ref([
  {
    color: '#fe0000',
    value: 25
  },
  {
    color: 'secondary',
    value: 50
  },
  {
    color: 'success',
    value: 75
  },
  {
    color: 'warning',
    value: 100
  },
  {
    color: 'info',
    value: 30
  },
  {
    color: 'error',
    value: 45
  }
]);

const pvalue = ref([
  {
    value: 25
  },
  {
    value: 50
  },
  {
    value: 75
  },
  {
    value: 100
  }
]);

const psize = ref([
  {
    color: 'primary',
    size: 25
  },
  {
    color: 'secondary',
    size: 50
  },
  {
    color: 'error',
    size: 55
  },
  {
    color: 'warning',
    size: 65
  },
  {
    color: 'success',
    size: 75
  }
]);

const pheight = ref([
  {
    color: 'primary',
    size: 6,
    value: 80
  },
  {
    color: 'secondary',
    size: 6,
    value: 75
  },
  {
    color: 'success',
    size: 8,
    value: 99
  },
  {
    color: 'warning',
    size: 10,
    value: 35
  },
  {
    color: 'info',
    size: 12,
    value: 60
  },
  {
    color: 'error',
    size: 2,
    value: 15
  }
]);

// linear data

const p1 = ref(29);
const withLabel = ref(100);
const withLabel1 = ref(60);
const withLabel2 = ref(20);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Circular Indeterminate -->
            <v-col cols="12">
              <UiParentCard title="Circular Indeterminate">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 justify-center">
                  <div v-for="progress in pcolors" :key="progress.color">
                    <v-progress-circular
                      aria-label="circular progressbar"
                      indeterminate
                      size="40"
                      :model-value="progress.value"
                      :color="progress.color"
                    ></v-progress-circular>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Circular -->
            <v-col cols="12">
              <UiParentCard title="Circular Indeterminate with path">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 justify-center">
                  <div v-for="progress in pcolors" :key="progress.color">
                    <v-progress-circular
                      aria-label="circular progressbar"
                      indeterminate
                      size="40"
                      :model-value="progress.value"
                      bg-opacity="1"
                      bg-color="borderLight"
                      :color="progress.color"
                    >
                    </v-progress-circular>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Circular Determinate -->
            <v-col cols="12">
              <UiParentCard title="Circular Determinate">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 justify-center">
                  <div v-for="progress in pvalue" :key="progress.value">
                    <v-progress-circular aria-label="circular progressbar" size="40" :model-value="progress.value" color="primary">
                    </v-progress-circular>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Circular Determinate With Path -->
            <v-col cols="12">
              <UiParentCard title="Circular Determinate With Path">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 justify-center">
                  <div v-for="progress in pvalue" :key="progress.value">
                    <v-progress-circular
                      aria-label="circular progressbar"
                      size="40"
                      :model-value="progress.value"
                      color="primary"
                      bg-opacity="1"
                      bg-color="borderLight"
                    >
                    </v-progress-circular>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Circular Size -->
            <v-col cols="12">
              <UiParentCard title="Circular Size">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 justify-center">
                  <div v-for="progress in psize" :key="progress.color">
                    <v-progress-circular
                      aria-label="circular progressbar"
                      :size="progress.size"
                      indeterminate
                      :color="progress.color"
                      bg-opacity="1"
                      bg-color="borderLight"
                    >
                    </v-progress-circular>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Linear striped -->
            <v-col cols="12">
              <UiParentCard title="Striped">
                <div class="d-flex flex-column ga-4">
                  <div v-for="progress in pcolors" :key="progress.color">
                    <v-progress-linear
                      aria-label="progressbar"
                      rounded
                      :color="progress.color"
                      :model-value="progress.value"
                      striped
                      height="10"
                    ></v-progress-linear>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Linear Intermidiate -->
            <v-col cols="12">
              <UiParentCard title="Linear Intermidiate">
                <v-progress-linear aria-label="progressbar" color="primary" indeterminate></v-progress-linear>
              </UiParentCard>
            </v-col>
            <!-- Linear -->
            <v-col cols="12">
              <UiParentCard title="Linear">
                <v-progress-linear aria-label="progressbar" color="primary" v-model="p1"></v-progress-linear>
              </UiParentCard>
            </v-col>
            <!-- Linear Reverse Intermidiate -->
            <v-col cols="12">
              <UiParentCard title="Linear Reverse Intermidiate">
                <v-progress-linear aria-label="progressbar" color="primary" reverse indeterminate></v-progress-linear>
              </UiParentCard>
            </v-col>
            <!-- Linear Reverse -->
            <v-col cols="12">
              <UiParentCard title="Linear Reverse">
                <v-progress-linear aria-label="progressbar" color="primary" reverse model-value="15"></v-progress-linear>
              </UiParentCard>
            </v-col>
            <!-- Linear with label -->
            <v-col cols="12">
              <UiParentCard title="Linear With Label">
                <v-progress-linear aria-label="progressbar" v-model="withLabel" color="success" class="mb-3" height="25">
                  <template v-slot:default="{ value }">
                    <strong class="text-surface">{{ Math.ceil(value) }}%</strong>
                  </template>
                </v-progress-linear>
                <v-progress-linear aria-label="progressbar" v-model="withLabel1" color="primary" class="mb-3" height="25">
                  <template v-slot:default="{ value }">
                    <strong class="text-surface">{{ Math.ceil(value) }}%</strong>
                  </template>
                </v-progress-linear>
                <v-progress-linear aria-label="progressbar" v-model="withLabel2" color="error" height="25">
                  <template v-slot:default="{ value }">
                    <strong>{{ Math.ceil(value) }}%</strong>
                  </template>
                </v-progress-linear>
              </UiParentCard>
            </v-col>
            <!-- Height -->
            <v-col cols="12">
              <UiParentCard title="Linear Color With Height">
                <div class="d-flex flex-column ga-4">
                  <div v-for="progress in pheight" :key="progress.color" class="d-flex align-center">
                    <v-progress-linear
                      aria-label="progressbar"
                      rounded
                      :color="progress.color"
                      :model-value="progress.value"
                      :height="progress.size"
                    ></v-progress-linear>
                    <span class="text-caption text-lightText ms-3">{{ progress.value }}%</span>
                  </div>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Linear Stream -->
            <v-col cols="12">
              <UiParentCard title="Linear Stream">
                <v-progress-linear aria-label="progressbar" color="primary" model-value="20" buffer-value="0" stream> </v-progress-linear>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
