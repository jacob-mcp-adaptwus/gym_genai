<script setup lang="ts">
import { computed } from 'vue';
import { User, Lightbulb, Target } from 'lucide-vue-next';

interface StudentProfile {
  profileName: string;
  adaptations: string[];
  teachingStrategies: string[];
}

interface Props {
  profile: StudentProfile;
}

const props = defineProps<Props>();

// Computed property to format the profile name for display
const formattedProfileName = computed(() => {
  return props.profile.profileName
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
});

// Computed property to categorize teaching strategies
const categorizedStrategies = computed(() => {
  return props.profile.teachingStrategies.map(strategy => {
    const [category, ...details] = strategy.split(':');
    return {
      category: category.trim(),
      details: details.join(':').trim()
    };
  });
});
</script>

# Template Section
<template>
  <section class="student-profile-section">
    <!-- Section Header -->
    <div class="d-flex align-center mb-4">
      <User :size="24" class="text-primary mr-2" />
      <h2 class="text-h5">Student Profile</h2>
    </div>

    <!-- Profile Name Card -->
    <v-card class="mb-4" variant="tonal" color="primary">
      <v-card-text class="d-flex align-center">
        <User :size="20" class="mr-2" />
        <span class="text-h6">{{ formattedProfileName }}</span>
      </v-card-text>
    </v-card>

    <!-- Adaptations -->
    <div class="mb-4">
      <div class="d-flex align-center mb-2">
        <Target :size="20" class="text-primary mr-2" />
        <h3 class="text-h6">Adaptations</h3>
      </div>
      <v-list>
        <v-list-item
          v-for="(adaptation, index) in profile.adaptations"
          :key="index"
          class="adaptation-item"
        >
          <template v-slot:prepend>
            <v-icon color="primary" size="small" class="mr-2">•</v-icon>
          </template>
          {{ adaptation }}
        </v-list-item>
      </v-list>
    </div>

    <!-- Teaching Strategies -->
    <div>
      <div class="d-flex align-center mb-2">
        <Lightbulb :size="20" class="text-primary mr-2" />
        <h3 class="text-h6">Teaching Strategies</h3>
      </div>
      <v-list>
        <v-list-item
          v-for="(strategy, index) in categorizedStrategies"
          :key="index"
          class="strategy-item"
        >
          <v-list-item-title class="font-weight-medium">
            {{ strategy.category }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ strategy.details }}
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.student-profile-section {
  // Section title styling
  .text-h5 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    color: #5C6970;
  }

  .text-h6 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #5C6970;
  }

  // List styling
  .v-list {
    padding: 8px;
    background-color: transparent;

    .v-list-item {
      border-radius: 6px;
      margin-bottom: 4px;
      transition: all 0.2s ease;
      font-family: 'Quicksand', sans-serif;
      
      &:hover {
        background-color: rgba(var(--v-theme-primary), 0.05);
        transform: translateX(4px);
      }

      &-title {
        font-size: 0.95rem;
        line-height: 1.4;
      }

      &-subtitle {
        font-size: 0.875rem;
        opacity: 0.8;
        margin-top: 4px;
      }
    }
  }

  // Profile name card styling
  .v-card {
    border-radius: 8px;
    
    .v-card-text {
      font-family: 'Quicksand', sans-serif;
      font-weight: 500;
      padding: 12px 16px;
    }
  }

  // Dark mode adjustments
  :deep(.v-theme--dark) {
    .v-list-item {
      &:hover {
        background-color: rgba(var(--v-theme-primary), 0.1);
      }
    }
  }
}

// Mobile optimizations
@media (max-width: 600px) {
  .student-profile-section {
    .text-h5 {
      font-size: 1.25rem;
    }

    .text-h6 {
      font-size: 1rem;
    }

    .v-list {
      padding: 4px;

      .v-list-item {
        padding: 8px;
        
        &:hover {
          transform: none;
        }
      }
    }
  }
}
</style>