<script setup lang="ts">
import { ref, computed } from 'vue';
import { usePlanStore } from '@/stores/plans';
import type { Plan } from '@/services/planService';

const props = defineProps<{
  modelValue: boolean;
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
  (e: 'plan-created', plan: Plan): void;
}>();

const planStore = usePlanStore();

// Form data
const title = ref('');
const goal = ref('');
const experience = ref('');
const isSubmitting = ref(false);
const error = ref('');

// Form validation
const titleRules = [
  (v: string) => !!v || 'Title is required',
  (v: string) => (v && v.length <= 100) || 'Title must be less than 100 characters',
];

const goalRules = [
  (v: string) => (v && v.length <= 200) || 'Goal must be less than 200 characters',
];

const experienceOptions = [
  { value: 'beginner', text: 'Beginner' },
  { value: 'intermediate', text: 'Intermediate' },
  { value: 'advanced', text: 'Advanced' },
  { value: 'elite', text: 'Elite' },
];

// Computed properties
const dialog = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

const isFormValid = computed(() => {
  return !!title.value;
});

// Methods
const resetForm = () => {
  title.value = '';
  goal.value = '';
  experience.value = '';
  error.value = '';
};

const handleClose = () => {
  resetForm();
  dialog.value = false;
};

const handleSubmit = async () => {
  if (!isFormValid.value) return;

  isSubmitting.value = true;
  error.value = '';

  try {
    const plan = await planStore.generatePlan({
      title: title.value,
      goal: goal.value,
      experience: experience.value,
    });

    emit('plan-created', plan);
    handleClose();
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to create plan';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <v-dialog v-model="dialog" max-width="600px" persistent>
    <v-card>
      <v-card-title class="text-h5 pa-4">Create New Workout Plan</v-card-title>
      
      <v-card-text class="pa-4">
        <v-alert v-if="error" type="error" class="mb-4">{{ error }}</v-alert>
        
        <v-form @submit.prevent="handleSubmit">
          <v-text-field
            v-model="title"
            label="Plan Title"
            :rules="titleRules"
            required
            variant="outlined"
            class="mb-4"
          ></v-text-field>
          
          <v-textarea
            v-model="goal"
            label="Primary Goal"
            :rules="goalRules"
            variant="outlined"
            class="mb-4"
            hint="What do you want to achieve with this plan? (e.g., Muscle gain, Fat loss, Competition prep)"
            persistent-hint
          ></v-textarea>
          
          <v-select
            v-model="experience"
            label="Experience Level"
            :items="experienceOptions"
            item-title="text"
            item-value="value"
            variant="outlined"
            class="mb-4"
          ></v-select>
        </v-form>
      </v-card-text>
      
      <v-card-actions class="pa-4">
        <v-spacer></v-spacer>
        <v-btn
          color="grey-darken-1"
          variant="text"
          @click="handleClose"
          :disabled="isSubmitting"
        >
          Cancel
        </v-btn>
        <v-btn
          color="primary"
          @click="handleSubmit"
          :loading="isSubmitting"
          :disabled="!isFormValid || isSubmitting"
        >
          Create Plan
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

.v-btn {
  font-family: "Quicksand", sans-serif;
  font-weight: 600;
  text-transform: none;
  letter-spacing: 0.5px;
}
</style> 