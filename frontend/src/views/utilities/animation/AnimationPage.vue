<script setup lang="ts">
import { ref } from 'vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Animation' });
const subContent = ref({ content: 'Animation allows you to give different effects in images or cards.' });
const path = ref({ filepath: 'src/views/utilities/animation' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/styles/transitions/' });

const fadeTran = ref(true);
const expandTran = ref(true);
const fabTran = ref(true);
const slidxTran = ref(true);
const slidyTran = ref(true);
const scrolTran = ref(true);
const scrolyTran = ref(true);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12" md="12">
      <v-row>
        <v-col cols="12" sm="6">
          <UiParentCard title="Slide X Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="slidxTran = !slidxTran"> Slide X Transition </v-btn>
            <br />
            <v-slide-x-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="slidxTran" class="rounded-md mt-8 w-75" />
            </v-slide-x-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Slide y Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="slidyTran = !slidyTran"> Slide Y Transition </v-btn>
            <br />
            <v-slide-y-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="slidyTran" class="rounded-md mt-8 w-75" />
            </v-slide-y-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Scroll x Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="scrolTran = !scrolTran"> Scroll x Transition </v-btn>
            <br />
            <v-scroll-x-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="scrolTran" class="rounded-md mt-8 w-75" />
            </v-scroll-x-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Scroll y Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="scrolyTran = !scrolyTran"> Scroll Y Transition </v-btn>
            <br />
            <v-scroll-y-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="scrolyTran" class="rounded-md mt-8 w-75" />
            </v-scroll-y-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Expand Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="expandTran = !expandTran"> Expand-transition </v-btn>
            <br />
            <v-expand-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="expandTran" class="rounded-md mt-8 w-75" />
            </v-expand-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Fab Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="fabTran = !fabTran"> Fab-transition </v-btn>
            <br />
            <v-fab-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="fabTran" class="rounded-md mt-8 w-75" />
            </v-fab-transition>
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="6">
          <UiParentCard title="Fade Transition">
            <v-btn color="primary" variant="outlined" class="ma-2" @click="fadeTran = !fadeTran"> Fade-transition </v-btn>
            <br />
            <v-fade-transition>
              <img src="@/assets/images/background/img-profile-bg.png" alt="mantis" v-show="fadeTran" class="rounded-md mt-8 w-75" />
            </v-fade-transition>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
