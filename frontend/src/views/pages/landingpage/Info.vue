// src/views/pages/Info.vue
<script setup lang="ts">
import { ref } from 'vue';
import { useCustomizerStore } from '@/stores/customizer';
import Appbar from './Components/AppBarMenu.vue';
import FooterSection from './Components/FooterSection.vue';
import { BookOpen, Users, Lightbulb, Brain } from 'lucide-vue-next';

const panels = ref(['lesson-planning']);
const customizer = useCustomizerStore();

const faqSections = [
  {
    title: "How does Mathilda create personalized lesson plans?",
    content: "Mathilda uses advanced AI technology to generate customized lesson plans based on your student profiles, teaching objectives, and curriculum requirements. Each plan is tailored to accommodate different learning styles and abilities.",
    value: "lesson-planning"
  },
  {
    title: "What are student profiles and how do they work?",
    content: "Student profiles store important information about learning styles, abilities, and needs. This includes demographics, general background, math ability, engagement preferences, and special considerations. These profiles help Mathilda customize content for better learning outcomes.",
    value: "profiles"
  },
  {
    title: "Can I modify AI-generated lesson plans?",
    content: "Yes! While Mathilda creates comprehensive lesson plans, you maintain full control. You can edit, adjust, or enhance any part of the plan through our interactive interface. The AI assistant can help refine plans based on your feedback.",
    value: "customization"
  },
  {
    title: "How does Mathilda support different learning styles?",
    content: "Mathilda integrates various teaching strategies based on student profiles, including visual learning, hands-on activities, collaborative exercises, and technology-enhanced learning. Each lesson plan can be adapted to match your students' preferred learning methods.",
    value: "learning-styles"
  }
];
</script>

<template>
  <v-layout class="flex-column" :class="customizer.actTheme === 'dark' ? 'bg-containerBg' : 'bg-surface'">
    <Appbar />
    <v-main class="mx-0 pt-16 pb-0">
      <!-- Hero Section -->
      <section class="bg-primary pa-12 position-relative">
        <v-container>
          <v-row class="justify-center">
            <v-col cols="12" lg="8" class="text-center">
              <h1 class="text-h2 font-weight-bold mb-4 text-white">
                Empowering Teachers with AI Technology
              </h1>
              <p class="text-h5 text-white-darken-2 mb-0">
                Learn how Mathilda helps you create personalized learning experiences
              </p>
            </v-col>
          </v-row>
        </v-container>
      </section>

      <!-- Features Grid -->
      <section class="py-16">
        <v-container>
          <v-row>
            <v-col cols="12" md="6" lg="3">
              <v-card elevation="1" class="pa-6 h-100">
                <BookOpen :size="32" class="text-primary mb-4" />
                <h3 class="text-h5 mb-2">Smart Lesson Planning</h3>
                <p class="text-body-1">Create customized lesson plans powered by advanced AI technology</p>
              </v-card>
            </v-col>
            <v-col cols="12" md="6" lg="3">
              <v-card elevation="1" class="pa-6 h-100">
                <Users :size="32" class="text-primary mb-4" />
                <h3 class="text-h5 mb-2">Student Profiles</h3>
                <p class="text-body-1">Manage detailed student profiles for personalized learning</p>
              </v-card>
            </v-col>
            <v-col cols="12" md="6" lg="3">
              <v-card elevation="1" class="pa-6 h-100">
                <Lightbulb :size="32" class="text-primary mb-4" />
                <h3 class="text-h5 mb-2">Adaptive Content</h3>
                <p class="text-body-1">Automatically adapt content to match learning styles</p>
              </v-card>
            </v-col>
            <v-col cols="12" md="6" lg="3">
              <v-card elevation="1" class="pa-6 h-100">
                <Brain :size="32" class="text-primary mb-4" />
                <h3 class="text-h5 mb-2">Learning Insights</h3>
                <p class="text-body-1">Track progress and optimize teaching strategies</p>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </section>

      <!-- FAQ Section -->
      <section class="py-16 bg-surface">
        <v-container>
          <v-row class="justify-center mb-12">
            <v-col cols="12" lg="8" class="text-center">
              <h2 class="text-h3 mb-2">Frequently Asked Questions</h2>
              <p class="text-h6 text-medium-emphasis">
                Learn more about how Mathilda can enhance your teaching experience
              </p>
            </v-col>
          </v-row>

          <v-row class="justify-center">
            <v-col cols="12" md="8">
              <v-card elevation="1" class="pa-6">
                <v-expansion-panels v-model="panels" multiple>
                  <v-expansion-panel
                    v-for="item in faqSections"
                    :key="item.value"
                    :value="item.value"
                    elevation="0"
                    class="mb-2"
                  >
                    <template v-slot:title>
                      <span class="text-h6">{{ item.title }}</span>
                    </template>
                    <v-expansion-panel-text class="text-body-1">
                      {{ item.content }}
                    </v-expansion-panel-text>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </section>
    </v-main>
    <FooterSection />
  </v-layout>
</template>

<style lang="scss" scoped>
.v-expansion-panel {
  background-color: transparent !important;
  
  &::before {
    box-shadow: none !important;
  }
}

.v-card {
  border-radius: 12px;
  transition: transform 0.2s ease-in-out;
  
  &:hover {
    transform: translateY(-4px);
  }
}

h1, h2, h3 {
  font-family: 'Museo Moderno', sans-serif;
}

.text-body-1 {
  font-family: 'Quicksand', sans-serif;
  line-height: 1.6;
}

.bg-primary {
  background: linear-gradient(45deg, #78C0E5, #B7E6F2);
}
</style>