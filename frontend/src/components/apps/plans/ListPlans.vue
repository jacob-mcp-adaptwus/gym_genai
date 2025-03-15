<script setup lang="ts">
import { ref, computed } from 'vue';
import type { Plan } from '@/services/planService';
import { Trash2 } from 'lucide-vue-next';

const props = defineProps<{
  plans: Plan[];
  selectedPlanId?: string | null;
  isLoading: boolean;
}>();

const emit = defineEmits<{
  (e: 'select-plan', plan: Plan): void;
  (e: 'delete-plan', plan: Plan): void;
}>();

// Search functionality
const searchQuery = ref('');

const filteredPlans = computed(() => {
  if (!searchQuery.value) return props.plans;
  
  const query = searchQuery.value.toLowerCase();
  return props.plans.filter(plan => 
    plan.title.toLowerCase().includes(query) || 
    plan.goal?.toLowerCase().includes(query) ||
    plan.experience?.toLowerCase().includes(query)
  );
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
    }).format(date);
  } catch (e) {
    console.error('Error formatting date:', e);
    return dateString;
  }
};

// Handle plan selection
const handleSelectPlan = (plan: Plan) => {
  emit('select-plan', plan);
};

// Handle plan deletion
const handleDeletePlan = (event: Event, plan: Plan) => {
  event.stopPropagation();
  emit('delete-plan', plan);
};

// Get experience level badge color
const getExperienceBadgeColor = (experience: string) => {
  switch (experience?.toLowerCase()) {
    case 'beginner':
      return 'success';
    case 'intermediate':
      return 'info';
    case 'advanced':
      return 'warning';
    case 'elite':
      return 'error';
    default:
      return 'grey';
  }
};
</script>

<template>
  <div class="list-plans">
    <!-- Search Bar -->
    <div class="search-container pa-4">
      <v-text-field
        v-model="searchQuery"
        density="compact"
        variant="outlined"
        placeholder="Search plans..."
        prepend-inner-icon="mdi-magnify"
        hide-details
        class="search-field"
      ></v-text-field>
    </div>
    
    <!-- Loading State -->
    <div v-if="isLoading" class="d-flex justify-center align-center pa-8">
      <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </div>
    
    <!-- Empty State -->
    <div v-else-if="!plans.length" class="d-flex flex-column align-center pa-8">
      <v-icon icon="mdi-dumbbell" size="48" color="grey-lighten-1" class="mb-4"></v-icon>
      <span class="text-body-1 text-grey-darken-1">No workout plans yet</span>
      <span class="text-body-2 text-grey">Create your first plan to get started</span>
    </div>
    
    <!-- No Search Results -->
    <div v-else-if="!filteredPlans.length" class="d-flex flex-column align-center pa-8">
      <v-icon icon="mdi-text-search" size="48" color="grey-lighten-1" class="mb-4"></v-icon>
      <span class="text-body-1 text-grey-darken-1">No plans match your search</span>
      <span class="text-body-2 text-grey">Try a different search term</span>
    </div>
    
    <!-- Plan List -->
    <v-list v-else lines="two" class="plan-list">
      <v-list-item
        v-for="plan in filteredPlans"
        :key="plan.planId"
        :active="plan.planId === selectedPlanId"
        @click="handleSelectPlan(plan)"
        class="plan-item"
      >
        <template v-slot:prepend>
          <v-icon icon="mdi-dumbbell" :color="plan.planId === selectedPlanId ? 'primary' : 'grey'"></v-icon>
        </template>
        
        <v-list-item-title class="d-flex align-center justify-space-between">
          <span class="text-truncate">{{ plan.title }}</span>
          <v-btn
            icon="mdi-delete"
            size="small"
            variant="text"
            color="grey"
            @click="(e: Event) => handleDeletePlan(e, plan)"
            class="delete-btn"
          >
            <Trash2 :size="18" />
          </v-btn>
        </v-list-item-title>
        
        <v-list-item-subtitle>
          <div class="d-flex align-center mt-1">
            <v-chip
              v-if="plan.experience"
              size="x-small"
              :color="getExperienceBadgeColor(plan.experience)"
              class="mr-2"
              label
            >
              {{ plan.experience }}
            </v-chip>
            <span class="text-caption text-grey">{{ formatDate(plan.lastModified) }}</span>
          </div>
          <div v-if="plan.goal" class="text-caption text-truncate mt-1">
            {{ plan.goal }}
          </div>
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </div>
</template>

<style lang="scss" scoped>
.list-plans {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .search-container {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    
    .search-field {
      font-size: 14px;
    }
  }
  
  .plan-list {
    flex: 1;
    overflow-y: auto;
    
    .plan-item {
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
      transition: background-color 0.2s ease;
      
      &:hover {
        background-color: rgba(0, 0, 0, 0.02);
        
        .delete-btn {
          opacity: 1;
        }
      }
      
      .delete-btn {
        opacity: 0;
        transition: opacity 0.2s ease;
      }
    }
  }
}
</style> 