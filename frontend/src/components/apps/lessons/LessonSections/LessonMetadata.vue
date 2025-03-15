<script setup lang="ts">
import { BookOpen, GraduationCap, Brain, Clock, Target, User } from 'lucide-vue-next';
import { computed } from 'vue';

interface Standard {
  code: string;
  description: string;
}

interface Props {
  metadata: {
    topic: string;
    grade: string;
    subject: string;
    lastModified: string;
    standardsAddressed: {
      focalStandard: string[];
      supportingStandards: string[];
    };
    profileName?: string;
  };
  total_duration?: string;
}

const props = defineProps<Props>();

// Parse standards into code and description
const parseStandard = (standard: string): Standard => {
  const [code, ...descParts] = standard.split(':');
  return {
    code: code.trim(),
    description: descParts.join(':').trim()
  };
};

const focalStandards = computed(() => 
  props.metadata.standardsAddressed.focalStandard.map(parseStandard)
);

const supportingStandards = computed(() => 
  props.metadata.standardsAddressed.supportingStandards.map(parseStandard)
);

// Format duration helper
const formatDuration = (duration: string): string => {
  if (!duration) return '';
  return duration.includes('min') || duration.includes('hour') 
    ? duration 
    : `${duration} minutes`;
};
</script>

<template>
  <div class="lesson-metadata">
    <!-- Primary Metadata Tags -->
    <div class="d-flex flex-wrap gap-2 mb-4">
      <v-chip
        color="primary"
        class="d-flex align-center"
      >
        <GraduationCap class="mr-1" :size="16" />
        {{ metadata.grade }}
      </v-chip>
      <v-chip
        color="info"
      >
        <Brain class="mr-1" :size="16" />
        {{ metadata.subject }}
      </v-chip>
      <v-chip
        color="info"
        v-if="total_duration"
      >
        <Clock class="mr-1" :size="16" />
        {{ formatDuration(total_duration) }}
      </v-chip>
      <v-chip
        v-if="metadata.profileName"
        color="secondary"
      >
        <User class="mr-1" :size="16" />
        {{ metadata.profileName }}
      </v-chip>
    </div>

    <!-- Standards Section -->
    <div class="standards-section">
      <div class="d-flex align-center mb-2">
        <Target :size="20" class="mr-2" />
        <span class="text-h6">Standards</span>
      </div>
      
      <!-- Focal Standards -->
      <div class="standards-list mb-3">
        <v-tooltip
          v-for="standard in focalStandards"
          :key="standard.code"
          :text="standard.description"
          location="top"
        >
          <template v-slot:activator="{ props }">
            <v-chip
              class="standard-chip ma-1"
              color="primary"
              v-bind="props"
            >
              {{ standard.code }}
            </v-chip>
          </template>
        </v-tooltip>
      </div>

      <!-- Supporting Standards -->
      <div class="standards-list">
        <v-tooltip
          v-for="standard in supportingStandards"
          :key="standard.code"
          :text="standard.description"
          location="top"
        >
          <template v-slot:activator="{ props }">
            <v-chip
              class="standard-chip ma-1"
              color="secondary"
              variant="outlined"
              v-bind="props"
            >
              {{ standard.code }}
            </v-chip>
          </template>
        </v-tooltip>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.lesson-metadata {
  .text-h6 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    letter-spacing: -0.3px;
  }

  .standards-section {
    .standards-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .standard-chip {
      font-family: 'Quicksand', sans-serif;
      font-weight: 500;
      cursor: help;
      transition: transform 0.2s ease;
      
      &:hover {
        transform: translateY(-2px);
      }
    }
  }
}

@media (max-width: 600px) {
  .lesson-metadata {
    .text-h6 {
      font-size: 1rem;
    }
  }
}
</style> 