<script setup lang="ts">
import { ref } from 'vue';

import Appbar from './Components/AppBarMenu.vue';
import FooterSection from './Components/FooterSection.vue';
import NewsLetter from './Components/NewsLetter2.vue';
import { useCustomizerStore } from '@/stores/customizer';
const panel = ref(['foo']);
const customizer = useCustomizerStore();
</script>

<template>
  <v-layout class="flex-column" :class="customizer.actTheme === 'dark' ? 'bg-containerBg' : 'bg-surface'">
    <Appbar />
    <v-row class="justify-center">
      <v-col cols="12" class="py-0">
        <v-main class="mx-0 pt-16 pb-0 position-relative overflow-hidden">
          <div class="bg-blur">
            <div class="round-1"></div>
            <div class="round-2"></div>
          </div>
          <v-container class="maxWidth">
            <v-row class="justify-center py-10">
              <v-col cols="12" lg="5" md="6" sm="8">
                <div class="text-center position-relative pt-3">
                  <h2 class="text-h2 mb-2">Question ? Look here.</h2>
                  <p class="text-h6 text-lightText mb-0">Please refer the Frequently ask question for your quick help</p>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-main>
      </v-col>
      <v-col cols="12" md="8" lg="7" class="pt-0">
        <div class="py-md-16 py-8 px-4">
          <v-card elevation="0" class="py-0">
            <v-expansion-panels v-model="panel" multiple>
              <v-expansion-panel
                elevation="0"
                title="When do I need Extended License?"
                text="If your End Product which is sold - Then only your required Extended License. i.e. If you take subscription charges (monthly, yearly, etc...) from your end users in this case you required Extended License."
                value="foo"
              ></v-expansion-panel>
              <v-expansion-panel
                elevation="0"
                title="What Support Includes?"
                text="6 Months of Support Includes with 1 year of free updates. We are happy to solve your bugs, issue."
                value="support"
              ></v-expansion-panel>
              <v-expansion-panel
                elevation="0"
                title="Is Mantis Support TypeScript?"
                text="Yes, Mantis Support the TypeScript and it is only available in Plus and Extended License."
                value="typescript"
              ></v-expansion-panel>
              <v-expansion-panel
                elevation="0"
                title="Is there any RoadMap for Mantis?"
                text="Mantis is our flagship React Dashboard Template and we always add the new features for the long run. You can check the Roadmap in Documentation."
                value="raodmap"
              ></v-expansion-panel>
            </v-expansion-panels>
          </v-card>
        </div>
      </v-col>
    </v-row>
    <NewsLetter />
    <FooterSection />
  </v-layout>
</template>
