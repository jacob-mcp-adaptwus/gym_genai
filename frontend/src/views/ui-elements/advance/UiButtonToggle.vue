<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Buttons toggle' });
const subContent = ref({ content: 'Use data properties to control the visibility and methods to toggle them.' });
const path = ref({ filepath: 'src/views/ui-elements/advance/button-toggle' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/button-groups/' });

const toggle = ref(null);
const toggle1 = ref(2);
const toggle4 = ref(1);
const toggle5 = ref(0);
const toggle6 = ref(0);
const toggle7 = ref(0);
const toggle8 = ref(2);
const toggle9 = ref(2);
const toggle2 = ref(undefined);
const toggle3 = ref([]);

const alignment = ref(1);
const formatting = ref([]);
const value = ref('Toggle button requirements.\r\rHave at least three toggle buttons in a group\rLabel buttons with text, an icon, or');
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Default -->
        <v-col cols="12" lg="3" md="6">
          <UiParentCard title="Default">
            <div class="text-center">
              <v-btn-toggle color="primary" v-model="toggle">
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Outlined -->
        <v-col cols="12" lg="3" md="6">
          <UiParentCard title="Outlined">
            <div class="text-center">
              <v-btn-toggle variant="outlined" color="primary" v-model="toggle1">
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Text -->
        <v-col cols="12" lg="3" md="6">
          <UiParentCard title="Text">
            <div class="text-center">
              <v-btn-toggle variant="text" color="primary" v-model="toggle4">
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Plain -->
        <v-col cols="12" lg="3" md="6">
          <UiParentCard title="Plain">
            <div class="text-center">
              <v-btn-toggle variant="plain" color="primary" v-model="toggle5">
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Mandatory -->
        <v-col cols="12" md="6">
          <UiParentCard title="Mandatory">
            <div class="text-center">
              <v-btn-toggle v-model="toggle2" color="primary" mandatory>
                <v-btn icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
              <div class="font-weight-medium text-medium-emphasis pa-2">{{ toggle2 }}</div>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Multiple -->
        <v-col cols="12" md="6">
          <UiParentCard title="Multiple">
            <div class="text-center">
              <v-btn-toggle v-model="toggle3" color="primary" variant="text" multiple>
                <v-btn size="small" icon value="italic" aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-italic"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="bold" aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-bold"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="underline" aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-underline"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="color" aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-color"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
              <div class="font-weight-medium text-medium-emphasis pa-2">{{ toggle3 }}</div>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Rounded Sqaure -->
        <v-col cols="12" md="6">
          <UiParentCard title="Rounded Sqaure">
            <div class="text-center">
              <v-btn-toggle v-model="toggle5" color="primary" variant="outlined" rounded="0">
                <v-btn icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Rounded Pill -->
        <v-col cols="12" md="6">
          <UiParentCard title="Rounded Pill">
            <div class="text-center">
              <v-btn-toggle v-model="toggle6" color="primary" variant="outlined" rounded="xl">
                <v-btn icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>

        <!-- Density -->
        <v-col cols="12" md="6">
          <UiParentCard title="Density">
            <div class="text-center">
              <v-btn-toggle class="d-block mb-4" v-model="toggle7" color="primary" variant="outlined" density="compact">
                <v-btn size="small" icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>

              <v-btn-toggle class="d-block mb-4" v-model="toggle8" color="primary" variant="outlined" density="comfortable">
                <v-btn size="small" icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn size="small" icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>

              <v-btn-toggle class="d-block mb-4" v-model="toggle9" color="primary" variant="outlined">
                <v-btn icon value="left" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="center" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="right" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
                <v-btn icon value="justify" aria-label="toggle">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-justify"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>
          </UiParentCard>
        </v-col>

        <!-- Customized -->
        <v-col cols="12" md="6">
          <UiParentCard title="Customized">
            <div class="d-flex justify-space-between pb-4">
              <v-btn-toggle v-model="formatting" multiple variant="outlined" class="overflow-auto" color="primary" divided>
                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-italic"></use>
                  </svg>
                </v-btn>

                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-bold"></use>
                  </svg>
                </v-btn>

                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-underline"></use>
                  </svg>
                </v-btn>

                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-color"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>

              <v-btn-toggle v-model="alignment" variant="outlined" color="primary" divided>
                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-right"></use>
                  </svg>
                </v-btn>

                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-center"></use>
                  </svg>
                </v-btn>

                <v-btn size="small" icon aria-label="toggle">
                  <svg class="pc-icon" style="width: 16px; height: 16px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-align-left"></use>
                  </svg>
                </v-btn>
              </v-btn-toggle>
            </div>

            <v-sheet class="text-center">
              <v-textarea v-model="value" aria-label="content" variant="outlined" auto-grow full-width rows="2" hide-details></v-textarea>
            </v-sheet>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
