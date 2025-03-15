<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import { usePlanStore } from '@/stores/plans';
import type { PlanVersion } from '@/services/planService';

const props = defineProps<{
  modelValue: boolean;
  planId?: string;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
  (e: 'select-version', version: PlanVersion): void;
}>();

const planStore = usePlanStore();
const { planVersions, totalVersions } = planStore;

// Computed properties
const dialog = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

// Format date for display
const formatDate = (dateString: string) => {
  if (!dateString) return '';
  
  try {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: 'numeric',
    }).format(date);
  } catch (e) {
    console.error('Error formatting date:', e);
    return dateString;
  }
};

// Handle version selection
const handleSelectVersion = (version: PlanVersion) => {
  emit('select-version', version);
};

// Close dialog
const handleClose = () => {
  dialog.value = false;
};
</script>

<template>
  <v-dialog v-model="dialog" max-width="600px">
    <v-card>
      <v-card-title class="text-h5 pa-4">Plan Version History</v-card-title>
      
      <v-card-text class="pa-0">
        <v-list v-if="planVersions.length" lines="two" class="version-list">
          <v-list-item
            v-for="version in planVersions"
            :key="`${version.planId}-${version.version}`"
            @click="handleSelectVersion(version)"
            class="version-item"
          >
            <template v-slot:prepend>
              <v-icon icon="mdi-history" color="grey"></v-icon>
            </template>
            
            <v-list-item-title>
              Version {{ version.version }}
            </v-list-item-title>
            
            <v-list-item-subtitle>
              <div class="d-flex align-center mt-1">
                <span class="text-caption text-grey">{{ formatDate(version.timestamp) }}</span>
              </div>
              <div class="text-caption text-truncate mt-1">
                {{ version.title }}
                <span v-if="version.goal" class="text-grey"> - {{ version.goal }}</span>
              </div>
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>
        
        <div v-else class="d-flex flex-column align-center pa-8">
          <v-icon icon="mdi-history" size="48" color="grey-lighten-1" class="mb-4"></v-icon>
          <span class="text-body-1 text-grey-darken-1">No version history available</span>
          <span class="text-body-2 text-grey">Save changes to create new versions</span>
        </div>
      </v-card-text>
      
      <v-card-actions class="pa-4">
        <v-spacer></v-spacer>
        <v-btn color="grey-darken-1" variant="text" @click="handleClose">
          Close
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style lang="scss" scoped>
.v-card-title {
  font-family: "Museo Moderno", sans-serif;
  font-weight: 600;
  letter-spacing: -0.5px;
  color: #5c6970;
}

.version-list {
  max-height: 400px;
  overflow-y: auto;
  
  .version-item {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    transition: background-color 0.2s ease;
    
    &:hover {
      background-color: rgba(0, 0, 0, 0.02);
    }
  }
}
</style> 