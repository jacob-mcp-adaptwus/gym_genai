<script setup lang="ts">
import { ref, computed } from 'vue';
import { usePlanStore } from '@/stores/plans';
import { useChatStore } from '@/stores/chats';
import PlanDisplay from '@/components/apps/plans/PlanDisplay.vue';
import PlanChat from '@/components/apps/plans/PlanChat.vue';
import CreatePlan from '@/components/apps/plans/CreatePlan.vue';
import ListPlans from '@/components/apps/plans/ListPlans.vue';
import PlanVersions from '@/components/apps/plans/PlanVersions.vue';
import type { PlanVersion, Plan, WorkoutPlan } from '@/services/planService';
import { Save, History, Download } from 'lucide-vue-next';

const emit = defineEmits<{
  (e: 'analysis-message', message: string): void
}>();

const versionsDialog = ref(false);
const planStore = usePlanStore();
const { isLoading, isSaving } = planStore;
const chatStore = useChatStore();
interface Analysis {
  intent: string;
  rationale: string;
  components: string[];
}

// **State Management**
// Reactive state variables with descriptive comments
const updatedComponents = ref<string[]>([]); // Tracks which components have been updated for UI highlighting
const contextSelected = ref<string[]>([]); // Tracks selected contexts for chat focus
const selectedPlan = ref<Plan | null>(null); // Currently selected plan
const currentPlan = ref<WorkoutPlan | null>(null); // Current workout plan being displayed
const error = ref<string | null>(null); // Error message for display
const createDialog = ref(false); // Controls visibility of create plan dialog
const deleteDialog = ref(false); // Controls visibility of delete confirmation dialog
const planToDelete = ref<Plan | null>(null); // Plan to be deleted
const saveSnackbar = ref(false); // Controls visibility of save snackbar
const saveSnackbarText = ref(''); // Text to display in save snackbar
const saveSnackbarColor = ref('success'); // Color of save snackbar
const chatLoading = ref(false); // Indicates if chat is loading
const hasUnsavedChanges = ref(false); // Indicates if there are unsaved changes
const isDeleting = ref(false); // Indicates if deletion is in progress
const displayLoading = computed(() => 
  planStore.isLoading || chatLoading.value || isDeleting.value
); // Computed property to check if any loading state is active
const planChat = ref<InstanceType<typeof PlanChat> | null>(null); // Reference to PlanChat component
const chatHeight = ref(300); // Added for chat height management

// **Functions**

// Fetches the user's plans from the store
const fetchPlans = async () => {
  try {
    await planStore.fetchUserPlans(); // Fetch user's plans from store
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch plans'; // Set error message
  }
};

const enhanceMessage = (message: string, contexts: string[]): string => {
  if (contexts.length > 0) {
    return message + " with a reference and hyper focus on these components: " + contexts.join(', ');
  }
  return message;
};

// Analyzes the message to determine intent and components to update
const analyzeMessage = async (message: string, plan: WorkoutPlan): Promise<Analysis> => {
  return await chatStore.analyzeMessage(message, JSON.stringify(plan));
};

// Updates the specified components of the workout plan
const updateComponents = async (analysis: Analysis, plan: Plan, message: string, workoutPlan: WorkoutPlan): Promise<void> => {
  const filteredComponents = [...new Set([
    ...analysis.components,
    ...contextSelected.value
  ])];
  console.log('Combined and deduplicated components:', filteredComponents);
  const componentsToUpdate = sortComponentsByPriority(filteredComponents);

  let currentPlanState = JSON.parse(JSON.stringify(workoutPlan)); // Deep copy of the current plan

  for (const component of componentsToUpdate) {
    try {
      const response = await chatStore.sendComponentMessage(
        plan.planId,
        message,
        JSON.stringify(currentPlanState),
        component,
        analysis
      );

      console.log('Response from bodybuildr sendComponentMessage:', response);

      if (response && typeof response === 'object') {
        // Handle the response update
        if ('updatedPlan' in response) {
          currentPlanState = JSON.parse(response.updatedPlan as string);
        } else {
          // Directly update the specific component
          console.log(`Updating specific component: in the currentPlanState ${component}:`, response[component as keyof typeof response]);
          currentPlanState[component] = response[component as keyof typeof response];
          updatedComponents.value.push(component);
        }
        
        currentPlan.value = currentPlanState;
        hasUnsavedChanges.value = true;
      }
    } catch (err) {
      console.error(`Error updating component ${component}:`, err);
    }
  }
};

// Main function to handle chat messages and update the workout plan
const handleChatMessage = async (message: string) => {
  // Early exit if no current plan or selected plan
  if (!currentPlan.value || !selectedPlan.value) return;

  try {
    chatLoading.value = true; // Set loading state

    // Enhance the message with contexts
    const enhancedMessage = enhanceMessage(message, contextSelected.value);
    console.log('Enhanced message:', enhancedMessage);

    // Analyze the enhanced message
    const analysis = await analyzeMessage(enhancedMessage, currentPlan.value);

    // Add analysis to the chat window
    const analysisMessage = `I understand you want to ${analysis.intent}.. ${analysis.rationale}`;
    planChat.value?.addSystemMessage(analysisMessage);

    // Update the components based on the analysis
    console.log('analysis', analysis);
    await updateComponents(analysis, selectedPlan.value, enhancedMessage, currentPlan.value);
  } catch (err) {
    console.error('Error in chat message:', err);
    error.value = err instanceof Error ? err.message : 'An error occurred'; // Set error message
  } finally {
    chatLoading.value = false; // Reset loading state
  }
};

// Handles selecting a plan
const handleSelectPlan = (plan: Plan) => {
  if (!displayLoading.value) {
    console.log('Selecting plan:', plan);
    selectedPlan.value = plan; // Update selected plan
    if (plan.content) {
      try {
        const parsedContent = JSON.parse(plan.content);
        console.log('Parsed content:', parsedContent);
        currentPlan.value = parsedContent; // Set current plan directly
      } catch (err) {
        console.error('Error parsing plan content:', err);
        error.value = 'Error loading plan content'; // Set error message
      }
    } else {
      currentPlan.value = null; // Clear current plan if no content
    }
  }
};

// Handles selecting a plan version
const handleSelectVersion = (version: PlanVersion) => {
  currentPlan.value = JSON.parse(version.content) as WorkoutPlan; // Update current plan with selected version
  versionsDialog.value = false; // Close versions dialog
  hasUnsavedChanges.value = true; // Set unsaved changes flag to true
};

// Fetches and displays plan versions
const handleViewVersions = async (planId: string) => {
  try {
    await planStore.getPlanVersions(planId); // Fetch plan versions
    versionsDialog.value = true; // Open versions dialog
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch versions'; // Set error message
  }
};

// Initiates plan deletion process
const handleDeleteClick = (plan: Plan) => {
  planToDelete.value = plan; // Set plan to be deleted
  deleteDialog.value = true; // Open delete dialog
};

// Confirms and performs plan deletion
const confirmDelete = async () => {
  if (!planToDelete.value?.planId) return;
  
  try {
    isDeleting.value = true; // Set deleting state
    await planStore.deletePlan(planToDelete.value.planId); // Delete plan
    
    if (selectedPlan.value?.planId === planToDelete.value.planId) {
      selectedPlan.value = null; // Clear selected plan if deleted
      currentPlan.value = null; // Clear current plan if deleted
    }
    
    showSnackbar('Plan deleted successfully', 'success');
    deleteDialog.value = false; // Close delete dialog
    planToDelete.value = null; // Clear plan to delete
  } catch (err) {
    showSnackbar(
      err instanceof Error ? err.message : 'Failed to delete plan',
      'error'
    );
  } finally {
    isDeleting.value = false; // Reset deleting state
  }
};

// Function to build plan data for saving
const buildPlanData = (plan: Plan, workoutPlan: WorkoutPlan): Partial<Plan> => {
  return {
    planId: plan.planId,
    title: plan.title,
    goal: workoutPlan.profile?.goals?.primary || '',
    experience: workoutPlan.profile?.experience?.level || '',
    content: JSON.stringify(workoutPlan),
    status: plan.status,
    lastModified: new Date().toISOString()
  };
};

// Saves the current workout plan
const handleSave = async () => {
  // Guard clause: Exit if required data is missing
  if (!selectedPlan.value || !currentPlan.value) {
    console.warn('Cannot save: selectedPlan or currentPlan is missing.');
    return;
  }

  try {
    // Build plan data for saving
    const planData = buildPlanData(selectedPlan.value, currentPlan.value);

    // Save the workout plan via the store
    await planStore.savePlan(planData);

    // Reset local state after successful save
    // Clear any previous error state to ensure UI reflects success
    if (error.value) {
      error.value = null;
    }

    // Notify user of successful save
    showSnackbar('Workout plan saved successfully', 'success');
    hasUnsavedChanges.value = false; // Reset unsaved changes flag
    updatedComponents.value = [];    // Clear updated components list

  } catch (err) {
    // Log error for debugging purposes
    console.error('Error saving workout plan:', err);

    // Notify user of failure
    showSnackbar(
      err instanceof Error ? err.message : 'Failed to save workout plan',
      'error'
    );
  }
};

// Sorts components based on priority order
const sortComponentsByPriority = (
  components: string[],
  priorityOrder: string[] = [
    'profile',
    'workouts',
    'nutrition',
    'supplementation',
    'coachFeedback'
  ]
): string[] => {
  return [...components].sort((a, b) => {
    const aIndex = priorityOrder.indexOf(a);
    const bIndex = priorityOrder.indexOf(b);
    
    // If both components are in priority list, sort by priority order
    if (aIndex !== -1 && bIndex !== -1) {
      return aIndex - bIndex;
    }
    // If only a is in priority list, it comes first
    if (aIndex !== -1) return -1;
    // If only b is in priority list, it comes first
    if (bIndex !== -1) return 1;
    // If neither are in priority list, maintain original order
    return 0;
  });
};

// Handles new plan creation
const handlePlanCreated = (plan: Plan) => {
  showSnackbar('Plan created successfully', 'success');
  fetchPlans(); // Refresh plan list
};

// Displays snackbar notifications
const showSnackbar = (text: string, color: 'success' | 'error' = 'success') => {
  saveSnackbarText.value = text; // Set snackbar text
  saveSnackbarColor.value = color; // Set snackbar color
  saveSnackbar.value = true; // Show snackbar
};

// Closes snackbar and clears save status
const handleCloseSnackbar = () => {
  saveSnackbar.value = false; // Hide snackbar
  planStore.clearSaveStatus(); // Clear save status in store
};

// Downloads the current workout plan as HTML
const handleDownload = () => {
  if (!currentPlan.value || !selectedPlan.value) return;
  
  const planElement = document.querySelector('.plan-card');
  if (!planElement) return;

  const htmlContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>${selectedPlan.value.title} - Workout Plan</title>
    <link href="https://fonts.googleapis.com/css2?family=Museo+Moderno:wght@600&family=Quicksand:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Quicksand', sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .plan-card {
            background: white;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
        }

        /* Section Cards */
        .section-card {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            margin-bottom: 24px;
            background: white;
        }

        .v-card-title {
            background-color: rgba(120, 192, 229, 0.05);
            padding: 16px;
            font-family: 'Quicksand', sans-serif;
            font-weight: 600;
            font-size: 1.1rem;
            color: #5C6970;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #e0e0e0;
        }

        .v-card-text {
            padding: 16px;
        }

        /* Content Sections */
        .content-section {
            margin-bottom: 24px;
            padding: 16px;
        }

        .content-section:last-child {
            margin-bottom: 0;
        }

        .section-title {
            font-family: 'Museo Moderno', sans-serif;
            font-size: 1.1rem;
            color: #5C6970;
            margin-bottom: 12px;
            font-weight: 600;
        }

        /* Metadata Display */
        .metadata-display {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 24px;
        }

        .metadata-item {
            background: #f8f9fa;
            padding: 12px;
            border-radius: 8px;
        }

        /* Print Optimization */
        @media print {
            body {
                background: white;
                padding: 0;
            }

            .plan-card {
                box-shadow: none;
                padding: 20px;
            }

            .section-card {
                break-inside: avoid;
                border: 1px solid #e0e0e0;
            }

            .info-card {
                break-inside: avoid;
            }

            table {
                break-inside: avoid;
            }

            @page {
                margin: 2cm;
                size: A4;
            }
        }

        /* Fix Vuetify-specific classes */
        .d-flex { display: flex; }
        .align-center { align-items: center; }
        .justify-space-between { justify-content: space-between; }
        .flex-grow-1 { flex-grow: 1; }
        .gap-2 { gap: 8px; }
        .mb-4 { margin-bottom: 16px; }
        .mr-2 { margin-right: 8px; }
    </style>
</head>
<body>
    ${planElement.outerHTML}
</body>
</html>`;

  const blob = new Blob([htmlContent], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `${selectedPlan.value.title.toLowerCase().replace(/\s+/g, '_')}_workout_plan.html`;
  link.click();
  URL.revokeObjectURL(url);
};

// Toggles selection of workout plan sections for chat context
const handleSectionSelect = (section: string) => {
  const index = contextSelected.value.indexOf(section);
  if (index === -1) {
    contextSelected.value.push(section); // Add section to selected contexts
  } else {
    contextSelected.value.splice(index, 1); // Remove section from selected contexts
  }
};
</script>

<template>
  <v-container fluid>
    <!-- Chat Component at the Top -->
    <div class="chat-top">
      <div v-if="selectedPlan" class="chat-wrapper" :style="{ height: chatHeight + 'px' }">
        <PlanChat
          ref="planChat"
          :is-generating="chatLoading"
          :initial-message="
            'How would you like to improve this workout plan? ' +
            'I can help you refine specific sections or make general improvements.'
          "
          :selected-contexts="contextSelected"
          @send-message="handleChatMessage"
          @resize="(height: number) => chatHeight = height"
        />
      </div>
    </div>

    <!-- Main Content Below Chat -->
    <v-row>
      <!-- Left Column: Plan List -->
      <v-col cols="12" md="3">
        <v-card elevation="1">
          <v-card-title class="py-4 px-4">
            <span class="text-h5">My Plans</span>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              size="small"
              @click="createDialog = true"
              class="create-button"
            >
              <template v-slot:prepend>
                <span class="text-h6">+</span>
              </template>
              New Plan
            </v-btn>
          </v-card-title>
          <ListPlans
            :plans="planStore.getSortedPlans"
            :selected-plan-id="selectedPlan?.planId"
            :is-loading="planStore.isLoading"
            @select-plan="handleSelectPlan"
            @delete-plan="handleDeleteClick"
          />
        </v-card>
      </v-col>

      <!-- Right Column: Workout Plan Display -->
      <v-col cols="12" md="9">
        <div class="d-flex flex-column h-100">
          <!-- Save Changes Notification -->
          <v-slide-y-transition>
            <v-card
              v-if="hasUnsavedChanges"
              class="mb-4"
              color="warning"
              variant="tonal"
            >
              <v-card-text class="d-flex align-center">
                <span class="flex-grow-1 text-body-1">You have unsaved changes</span>
                <v-btn
                  color="warning"
                  @click="handleSave"
                  :loading="planStore.isSaving"
                  :disabled="planStore.isSaving"
                >
                  <template v-slot:prepend>
                    <Save :size="20" />
                  </template>
                  Save Changes
                </v-btn>
              </v-card-text>
            </v-card>
          </v-slide-y-transition>

          <div class="d-flex gap-2 mb-4">
            <v-btn
              v-if="selectedPlan"
              color="info"
              variant="text"
              @click="handleViewVersions(selectedPlan.planId)"
            >
              <template v-slot:prepend>
                <History :size="20" />
              </template>
              View Versions
            </v-btn>
            <v-btn
              v-if="selectedPlan && currentPlan"
              color="info"
              variant="text"
              @click="handleDownload"
            >
              <template v-slot:prepend>
                <Download :size="20" />
              </template>
              Download Plan
            </v-btn>
          </div>

          <!-- Workout Plan Display -->
          <PlanDisplay
            :plan="currentPlan"
            :is-loading="chatLoading"
            :selected-sections="contextSelected"
            :updated-sections="updatedComponents"
            @section-select="handleSectionSelect"
            @update:updatedComponents="(component: string) => updatedComponents.push(component)"
          >
            <div v-if="isLoading || !currentPlan" class="loading-skeleton">
              <v-skeleton-loader type="card"></v-skeleton-loader>
              <v-skeleton-loader type="text"></v-skeleton-loader>
              <v-skeleton-loader type="text"></v-skeleton-loader>
              <v-skeleton-loader type="text"></v-skeleton-loader>
              <v-skeleton-loader type="card"></v-skeleton-loader>
              <v-skeleton-loader type="text"></v-skeleton-loader>
              <v-skeleton-loader type="text"></v-skeleton-loader>
            </div>
          </PlanDisplay>
        </div>
      </v-col>
    </v-row>

    <!-- Create Plan Modal -->
    <CreatePlan v-model="createDialog" @plan-created="handlePlanCreated" />

    <!-- Delete Confirmation Dialog -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title class="text-h5 pa-4">Delete Workout Plan</v-card-title>
        <v-card-text class="pa-4">
          Are you sure you want to delete "{{ planToDelete?.title }}"?
          This action cannot be undone.
        </v-card-text>
        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn color="grey-darken-1" variant="text" @click="deleteDialog = false">
            Cancel
          </v-btn>
          <v-btn
            color="error"
            @click="confirmDelete"
            :loading="isDeleting"
            :disabled="isDeleting"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Snackbar -->
    <v-snackbar
      v-model="saveSnackbar"
      :color="saveSnackbarColor"
      :timeout="3000"
      location="top"
    >
      {{ saveSnackbarText }}
      <template v-slot:actions>
        <v-btn color="white" variant="text" @click="handleCloseSnackbar">
          Close
        </v-btn>
      </template>
    </v-snackbar>

    <!-- Versions Dialog -->
    <PlanVersions
      v-model="versionsDialog"
      :plan-id="selectedPlan?.planId"
      @select-version="handleSelectVersion"
    />
  </v-container>
</template>

<style lang="scss" scoped>
// Main container layout styles
.v-container {
  max-width: 1600px;
  margin: 0 auto;
  padding-bottom: 64px;
}

// Card base styles with design system colors
.v-card {
  border-radius: 8px;
  transition: all 0.3s ease;
  background-color: rgb(var(--v-theme-background));
  
  .v-card-title {
    font-family: "Museo Moderno", sans-serif;
    font-weight: 600;
    letter-spacing: -0.5px;
    
    .text-h5 {
      font-size: 22pt;
      color: #5c6970; // Neutral Dark from style guide
    }
  }
}

// Create button styling
.create-button {
  font-family: "Quicksand", sans-serif;
  font-weight: 600;
  text-transform: none;
  letter-spacing: 0.5px;
  background-color: #78c0e5; // Primary color from style guide
  
  &:hover {
    background-color: darken(#78c0e5, 10%);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(120, 192, 229, 0.2);
  }
}

// Save changes notification styling
.v-slide-y-transition-enter-active,
.v-slide-y-transition-leave-active {
  transition: all 0.3s ease;
}

.v-slide-y-transition-enter-from,
.v-slide-y-transition-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

// Dialog and modal styling
.v-dialog {
  .v-card {
    border-radius: 12px;
    overflow: hidden;
  }
}

// Chat component styling
.chat-top {
  margin-bottom: 24px;
  
  .chat-wrapper {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  }
}

// Loading skeleton styling
.loading-skeleton {
  padding: 16px;
  
  .v-skeleton-loader {
    margin-bottom: 16px;
  }
}

// Responsive adjustments
@media (max-width: 960px) {
  .v-container {
    padding: 16px;
  }
  
  .chat-top {
    margin-bottom: 16px;
  }
}
</style> 