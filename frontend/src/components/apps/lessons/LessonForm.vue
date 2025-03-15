<script setup lang="ts">
import { ref, defineEmits, onMounted, computed, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useProfileStore } from '@/stores/profiles';
import type { Profile } from '@/services/profileService';
import { User, BookOpen, RefreshCw, Save } from 'lucide-vue-next';

interface Props {
  isGenerating?: boolean;
  hasCurrentPlan?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  isGenerating: false,
  hasCurrentPlan: false
});

const emit = defineEmits<{
  (e: 'generate', topic: string, selectedProfile: Profile | null): void;
  (e: 'reset'): void;
  (e: 'save'): void;
}>();

const topic = ref('');
const selectedProfile = ref<Profile | null>(null);
const error = ref<string | null>(null);
const hasInitialPlan = ref(false);

// Profile store integration
const profileStore = useProfileStore();
const { isLoading } = storeToRefs(profileStore);

// Get active profiles with proper typing
const activeProfiles = computed(() => {
  console.log('All profiles:', profileStore.getSortedProfiles);
  const filtered = profileStore.getSortedProfiles.filter(profile => profile.active);
  console.log('Filtered active profiles:', filtered);
  return filtered;
});

// Watch for profile changes
watch(() => activeProfiles.value, (newProfiles) => {
  console.log('Active profiles updated:', newProfiles);
  // Reset selected profile if it's no longer in the active profiles
  if (selectedProfile.value && !newProfiles.find(p => p.profileName === selectedProfile.value?.profileName)) {
    selectedProfile.value = null;
  }
}, { immediate: true });

onMounted(async () => {
  try {
    // Check if profiles are already loaded
    if (profileStore.getSortedProfiles.length === 0) {
      console.log('Fetching profiles...');
      await profileStore.fetchProfiles();
    } else {
      console.log('Profiles already loaded:', profileStore.getSortedProfiles);
    }
  } catch (err) {
    console.error('Error fetching profiles:', err);
    error.value = err instanceof Error ? err.message : 'Failed to fetch profiles';
  }
});

const validateAndGenerate = () => {
  if (!topic.value.trim()) {
    error.value = 'Please enter a topic';
    return;
  }
  error.value = null;
  hasInitialPlan.value = true;
  emit('generate', topic.value, selectedProfile.value);
};

const resetForm = () => {
  topic.value = '';
  selectedProfile.value = null;
  error.value = null;
  hasInitialPlan.value = false;
  emit('reset');
};

const handleProfileSelect = (profile: Profile | null) => {
  console.log('Profile selected:', profile);
  selectedProfile.value = profile;
};



</script>
# Template Section
<template>
  <v-card class="mb-4" elevation="1">
    <v-card-title class="text-h5 py-4 px-4">
      Lesson Plan Generator
    </v-card-title>
    
    <v-card-text>
      <v-form @submit.prevent="validateAndGenerate">
        <!-- Topic Input -->
        <v-text-field
          v-model="topic"
          label="Lesson Topic"
          :error-messages="error"
          required
          variant="outlined"
          placeholder="Enter the topic for your lesson"
          class="mb-4"
        ></v-text-field>

        <!-- Profile Selection -->
        <v-select
          v-model="selectedProfile"
          :items="activeProfiles"
          item-title="profileName"
          label="Select Student Profile"
          variant="outlined"
          class="mb-4"
          :loading="isLoading"
          :disabled="isLoading || props.isGenerating"
          clearable
          return-object
          @update:model-value="handleProfileSelect"
          :menu-props="{ maxHeight: 400 }"
          persistent-placeholder
        >
          <!-- Header Item -->
          <template v-slot:prepend-item>
            <v-list-item
              :title="activeProfiles.length ? 'Choose a profile' : 'No active profiles'"
              :subtitle="activeProfiles.length ? 'Customize lesson for specific student' : 'Create profiles in My Profiles'"
              density="compact"
              class="text-primary"
            >
              <template v-slot:prepend>
                <BookOpen class="mr-2" :size="20" />
              </template>
            </v-list-item>
            <v-divider class="mt-2"></v-divider>
          </template>

          <!-- Profile Item Template -->
          <template v-slot:item="{ props: itemProps, item }">
            <v-list-item v-bind="itemProps">
              <template v-slot:prepend>
                <User :size="20" class="mr-2" />
              </template>
              <v-list-item-title>{{ item.raw.profileName }}</v-list-item-title>
              <v-list-item-subtitle class="text-caption">
                {{ item.raw.demographics }}
              </v-list-item-subtitle>
            </v-list-item>
          </template>

          <!-- Selected Item Display -->
          <template v-slot:selection="{ item }">
            <v-chip
              color="primary"
              variant="flat"
              class="mr-2"
              size="small"
            >
              <template v-slot:prepend>
                <User :size="16" />
              </template>
              {{ item.raw.profileName }}
            </v-chip>
          </template>

          <!-- No Data Message -->
          <template v-slot:no-data>
            <v-list-item
              title="No Active Profiles"
              subtitle="Create profiles in My Profiles section"
            >
              <template v-slot:prepend>
                <User :size="20" class="mr-2" />
              </template>
            </v-list-item>
          </template>
        </v-select>

        <div class="d-flex flex-column gap-3">
          <!-- Generate Plan button -->
          <v-btn
            v-if="!props.hasCurrentPlan && !hasInitialPlan"
            color="primary"
            :loading="props.isGenerating"
            :disabled="!topic.trim() || props.isGenerating"
            @click="validateAndGenerate"
            block
          >
            <template v-slot:prepend>
              <BookOpen :size="20" />
            </template>
            Generate Plan
          </v-btn>

          <!-- Reset Button -->
          <v-btn
            color="secondary"
            variant="outlined"
            @click="resetForm"
            :disabled="props.isGenerating"
            block
          >
            <template v-slot:prepend>
              <RefreshCw :size="20" />
            </template>
            Reset
          </v-btn>

          <!-- Save Button -->
          <v-btn
            v-if="props.hasCurrentPlan"
            color="success"
            variant="outlined"
            @click="$emit('save')"
            :disabled="props.isGenerating"
            block
          >
            <template v-slot:prepend>
              <Save :size="20" />
            </template>
            Save Plan
          </v-btn>
        </div>
      </v-form>
    </v-card-text>

    <!-- Helper Text for Profile Selection -->
    <v-card-text v-if="selectedProfile" class="pt-0">
      <v-alert
        color="info"
        variant="tonal"
        density="comfortable"
      >
        <template v-slot:prepend>
          <User :size="20" />
        </template>
        Lesson will be customized for: {{ selectedProfile.profileName }}
      </v-alert>
    </v-card-text>
  </v-card>
</template>

# Style Section
<style lang="scss" scoped>
// Card base styles
.v-card {
  transition: all 0.3s ease;
  border-radius: 8px;
  overflow: visible; // Allow dropdown to extend outside card

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  // Card title styles
  .v-card-title {
    font-weight: 600;
    letter-spacing: -0.5px;
  }
}

// Form field base styles
.v-text-field,
.v-select {
  :deep(.v-field__input) {
    padding: 8px 16px;
    min-height: 48px;
  }
  
  :deep(.v-field__outline) {
    border-radius: 8px;
  }

  // Form field focus animations
  :deep(.v-field) {
    transition: transform 0.2s ease;
    
    &:focus-within {
      transform: scale(1.01);
    }
  }

  // Error state
  &.error--text {
    :deep(.v-field__outline) {
      border-color: rgb(var(--v-theme-error));
    }
  }
}

// Profile select specific styles
.v-select {
  :deep(.v-field__append-inner) {
    padding-top: 6px;
  }

  // Dropdown list styles
  :deep(.v-list) {
    padding: 8px;
    border-radius: 8px;
    
    .v-list-item {
      min-height: 48px;
      padding: 8px 16px;
      margin-bottom: 4px;
      border-radius: 6px;
      transition: all 0.2s ease;
      
      &:hover {
        background-color: rgba(var(--v-theme-primary), 0.05);
        transform: translateX(4px);
      }

      &--active {
        background-color: rgba(var(--v-theme-primary), 0.1);
        
        &:hover {
          background-color: rgba(var(--v-theme-primary), 0.15);
        }
      }

      &__title {
        font-weight: 500;
        font-size: 0.95rem;
        line-height: 1.4;
      }

      &__subtitle {
        font-size: 0.75rem;
        opacity: 0.7;
        margin-top: 2px;
      }
    }
  }

  // Selected value display
  :deep(.v-select__selection) {
    margin: 4px 0;
    
    .v-chip {
      margin: 0;
      font-weight: 500;
      
      &__prepend {
        margin-right: 4px;
      }
    }
  }
}

// Button styles
.v-btn {
  text-transform: none;
  letter-spacing: 0.5px;
  font-weight: 500;
  transition: all 0.3s ease;
  height: 44px;
  
  &.v-btn--block {
    margin-bottom: 8px;
    
    &:last-child {
      margin-bottom: 0;
    }
  }

  &:not(.v-btn--disabled) {
    &:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
  }

  // Icon alignment
  :deep(.v-btn__prepend) {
    margin-right: 8px;
  }

  // Loading state
  &.v-btn--loading {
    .v-btn__prepend {
      opacity: 0;
    }
  }
}

// Alert styles
.v-alert {
  border-radius: 8px;
  
  :deep(.v-alert__prepend) {
    margin-right: 12px;
    align-self: center;
  }

  :deep(.v-alert__content) {
    font-size: 0.875rem;
  }
}

// Transitions
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

// Mobile optimizations
@media (max-width: 960px) {
  .v-card {
    margin-bottom: 16px;
  }

  .v-text-field,
  .v-select {
    :deep(.v-field__input) {
      min-height: 44px;
    }
  }

  .v-btn {
    height: 40px;
    
    &.v-btn--block {
      margin-bottom: 8px;
    }
  }
  
  .v-select {
    :deep(.v-list-item) {
      min-height: 40px;
      padding: 6px 12px;
    }
  }

  .v-alert {
    margin-top: 12px;
    padding: 12px;
  }
}

// Dark mode optimizations
:deep(.v-theme--dark) {
  .v-card {
    &:hover {
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
  }

  .v-select {
    :deep(.v-list-item:hover) {
      background-color: rgba(var(--v-theme-primary), 0.1);
    }
  }

  .v-btn:not(.v-btn--disabled):hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  }
}
</style>