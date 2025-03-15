<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Snackbar' });
const subContent = ref({ content: 'Snackbars provide brief notifications. The component is also known as a toast.' });
const path = ref({ filepath: 'src/views/ui-elements/advance/snackbar' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/snackbars/' });

const primarysnackbar = ref(false);
const secondarysnackbar = ref(false);
const errorsnackbar = ref(false);
const successsnackbar = ref(false);
const warningsnackbar = ref(false);
const infosnackbar = ref(false);

const primary9snackbar = ref(false);
const secondary9snackbar = ref(false);
const error9snackbar = ref(false);
const success9snackbar = ref(false);
const warning9snackbar = ref(false);
const info9snackbar = ref(false);

const primary10snackbar = ref(false);
const secondary10snackbar = ref(false);
const error10snackbar = ref(false);
const success10snackbar = ref(false);
const warning10snackbar = ref(false);
const info10snackbar = ref(false);

const primary2snackbar = ref(false);
const secondary2snackbar = ref(false);
const info2snackbar = ref(false);
const error2snackbar = ref(false);
const success2snackbar = ref(false);
const warning2snackbar = ref(false);

const primary11snackbar = ref(false);
const secondary11snackbar = ref(false);
const info11snackbar = ref(false);
const error11snackbar = ref(false);
const success11snackbar = ref(false);
const warning11snackbar = ref(false);

const primary3snackbar = ref(false);
const primary4snackbar = ref(false);
const primary5snackbar = ref(false);
const primary6snackbar = ref(false);
const primary7snackbar = ref(false);
const primary8snackbar = ref(false);

const snackbar12 = ref(false);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Basic -->
            <v-col cols="12">
              <UiParentCard title="Basic">
                <div class="d-flex flex-column flex-sm-row align-center flex-wrap ga-4">
                  <v-btn variant="flat" color="primary" rounded="md" @click="primarysnackbar = true"> default </v-btn>
                  <v-btn variant="flat" color="secondary" rounded="md" @click="secondarysnackbar = true"> secondary </v-btn>
                  <v-btn variant="flat" color="success" rounded="md" class="text-surface" @click="successsnackbar = true"> success </v-btn>
                  <v-btn variant="flat" color="warning" rounded="md" class="text-surface" @click="warningsnackbar = true"> warning </v-btn>
                  <v-btn variant="flat" color="info" rounded="md" @click="infosnackbar = true"> info </v-btn>
                  <v-btn variant="flat" color="error" rounded="md" @click="errorsnackbar = true"> error </v-btn>
                </div>

                <v-snackbar color="primary" variant="flat" elevation-1 rounded="md" v-model="primarysnackbar" location="bottom right">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                </v-snackbar>
                <v-snackbar color="secondary" variant="flat" elevation-1 rounded="md" v-model="secondarysnackbar" location="bottom right">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is secondary message
                </v-snackbar>
                <v-snackbar
                  variant="flat"
                  color="success"
                  rounded="md"
                  class="text-surface"
                  v-model="successsnackbar"
                  location="bottom right"
                >
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Success message
                </v-snackbar>
                <v-snackbar
                  variant="flat"
                  color="warning"
                  rounded="md"
                  class="text-surface"
                  v-model="warningsnackbar"
                  location="bottom right"
                >
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                </v-snackbar>
                <v-snackbar variant="flat" color="info" rounded="md" class="text-surface" v-model="infosnackbar" location="bottom right">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Info message
                </v-snackbar>
                <v-snackbar variant="flat" color="error" rounded="md" v-model="errorsnackbar" location="bottom right">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Error message
                </v-snackbar>
              </UiParentCard>
            </v-col>
            <!-- With Close -->
            <v-col cols="12">
              <UiParentCard title="With Close">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 flex-wrap">
                  <v-btn variant="flat" color="primary" rounded="md" @click="primary2snackbar = true"> default </v-btn>
                  <v-btn variant="flat" color="secondary" rounded="md" @click="secondary2snackbar = true"> secondary </v-btn>
                  <v-btn variant="flat" color="success" rounded="md" class="text-surface" @click="success2snackbar = true"> success </v-btn>
                  <v-btn variant="flat" color="warning" rounded="md" class="text-surface" @click="warning2snackbar = true"> warning </v-btn>
                  <v-btn variant="flat" color="info" rounded="md" class="text-surface" @click="info2snackbar = true"> info </v-btn>
                  <v-btn variant="flat" color="error" rounded="md" @click="error2snackbar = true"> error </v-btn>
                </div>

                <v-snackbar color="primary" variant="flat" elevation-1 rounded="md" v-model="primary2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="primary2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="secondary" variant="flat" elevation-1 rounded="md" v-model="secondary2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="secondary2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="success" variant="flat" rounded="md" class="text-surface" v-model="success2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Success message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="success2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="warning" variant="flat" rounded="md" class="text-surface" v-model="warning2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="warning2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="info" variant="flat" rounded="md" class="text-surface" v-model="info2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="info2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="error" aria-label="close" variant="flat" rounded="md" v-model="error2snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Error message
                  <template v-slot:actions>
                    <v-btn color="white" aria-label="close" variant="text" @click="error2snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
              </UiParentCard>
            </v-col>
            <!-- Location -->
            <v-col cols="12">
              <UiParentCard title="Position">
                <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary3snackbar = true"> Top Left </v-btn>
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary4snackbar = true"> Top Center </v-btn>
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary5snackbar = true"> Top Right </v-btn>
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary6snackbar = true"> Bottom Left </v-btn>
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary7snackbar = true"> Bottom </v-btn>
                  <v-btn color="primary" variant="flat" rounded="md" @click="primary8snackbar = true"> Bottom Right </v-btn>
                </div>

                <v-snackbar color="primary" variant="flat" elevation-1 rounded="md" location="top left" v-model="primary3snackbar">
                  I'm Top Left Message
                </v-snackbar>
                <v-snackbar color="primary" variant="flat" rounded="md" location="top" v-model="primary4snackbar">
                  I'm Top Center Message
                </v-snackbar>
                <v-snackbar color="primary" variant="flat" rounded="md" location="top right" v-model="primary5snackbar">
                  I'm Top Right Message
                </v-snackbar>
                <v-snackbar color="primary" variant="flat" rounded="md" location="bottom left" v-model="primary6snackbar">
                  I'm Bottom Left Message
                </v-snackbar>
                <v-snackbar color="primary" variant="flat" rounded="md" location="bottom" v-model="primary7snackbar">
                  I'm Bottom Center Message
                </v-snackbar>
                <v-snackbar color="primary" variant="flat" rounded="md" location="bottom right" v-model="primary8snackbar">
                  I'm Bottom Right Message
                </v-snackbar>
              </UiParentCard>
            </v-col>
            <v-col cols="12">
              <UiParentCard title="Vertical">
                <v-btn color="secondary" variant="tonal" rounded="md" @click="snackbar12 = true"> Open Snackbar </v-btn>

                <v-snackbar v-model="snackbar12" color="secondary" variant="tonal" vertical>
                  <div class="text-subtitle-1 pb-2">This is a snackbar message</div>

                  <p>This is a longer paragraph explaining something</p>

                  <template v-slot:actions>
                    <v-btn color="indigo" variant="text" @click="snackbar12 = false"> Close </v-btn>
                  </template>
                </v-snackbar>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="12" md="6">
          <v-row>
            <!-- Outlined -->
            <v-col cols="12">
              <UiParentCard title="Outlined">
                <div class="d-flex flex-column flex-sm-row align-center flex-wrap ga-4">
                  <v-btn variant="outlined" color="primary" rounded="md" @click="primary9snackbar = true"> default </v-btn>
                  <v-btn variant="outlined" color="secondary" rounded="md" @click="secondary9snackbar = true"> secondary </v-btn>
                  <v-btn variant="outlined" color="success" rounded="md" class="text-surface" @click="success9snackbar = true">
                    success
                  </v-btn>
                  <v-btn variant="outlined" color="warning" rounded="md" class="text-surface" @click="warning9snackbar = true">
                    warning
                  </v-btn>
                  <v-btn variant="outlined" color="info" rounded="md" @click="info9snackbar = true"> info </v-btn>
                  <v-btn variant="outlined" color="error" rounded="md" @click="error9snackbar = true"> error </v-btn>
                </div>

                <v-snackbar color="primary" variant="outlined" elevation-1 rounded="md" v-model="primary9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                </v-snackbar>
                <v-snackbar color="secondary" variant="outlined" elevation-1 rounded="md" v-model="secondary9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is secondary message
                </v-snackbar>
                <v-snackbar variant="outlined" color="success" rounded="md" class="text-surface" v-model="success9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Success message
                </v-snackbar>
                <v-snackbar variant="outlined" color="warning" rounded="md" class="text-surface" v-model="warning9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                </v-snackbar>
                <v-snackbar variant="outlined" color="info" rounded="md" class="text-surface" v-model="info9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Info message
                </v-snackbar>
                <v-snackbar variant="outlined" color="error" rounded="md" v-model="error9snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Error message
                </v-snackbar>
              </UiParentCard>
            </v-col>
            <!-- action -->
            <v-col cols="12">
              <UiParentCard title="With Close + Action">
                <div class="d-flex flex-column flex-sm-row align-center flex-wrap ga-4">
                  <v-btn variant="outlined" color="primary" rounded="md" @click="primary10snackbar = true"> default </v-btn>
                  <v-btn variant="outlined" color="secondary" rounded="md" @click="secondary10snackbar = true"> secondary </v-btn>
                  <v-btn variant="outlined" color="success" rounded="md" class="text-surface" @click="success10snackbar = true">
                    success
                  </v-btn>
                  <v-btn variant="outlined" color="warning" rounded="md" class="text-surface" @click="warning10snackbar = true">
                    warning
                  </v-btn>
                  <v-btn variant="outlined" color="info" rounded="md" @click="info10snackbar = true"> info </v-btn>
                  <v-btn variant="outlined" color="error" rounded="md" @click="error10snackbar = true"> error </v-btn>
                </div>

                <v-snackbar color="primary" variant="outlined" elevation-1 rounded="md" v-model="primary10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="primary10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="primary10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="secondary" variant="outlined" elevation-1 rounded="md" v-model="secondary10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is secondary message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="secondary10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="secondary10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar variant="outlined" color="success" rounded="md" class="text-surface" v-model="success10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Success message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="success10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="success10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar variant="outlined" color="warning" rounded="md" class="text-surface" v-model="warning10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="warning10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="warning10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar variant="outlined" color="info" rounded="md" class="text-surface" v-model="info10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Info message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="info10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="info10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar variant="outlined" color="error" rounded="md" v-model="error10snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Error message
                  <template v-slot:actions>
                    <v-btn variant="text" size="small" @click="error10snackbar = false"> Undo </v-btn>
                    <v-btn variant="text" aria-label="close" @click="error10snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close-square-fill"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
              </UiParentCard>
            </v-col>
            <!-- Tonal -->
            <v-col cols="12">
              <UiParentCard title="With Close">
                <div class="d-flex flex-column flex-sm-row align-center ga-4 flex-wrap">
                  <v-btn variant="tonal" color="primary" rounded="md" @click="primary11snackbar = true"> default </v-btn>
                  <v-btn variant="tonal" color="secondary" rounded="md" @click="secondary11snackbar = true"> secondary </v-btn>
                  <v-btn variant="tonal" color="success" rounded="md" class="text-surface" @click="success11snackbar = true">
                    success
                  </v-btn>
                  <v-btn variant="tonal" color="warning" rounded="md" class="text-surface" @click="warning11snackbar = true">
                    warning
                  </v-btn>
                  <v-btn variant="tonal" color="info" rounded="md" class="text-surface" @click="info11snackbar = true"> info </v-btn>
                  <v-btn variant="tonal" color="error" rounded="md" @click="error11snackbar = true"> error </v-btn>
                </div>

                <v-snackbar color="primary" variant="tonal" elevation-1 rounded="md" v-model="primary11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="primary11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="secondary" variant="tonal" elevation-1 rounded="md" v-model="secondary11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is default message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="secondary11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="success" variant="tonal" rounded="md" class="text-surface" v-model="success11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Success message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="success11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="warning" variant="tonal" rounded="md" class="text-surface" v-model="warning11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="warning11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="info" variant="tonal" rounded="md" class="text-surface" v-model="info11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Warning message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="info11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
                <v-snackbar color="error" variant="tonal" rounded="md" v-model="error11snackbar">
                  <svg class="pc-icon" style="width: 20px; height: 20px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-checkbox-marked-circle-outline"></use>
                  </svg>
                  This is Error message
                  <template v-slot:actions>
                    <v-btn variant="text" aria-label="close" @click="error11snackbar = false">
                      <svg class="pc-icon" style="width: 20px; height: 20px; transform: rotate(45deg)">
                        <use xlink:href="/assets/svg/sprite.svg#custom-close"></use>
                      </svg>
                    </v-btn>
                  </template>
                </v-snackbar>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.v-snackbar--variant-outlined {
  background-color: rgb(var(--v-theme-containerBg));
}
.v-snackbar--vertical {
  font-family: 'Public sans', sans-serif;
}
</style>
