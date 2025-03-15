<script setup lang="ts">
import { ref, computed } from 'vue';
import { useLessonStore } from '@/stores/lessons';
import { useProfileStore } from '@/stores/profiles';
import type { Profile } from '@/services/profileService';
import type { Lesson, LessonPlan } from '@/services/lessonService';
import LessonPlanDisplay from '@/components/apps/lessons/LessonPlanDisplay.vue';
import { Save, X } from 'lucide-vue-next';

interface Props {
  modelValue: boolean;
}

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
  (e: 'lesson-created', lesson: Lesson): void;
}>();

const lessonStore = useLessonStore();
const profileStore = useProfileStore();

const topic = ref('');
const selectedProfile = ref<Profile | null>(null);
const selectedGrade = ref('');
const selectedSubject = ref('');
const currentPlan = ref<LessonPlan | null>(null);
const error = ref<string | null>(null);
const isGenerating = ref(false);
const isSaving = ref(false);

const isValid = computed(() => {
  return topic.value.trim() !== '' && 
         selectedGrade.value !== '' && 
         selectedSubject.value !== '';
});

const activeProfiles = computed(() => {
  return profileStore.getSortedProfiles.filter(profile => profile.active);
});

const gradeOptions = [
  'K', '1st', '2nd', '3rd', '4th', '5th', 
  '6th', '7th', '8th', '9th', '10th', '11th', '12th'
];

const subjectOptions = [
  'Math', 'Science', 'English', 'History', 
  'Art', 'Music', 'Physical Education'
];

interface GenerateParams {
  topic: string;
  grade?: string;
  subject?: string;
  profile?: Profile | null;
  existingPlan?: string;
}

const handleClose = () => {
  emit('update:modelValue', false);
  resetForm();
};

const resetForm = () => {
  topic.value = '';
  selectedProfile.value = null;
  selectedGrade.value = '';
  selectedSubject.value = '';
  currentPlan.value = null;
  error.value = null;
};

const handleGenerate = async () => {
  if (!isValid.value) return;
  try {
    isGenerating.value = true;
    error.value = null;
    
    const generateParams: GenerateParams = {
      topic: topic.value,
      grade: selectedGrade.value,
      subject: selectedSubject.value,
      profile: selectedProfile.value
    };

    if (currentPlan.value) {
      generateParams.existingPlan = JSON.stringify(currentPlan.value);
    }
    
    const response = await lessonStore.generateLessonPlan(generateParams);
    const lessonPlan = typeof response === 'string' ? JSON.parse(response) : response;
    
    currentPlan.value = lessonPlan.lesson_plan || lessonPlan;
    
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to generate lesson plan';
    currentPlan.value = null;
  } finally {
    isGenerating.value = false;
  }
};

const handleSave = async () => {
  if (!currentPlan.value) return;

  try {
    isSaving.value = true;
    error.value = null;

    const lessonData: Partial<Lesson> = {
      title: topic.value,
      subject: selectedSubject.value,
      grade: selectedGrade.value,
      duration: currentPlan.value.total_duration,
      content: JSON.stringify(currentPlan.value),
      status: 'draft',
      lastModified: new Date().toISOString()
    };

    const response = await lessonStore.saveLessonPlan(lessonData);
    if (response.lesson) {
      emit('lesson-created', response.lesson);
      handleClose();
    }
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to save lesson plan';
  } finally {
    isSaving.value = false;
  }
};
</script>
# Template Section
<template>
  <v-dialog
    :model-value="modelValue"
    @update:model-value="emit('update:modelValue', $event)"
    max-width="1200"
    persistent
    class="create-lesson-dialog"
  >
    <v-card class="create-lesson-card">
      <!-- Dialog Header -->
      <v-card-title class="d-flex justify-space-between align-center pa-4">
        <span class="text-h5">Create New Lesson Plan</span>
        <v-btn
          icon
          variant="text"
          @click="handleClose"
          :disabled="isGenerating || isSaving"
        >
          <X :size="20" />
        </v-btn>
      </v-card-title>

      <v-divider></v-divider>

      <v-card-text class="pa-4">
        <v-row>
          <!-- Left Column: Form Controls -->
          <v-col cols="12" md="4">
            <v-form @submit.prevent="handleGenerate">
              <!-- Topic Input -->
              <v-text-field
                v-model="topic"
                label="Lesson Topic"
                required
                variant="outlined"
                :disabled="isGenerating || isSaving"
                :error-messages="error"
                class="mb-4"
              ></v-text-field>

              <!-- Grade Selection -->
              <v-select
                v-model="selectedGrade"
                :items="gradeOptions"
                label="Grade Level"
                required
                variant="outlined"
                :disabled="isGenerating || isSaving"
                class="mb-4"
              ></v-select>

              <!-- Subject Selection -->
              <v-select
                v-model="selectedSubject"
                :items="subjectOptions"
                label="Subject"
                required
                variant="outlined"
                :disabled="isGenerating || isSaving"
                class="mb-4"
              ></v-select>

              <!-- Profile Selection -->
              <v-select
                v-model="selectedProfile"
                :items="activeProfiles"
                item-title="profileName"
                label="Student Profile (Optional)"
                variant="outlined"
                :disabled="isGenerating || isSaving"
                clearable
                return-object
                class="mb-4"
              >
                <template v-slot:prepend-item>
                  <v-list-item
                    :title="activeProfiles.length ? 'Choose a profile' : 'No active profiles'"
                    :subtitle="activeProfiles.length ? 'Customize lesson for specific student' : 'Create profiles in My Profiles'"
                    density="compact"
                    class="text-primary"
                  >
                  </v-list-item>
                  <v-divider class="mt-2"></v-divider>
                </template>
              </v-select>

              <!-- Action Buttons -->
              <div class="d-flex flex-column gap-3">
                <v-btn
                  color="primary"
                  :loading="isGenerating"
                  :disabled="!isValid || isGenerating || isSaving"
                  @click="handleGenerate"
                  block
                >
                  {{ currentPlan ? 'Regenerate Plan' : 'Generate Plan' }}
                </v-btn>

                <v-btn
                  v-if="currentPlan"
                  color="success"
                  :loading="isSaving"
                  :disabled="isGenerating || isSaving"
                  @click="handleSave"
                  block
                >
                  <template v-slot:prepend>
                    <Save :size="20" />
                  </template>
                  Save Lesson
                </v-btn>
              </div>
            </v-form>

            <!-- Selected Profile Info -->
            <v-card-text v-if="selectedProfile" class="mt-4">
              <v-alert
                color="info"
                variant="tonal"
                density="comfortable"
              >
                Lesson will be customized for: {{ selectedProfile.profileName }}
              </v-alert>
            </v-card-text>
          </v-col>

          <!-- Right Column: Lesson Plan Display -->
          <v-col cols="12" md="8">
            <LessonPlanDisplay
              :plan="currentPlan"
              :is-loading="isGenerating"
              :selected-sections="[]"
              :updated-sections="[]"
            />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<style lang="scss" scoped>
.create-lesson-dialog {
  .create-lesson-card {
    border-radius: 8px;
    max-height: 90vh;
    overflow-y: auto;
  }

  .v-card-title {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    letter-spacing: -0.5px;
  }

  .v-form {
    .v-text-field, .v-select {
      :deep(.v-field__input) {
        padding: 8px 16px;
        min-height: 48px;
      }
      
      :deep(.v-field__outline) {
        border-radius: 8px;
      }

      &:focus-within {
        transform: scale(1.01);
        transition: transform 0.2s ease;
      }
    }
  }

  .v-btn {
    text-transform: none;
    letter-spacing: 0.5px;
    font-weight: 500;
    height: 44px;
    transition: all 0.3s ease;

    &:not(.v-btn--disabled) {
      &:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      }
    }
  }

  .v-alert {
    border-radius: 8px;
    
    :deep(.v-alert__content) {
      font-size: 0.875rem;
    }
  }

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
}

@media (max-width: 960px) {
  .create-lesson-dialog {
    margin: 12px;

    .v-card-text {
      padding: 12px !important;
    }

    .v-form {
      .v-text-field, .v-select {
        :deep(.v-field__input) {
          min-height: 44px;
        }
      }
    }

    .v-btn {
      height: 40px;
    }
  }
}

:deep(.v-theme--dark) {
  .create-lesson-dialog {
    .create-lesson-card {
      background-color: rgb(var(--v-theme-surface));
    }

    ::-webkit-scrollbar-thumb {
      background: rgba(var(--v-theme-primary), 0.3);
      
      &:hover {
        background: rgba(var(--v-theme-primary), 0.5);
      }
    }
  }
}
</style>