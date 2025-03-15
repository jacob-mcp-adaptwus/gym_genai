// Script Section
<script setup lang="ts">
// Script Section of LessonPlanDisplay.vue
import { defineProps, computed, watch, ref, onMounted } from 'vue';
import { BookOpen, Clock, GraduationCap, Brain } from 'lucide-vue-next';
import type { LessonPlan } from '@/services/lessonService';

// Subcomponents
import LessonPedagogicalContext from '@/components/apps/lessons/LessonSections/LessonPedagogicalContext.vue';
import LessonObjectives from '@/components/apps/lessons/LessonSections/LessonObjectives.vue';
import LessonFlow from '@/components/apps/lessons/LessonSections/LessonFlow.vue';
import LessonProblemSets from '@/components/apps/lessons/LessonSections/LessonProblemSets.vue';
import LessonProblemSetsBelowGradeLevel from '@/components/apps/lessons/LessonSections/LessonProblemSetsBelowGradeLevel.vue';
import LessonProblemSetsAboveGradeLevel from '@/components/apps/lessons/LessonSections/LessonProblemSetsAboveGradeLevel.vue';
import LessonAssessments from '@/components/apps/lessons/LessonSections/LessonAssessments.vue';
import LessonAccessibility from '@/components/apps/lessons/LessonSections/LessonAccessibility.vue';
import LessonStudentProfile from '@/components/apps/lessons/LessonSections/LessonStudentProfile.vue';
import LessonMetadata from '@/components/apps/lessons/LessonSections/LessonMetadata.vue';

interface Props {
  plan: LessonPlan | null;
  isLoading?: boolean;
  version?: number;
  lastModified?: string;
  profileId?: string;
  selectedSections: string[];
  updatedSections: string[];
}

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: 'section-select', section: string): void;
  (e: 'update:updatedComponents', componentName: string): void;
}>();

// Local reactive copy of the plan
const localPlan = ref<LessonPlan | null>(null);

// Watch for plan changes with deep comparison
watch(() => props.plan, (newPlan) => {
  if (newPlan !== null) {
    // Create new reference to force reactivity
    localPlan.value = JSON.parse(JSON.stringify(newPlan));
    console.log('Plan updated in LessonPlanDisplay:', newPlan);
  } else {
    localPlan.value = null;
  }
}, { immediate: true, deep: true });

// Computed property to check if we have a valid plan
const hasPlan = computed(() => {
  return localPlan.value !== null && typeof localPlan.value === 'object';
});

// Format the timestamp
const formattedTimestamp = computed(() => {
  if (!props.lastModified) return '';
  
  return new Date(props.lastModified).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
});

// Format version display
const versionDisplay = computed(() => {
  if (typeof props.version === 'undefined') return '';
  return `v${props.version}`;
});

// Method to get subject-specific colors
const getSubjectColor = computed(() => {
  if (!localPlan.value?.metadata?.subject) return 'primary';
  
  const subjectColors: Record<string, string> = {
    'Math': 'blue',
    'Science': 'green',
    'English': 'purple',
    'History': 'orange',
    'Art': 'pink',
    'Music': 'deep-purple',
    'Physical Education': 'red',
  };
  
  return subjectColors[localPlan.value.metadata.subject] || 'primary';
});

// Format duration helper
const formatDuration = (duration: string): string => {
  if (!duration) return '';
  
  if (duration.includes('min') || duration.includes('hour')) {
    return duration;
  }
  
  return `${duration} minutes`;
};

// Debug mounted hook
onMounted(() => {
  console.log('LessonPlanDisplay mounted with plan:', props.plan);
});

// Add method to handle section selection
const toggleSection = (section: string) => {
  emit('section-select', section);
};

// Add method to track updates
const trackUpdate = (componentName: string) => {
  emit('update:updatedComponents', componentName);
};

</script>



# Template Section
<template>
  <v-card elevation="1" v-if="hasPlan" class="lesson-plan-card position-relative">
    <!-- Loading Overlay -->
    <v-overlay
      :model-value="isLoading"
      contained
      class="align-center justify-center"
      persistent
      scrim="white"
    >
      <v-card-text class="text-center">
        <v-progress-circular
          indeterminate
          color="primary"
          size="64"
        ></v-progress-circular>
        <div class="text-h6 mt-4">Updating Lesson Plan...</div>
      </v-card-text>
    </v-overlay>

    <!-- Header Section with Metadata -->
    <v-card-title class="d-flex flex-column py-4 px-4">
      <!-- Title Row -->
      <div class="d-flex align-center flex-grow-1 mb-3">
        <BookOpen class="mr-2" :size="24" />
        <span class="text-h5">{{ plan?.metadata?.topic }}</span>
      </div>

      <!-- Primary Tags Row -->


      <!-- Version Info -->
      <div v-if="versionDisplay || formattedTimestamp" class="d-flex flex-wrap gap-2">
        <v-chip v-if="versionDisplay" size="small" color="secondary">
          {{ versionDisplay }}
        </v-chip>
        <v-chip v-if="formattedTimestamp" size="small" color="primary">
          {{ formattedTimestamp }}
        </v-chip>
      </div>
    </v-card-title>

    <v-divider></v-divider>

    <!-- Main Content Sections -->
    <v-card-text class="pa-4">
      <div class="section-container">
        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('metadata'),
            'selected': selectedSections.includes('metadata')
          }"
          @click="toggleSection('metadata')"
        >
          <LessonMetadata 
            v-if="plan?.metadata"
            :metadata="plan.metadata"
            :total_duration="plan.total_duration"
            @update="() => trackUpdate('metadata')"
          />
        </div>
        
        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('pedagogicalContext'),
            'selected': selectedSections.includes('pedagogicalContext')
          }"
          @click="toggleSection('pedagogicalContext')"
        >
          <LessonPedagogicalContext 
            v-if="plan?.pedagogicalContext"
            :context="plan.pedagogicalContext"
            @update="() => trackUpdate('pedagogicalContext')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('objectives'),
            'selected': selectedSections.includes('objectives')
          }"
          @click="toggleSection('objectives')"
        >
          <LessonObjectives 
            v-if="plan?.objectives"
            :objectives="plan.objectives"
            @update="() => trackUpdate('objectives')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('lessonFlow'),
            'selected': selectedSections.includes('lessonFlow')
          }"
          @click="toggleSection('lessonFlow')"
        >
          <LessonFlow 
            v-if="plan?.lessonFlow"
            :flow="plan.lessonFlow"
            @update="() => trackUpdate('lessonFlow')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('markupProblemSetsBelowGradeLevel'),
            'selected': selectedSections.includes('markupProblemSetsBelowGradeLevel')
          }"
          @click="toggleSection('markupProblemSetsBelowGradeLevel')"
        >
          <LessonProblemSetsBelowGradeLevel 
            v-if="plan?.markupProblemSetsBelowGradeLevel"
            :problemSets="plan.markupProblemSetsBelowGradeLevel"
            @update="() => trackUpdate('markupProblemSetsBelowGradeLevel')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('markupProblemSets'),
            'selected': selectedSections.includes('markupProblemSets')
          }"
          @click="toggleSection('markupProblemSets')"
        >
          <LessonProblemSets 
            v-if="plan?.markupProblemSets"
            :problemSets="plan.markupProblemSets"
            @update="() => trackUpdate('markupProblemSets')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('markupProblemSetsAboveGradeLevel'),
            'selected': selectedSections.includes('markupProblemSetsAboveGradeLevel')
          }"
          @click="toggleSection('markupProblemSetsAboveGradeLevel')"
        >
          <LessonProblemSetsAboveGradeLevel 
            v-if="plan?.markupProblemSetsAboveGradeLevel"
            :problemSets="plan.markupProblemSetsAboveGradeLevel"
            @update="() => trackUpdate('markupProblemSetsAboveGradeLevel')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('assessments'),
            'selected': selectedSections.includes('assessments')
          }"
          @click="toggleSection('assessments')"
        >
          <LessonAssessments 
            v-if="plan?.assessments"
            :assessments="plan.assessments"
            @update="() => trackUpdate('assessments')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('accessibility'),
            'selected': selectedSections.includes('accessibility')
          }"
          @click="toggleSection('accessibility')"
        >
          <LessonAccessibility 
            v-if="plan?.accessibility"
            :accessibility="plan.accessibility"
            @update="() => trackUpdate('accessibility')"
          />
        </div>

        <div 
          class="section-wrapper"
          :class="{
            'updated': updatedSections.includes('studentProfile'),
            'selected': selectedSections.includes('studentProfile')
          }"
          @click="toggleSection('studentProfile')"
        >
          <LessonStudentProfile 
            v-if="plan?.studentProfile"
            :profile="plan.studentProfile"
            @update="() => trackUpdate('studentProfile')"
          />
        </div>
      </div>
    </v-card-text>
  </v-card>

  <!-- Empty State -->
  <v-card v-else elevation="1" class="empty-state-card">
    <div class="text-center">
      <BookOpen :size="64" class="mb-4 text-primary" />
      <h3 class="text-h5 mb-2">No Lesson Plan Generated Yet</h3>
      <p class="text-medium-emphasis">
        Enter a topic and click Generate to create a new lesson plan
      </p>
    </div>
  </v-card>
</template>

# Style Section
<style lang="scss" scoped>
.lesson-plan-card {
  background-color: rgb(var(--v-theme-background));
  border-radius: 8px;
  transition: all 0.3s ease;

  .v-card-title {
    font-family: 'Museo Moderno', sans-serif;
    
    .text-h5 {
      font-weight: 600;
      letter-spacing: -0.5px;
      line-height: 1.3;
    }
  }

  .v-chip {
    font-family: 'Quicksand', sans-serif;
    font-size: 0.875rem;
    
    &.v-chip--size-small {
      height: 24px;
    }
  }
}

.section-container {
  > :deep(*) {
    margin-bottom: 32px;
    padding-bottom: 32px;
    border-bottom: 1px solid rgba(var(--v-theme-on-surface), 0.12);
    
    &:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }
  }
}

.empty-state-card {
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px;
  
  .text-h5 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
  }
  
  p {
    font-family: 'Quicksand', sans-serif;
    opacity: 0.75;
  }
}

.v-overlay {
  backdrop-filter: blur(4px);
  
  .v-card-text {
    background: transparent;
    padding: 32px;
    
    .text-h6 {
      font-family: 'Museo Moderno', sans-serif;
      color: rgb(var(--v-theme-primary));
    }
  }
}

:deep(.v-theme--dark) {
  .lesson-plan-card {
    background-color: rgb(var(--v-theme-surface));
  }
}

@media (max-width: 960px) {
  .lesson-plan-card {
    .v-card-title {
      padding: 16px;
      
      .text-h5 {
        font-size: 1.25rem;
      }
    }
  }
  
  .empty-state-card {
    padding: 24px;
    min-height: 300px;
    
    .text-h5 {
      font-size: 1.25rem;
    }
  }
}

.section-wrapper {
  position: relative;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: all 0.2s ease;
  border: 2px solid transparent;

  &:hover {
    background-color: rgba(var(--v-theme-primary), 0.05);
  }

  // Selected state (lower priority)
  &.selected:not(.updated) { // Only apply if not updated
    background-color: rgba(var(--v-theme-primary), 0.1);
    border: 2px solid rgb(var(--v-theme-primary));
  }

  // Updated state (higher priority)
  &.updated {
    border: 2px solid #FF9800 !important;
    background-color: rgba(255, 152, 0, 0.05) !important;
    animation: highlightUpdate 0.5s ease-in-out;
  }

  // Selected checkmark (only show if not updated)
  &.selected:not(.updated)::before {
    content: '✓';
    position: absolute;
    top: 8px;
    right: 8px;
    color: rgb(var(--v-theme-primary));
    font-weight: bold;
  }

  // Updated star (always show if updated)
  &.updated::after {
    content: '★';
    position: absolute;
    top: 8px;
    right: 8px;
    color: #FF9800;
    font-weight: bold;
  }
}

@keyframes highlightUpdate {
  0% {
    background-color: rgba(255, 152, 0, 0.2);
  }
  100% {
    background-color: rgba(255, 152, 0, 0.05);
  }
}
</style>