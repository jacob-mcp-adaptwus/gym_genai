<script setup lang="ts">
import { ref } from 'vue';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Slider' });
const subContent = ref({ content: 'Sliders allow users to make selections from a range of values.' });
const path = ref({ filepath: 'src/views/forms/components/slider' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/sliders/' });

const slider1 = ref(50);
const slider2 = ref(40);
const volume = ref(40);
const min = ref(-50);
const max = ref(90);
const slider3 = ref(40);
const slider4 = ref(40);
const slider5 = ref(40);
const slider6 = ref(40);
const slider7 = ref(40);
const slider8 = ref(40);
const slider9 = ref(60);
const slider10 = ref(40);
const slider11 = ref(90);
const slider12 = ref(30);
const slider13 = ref(70);
const slider14 = ref(10);
const red = ref(64);
const green = ref(128);
const blue = ref(10);
</script>

// ===============================|| Ui Slider ||=============================== //
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic Slider -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Basic Slider">
            <v-slider v-model="slider1" color="primary" label="basic"></v-slider>
          </UiParentCard>
        </v-col>
        <!-- Disabled -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Disabled">
            <v-slider v-model="slider2" color="primary" label="basic" disabled></v-slider>
          </UiParentCard>
        </v-col>
        <!-- Volume -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Volume">
            <v-slider v-model="volume" color="primary" min="40" max="218" :step="1">
              <template v-slot:prepend>
                <v-btn size="small" icon variant="text" aria-label="volume" color="primary">
                  <div class="text-darkText me-1">
                    <SvgSprite name="custom-speaker-outline" style="width: 20px; height: 20px" />
                  </div>
                </v-btn>
              </template>

              <template v-slot:append>
                <v-btn size="small" icon variant="text" aria-label="volume" color="primary">
                  <div class="text-darkText me-1">
                    <SvgSprite name="custom-sound-outline" style="width: 20px; height: 20px" />
                  </div>
                </v-btn>
              </template>
            </v-slider>
          </UiParentCard>
        </v-col>
        <!-- With Label -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="With Label">
            <div class="d-flex ga-4 align-center flex-row">
              <v-label class="text-subtitlte-1">Progress</v-label>
              <v-slider v-model="slider3" class="align-center" :max="max" :min="min" step="1" hide-details color="primary">
                <template v-slot:append>
                  <v-text-field variant="plain" aria-label="value" v-model="slider3"></v-text-field>
                </template>
              </v-slider>
            </div>
            <div class="d-flex ga-4 align-center flex-row">
              <v-label class="text-subtitlte-1">Progress</v-label>
              <v-slider v-model="slider4" class="align-center" :max="max" :min="min" step="1" hide-details color="secondary">
                <template v-slot:append>
                  <v-text-field variant="plain" aria-label="value" v-model="slider4"></v-text-field>
                </template>
              </v-slider>
            </div>
          </UiParentCard>
        </v-col>
        <!-- With Popup value -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="With Popup value">
            <v-slider class="mt-3" v-model="slider5" color="primary" step="1" thumb-label="always"></v-slider>
          </UiParentCard>
        </v-col>
        <!-- Steps With Popup Value -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Steps With Popup Value">
            <v-slider class="mt-3" v-model="slider6" color="primary" step="10" show-ticks="always" thumb-label="always"></v-slider>
          </UiParentCard>
        </v-col>
        <!-- Vertical Slider -->
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Vertical Slider">
            <div class="d-flex">
              <v-slider v-model="slider7" direction="vertical" label="Regular" color="primary"></v-slider>
              <v-slider v-model="slider8" direction="vertical" label="Regular" color="primary" disabled></v-slider>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="Color">
            <v-slider v-model="slider9" color="primary"></v-slider>
            <v-slider v-model="slider10" color="secondary"></v-slider>
            <v-slider v-model="slider11" color="success"></v-slider>
            <v-slider v-model="slider12" color="warning"></v-slider>
            <v-slider v-model="slider13" color="info"></v-slider>
            <v-slider v-model="slider14" color="error"></v-slider>
          </UiParentCard>
        </v-col>
        <v-col cols="12" lg="4" md="6">
          <UiParentCard title="RGB color">
            <v-responsive :style="{ background: `rgb(${red}, ${green}, ${blue})` }" height="150px"></v-responsive>

            <v-card-text class="pa-0">
              <v-slider v-model="red" :max="255" :step="1" label="R" color="primary" hide-details class="ma-4">
                <template v-slot:append>
                  <v-text-field
                    v-model="red"
                    type="number"
                    aria-label="value"
                    style="width: 80px"
                    density="compact"
                    hide-details
                    variant="outlined"
                  ></v-text-field>
                </template>
              </v-slider>

              <v-slider v-model="green" :max="255" :step="1" label="G" color="primary" hide-details class="ma-4">
                <template v-slot:append>
                  <v-text-field
                    v-model="green"
                    type="number"
                    aria-label="value"
                    style="width: 80px"
                    density="compact"
                    hide-details
                    variant="outlined"
                  ></v-text-field>
                </template>
              </v-slider>

              <v-slider v-model="blue" :max="255" :step="1" label="B" color="primary" hide-details class="ma-4">
                <template v-slot:append>
                  <v-text-field
                    v-model="blue"
                    type="number"
                    aria-label="value"
                    style="width: 80px"
                    density="compact"
                    hide-details
                    variant="outlined"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-card-text>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.v-slider {
  --v-input-padding-top: 15px;
  .v-input--density-default {
    --v-input-padding-top: 15px;
  }
}
</style>
