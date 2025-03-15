<script setup lang="ts">
import { ref, computed } from 'vue';
import { useLessonStore } from '@/stores/lessons';
import LessonForm from '@/components/apps/lessons/LessonForm.vue';
import LessonPlanDisplay from '@/components/apps/lessons/LessonPlanDisplay.vue';
import LessonChat from '@/components/apps/lessons/LessonChat.vue';
import type { Lesson, LessonPlan } from '@/services/lessonService';
import type { Profile } from '@/services/profileService';
import { Loader } from 'lucide-vue-next';

const lessonStore = useLessonStore();
const currentPlan = ref<LessonPlan | null>(null);
const showChatWindow = ref(false);
const error = ref<string | null>(null);
const activeTab = ref('plan');
const saveSnackbar = ref(false);
const saveSnackbarText = ref('');
const saveSnackbarColor = ref('success');
const chatLoading = ref(false);
const initialLoading = ref(false);
const selectedSections = ref<string[]>([]);

const isGenerating = computed(() => lessonStore.isLoading);
const isSaving = computed(() => lessonStore.isSaving);
const isLoading = computed(() => isGenerating.value || chatLoading.value || isSaving.value);

const handleGenerate = async (topic: string, profile: Profile | null) => {
  try {
    error.value = null;
    initialLoading.value = true;
    const lessonPlan = await lessonStore.generateLessonPlan({
      topic,
      profile
    });
    currentPlan.value = typeof lessonPlan === 'string' ? JSON.parse(lessonPlan) : lessonPlan;
    showChatWindow.value = true;
    activeTab.value = 'plan';
  } catch (err) {
    console.error('Error generating lesson plan:', err);
    error.value = err instanceof Error ? err.message : 'An error occurred';
  } finally {
    initialLoading.value = false;
  }
};

const handleChatMessage = async (message: string) => {
  if (!currentPlan.value) return;

  try {
    chatLoading.value = true;
    const existingPlan = JSON.stringify(currentPlan.value) + 
      "  user has requested this latest change: ......" + 
      message + 
      "......end latest user input ";
    
    const updatedPlan = await lessonStore.generateLessonPlan({
      topic: currentPlan.value.metadata.topic,
      existingPlan: existingPlan
    });
    currentPlan.value = typeof updatedPlan === 'string' ? 
      JSON.parse(updatedPlan) : updatedPlan;
  } catch (err) {
    console.error('Error updating lesson plan:', err);
    error.value = err instanceof Error ? err.message : 'An error occurred';
  } finally {
    chatLoading.value = false;
  }
};

const handleSave = async () => {
  if (!currentPlan.value) return;

  try {
    const lessonData: Partial<Lesson> = {
      title: currentPlan.value.metadata.topic,  // Access topic from metadata
      subject: currentPlan.value.subject,
      grade: currentPlan.value.grade,
      duration: currentPlan.value.total_duration,
      content: JSON.stringify(currentPlan.value),
      status: 'draft',
      lastModified: new Date().toISOString()
    };

    await lessonStore.saveLessonPlan(lessonData);
    
    saveSnackbarText.value = 'Lesson plan saved successfully!';
    saveSnackbarColor.value = 'success';
    saveSnackbar.value = true;
  } catch (err) {
    saveSnackbarText.value = err instanceof Error ? err.message : 'Failed to save lesson plan';
    saveSnackbarColor.value = 'error';
    saveSnackbar.value = true;
  }
};

const handleReset = () => {
  currentPlan.value = null;
  showChatWindow.value = false;
  error.value = null;
  activeTab.value = 'form';
};

const handleCloseSnackbar = () => {
  saveSnackbar.value = false;
  lessonStore.clearSaveStatus();
};

const handleSectionSelect = (section: string) => {
  selectedSections.value = [section];
};
</script>

<template>
  <v-container fluid>
    <v-row>
      <!-- Left Column: Lesson Form -->
      <v-col 
        :cols="12" 
        :md="showChatWindow ? 3 : 4"
      >
        <LessonForm
          :is-generating="isGenerating"
          :has-current-plan="!!currentPlan"
          @generate="handleGenerate"
          @reset="handleReset"
          @save="handleSave"
        />

        <!-- Initial Loading Overlay -->
        <v-overlay
          v-model="initialLoading"
          contained
          persistent
          class="align-center justify-center"
        >
          <v-card-text class="text-center">
            <Loader class="animate-spin mb-4" :size="48" />
            <div class="text-h6">Generating Lesson Plan...</div>
            <div class="text-body-2 text-medium-emphasis">This may take a moment</div>
          </v-card-text>
        </v-overlay>
      </v-col>

      <!-- Middle Column: Lesson Plan Display -->
      <v-col 
        :cols="12" 
        :md="showChatWindow ? 6 : 8"
      >
        <LessonPlanDisplay
          :plan="currentPlan"
          :is-loading="isLoading"
          :selected-sections="selectedSections"
          :updated-sections="[]"
          @section-select="handleSectionSelect"
        />

        <!-- Error Alert -->
        <v-alert
          v-if="error"
          type="error"
          variant="tonal"
          closable
          class="mt-4"
          @click:close="error = null"
        >
          {{ error }}
        </v-alert>
      </v-col>

      <!-- Right Column: Chat Window -->
      <v-col 
        v-if="showChatWindow" 
        cols="12" 
        md="3"
      >
        <LessonChat
          :is-generating="chatLoading"
          :initial-message="
            'How would you like to improve this lesson plan? ' +
            'I can help you refine specific sections or make general improvements.'
          "
          @send-message="handleChatMessage"
        />
      </v-col>
    </v-row>

    <!-- Save Status Snackbar -->
    <v-snackbar
      v-model="saveSnackbar"
      :color="saveSnackbarColor"
      :timeout="3000"
      location="top"
    >
      {{ saveSnackbarText }}

      <template v-slot:actions>
        <v-btn
          color="white"
          variant="text"
          @click="handleCloseSnackbar"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>
<style lang="scss" scoped>
// Container Layout
.v-container {
  max-width: 1600px;
  margin: 0 auto;
  padding-bottom: 64px;
}

// Loading Overlay Styling
.v-overlay {
  backdrop-filter: blur(4px);
  
  .v-card-text {
    background: transparent;
    padding: 32px;

    .text-h6 {
      color: rgb(var(--v-theme-primary));
      font-family: 'Museo Moderno', sans-serif;
      font-weight: 600;
      font-size: 22pt;
    }

    .text-body-2 {
      font-family: 'Quicksand', sans-serif;
      font-size: 16pt;
    }
  }

  .animate-spin {
    animation: spin 1s linear infinite;
    color: rgb(var(--v-theme-primary));
  }
}

// Animation Keyframes
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

// Grid Layout
.v-row {
  > .v-col {
    transition: all 0.3s ease;
    padding: 12px;
    position: relative;
  }
}

// Transition Effects
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

// Custom Scrollbar
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(var(--v-theme-primary), 0.2);
  border-radius: 3px;
  
  &:hover {
    background: rgba(var(--v-theme-primary), 0.4);
  }
}

// Color Variables Based on Style Guide
:root {
  --primary-color: #78C0E5;
  --secondary-color: #EF8D61;
  --accent-1: #B7E6F2;
  --accent-2: #FFCDB5;
  --accent-3: #C8E0D9;
  --neutral-dark: #5C6970;
  --neutral-medium: #B7BBBE;
  --neutral-light: #F1F1F2;
}

// Alert Styling
.v-alert {
  font-family: 'Quicksand', sans-serif;
  border-radius: 8px;
  
  &.error {
    background-color: rgba(var(--v-theme-error), 0.1);
  }
}

// Snackbar Styling
.v-snackbar {
  .v-snackbar__wrapper {
    font-family: 'Quicksand', sans-serif;
    font-weight: 500;
  }
  
  .v-btn {
    font-family: 'Quicksand', sans-serif;
    font-weight: bold;
    font-size: 16pt;
    text-transform: none;
  }
}

// Responsive Design
@media (max-width: 960px) {
  .v-container {
    padding: 12px;
  }

  .v-row {
    > .v-col {
      padding: 8px;
    }
  }

  .v-overlay {
    .v-card-text {
      padding: 24px;

      .text-h6 {
        font-size: 20pt;
      }

      .text-body-2 {
        font-size: 14pt;
      }
    }
  }
}

// Dark Mode Support
:deep(.v-theme--dark) {
  .v-overlay {
    .text-h6 {
      color: var(--accent-1);
    }
  }

  .v-alert {
    &.error {
      background-color: rgba(var(--v-theme-error), 0.2);
    }
  }

  ::-webkit-scrollbar-thumb {
    background: rgba(var(--v-theme-primary), 0.3);
    
    &:hover {
      background: rgba(var(--v-theme-primary), 0.5);
    }
  }
}
</style>