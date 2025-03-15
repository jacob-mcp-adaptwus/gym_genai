<script setup lang="ts">
import { ref, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useLessonStore } from '@/stores/lessons';
import { useChatStore } from '@/stores/chats';
import LessonPlanDisplay from '@/components/apps/lessons/LessonPlanDisplay.vue';
import LessonChat from '@/components/apps/lessons/LessonChat.vue';
import CreateLesson from '@/components/apps/lessons/CreateLesson.vue';
import ListLessons from '@/components/apps/lessons/ListLessons.vue';
import LessonVersions from '@/components/apps/lessons/LessonVersions.vue';
import type { LessonVersion, Lesson, LessonPlan } from '@/services/lessonService';
import { Save, History, Download } from 'lucide-vue-next';

const emit = defineEmits<{
  (e: 'analysis-message', message: string): void
}>();

const versionsDialog = ref(false);
const lessonStore = useLessonStore();
const { isLoading, isSaving } = storeToRefs(lessonStore);
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
const selectedLesson = ref<Lesson | null>(null); // Currently selected lesson
const currentPlan = ref<LessonPlan | null>(null); // Current lesson plan being displayed
const error = ref<string | null>(null); // Error message for display
const createDialog = ref(false); // Controls visibility of create lesson dialog
const deleteDialog = ref(false); // Controls visibility of delete confirmation dialog
const lessonToDelete = ref<Lesson | null>(null); // Lesson to be deleted
const saveSnackbar = ref(false); // Controls visibility of save snackbar
const saveSnackbarText = ref(''); // Text to display in save snackbar
const saveSnackbarColor = ref('success'); // Color of save snackbar
const chatLoading = ref(false); // Indicates if chat is loading
const hasUnsavedChanges = ref(false); // Indicates if there are unsaved changes
const isDeleting = ref(false); // Indicates if deletion is in progress
const displayLoading = computed(() => 
  isLoading.value || chatLoading.value || isDeleting.value
); // Computed property to check if any loading state is active
const lessonChat = ref<InstanceType<typeof LessonChat> | null>(null); // Reference to LessonChat component
const chatHeight = ref(300); // Added for chat height management

// **Functions**

// Fetches the user's lessons from the store
const fetchLessons = async () => {
  try {
    await lessonStore.fetchUserLessons(); // Fetch user's lessons from store
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch lessons'; // Set error message
  }
};

const enhanceMessage = (message: string, contexts: string[]): string => {
  if (contexts.length > 0) {
    return message + " with a reference and hyper focus on these components: " + contexts.join(', ');
  }
  return message;
};

// Analyzes the message to determine intent and components to update
const analyzeMessage = async (message: string, plan: LessonPlan): Promise<Analysis> => {
  return await chatStore.analyzeMessage(message, JSON.stringify(plan));
};


// Updates the specified components of the lesson plan
const updateComponents = async (analysis: Analysis, lesson: Lesson, message: string, plan: LessonPlan): Promise<void> => {
  const filteredComponents = [...new Set([
    ...analysis.components,
    ...contextSelected.value
  ])];
  console.log('Combined and deduplicated components:', filteredComponents);
  const componentsToUpdate = sortComponentsByPriority(filteredComponents);

  let currentPlanState = JSON.parse(JSON.stringify(plan)); // Deep copy of the current plan

  for (const component of componentsToUpdate) {
    try {
      const response = await chatStore.sendComponentMessage(
        lesson.lessonId,
        message,
        JSON.stringify(currentPlanState),
        component,
        analysis
      );

      console.log('Response from mathtildas sendComponentMessage :', response);

      if (response && typeof response === 'object') {
        // Handle the response update
        if ('updatedPlan' in response) {
          currentPlanState = JSON.parse(response.updatedPlan as string);
        } else {
          // Directly update the specific component this is having errors
          console.log(`Updating specific  component: in the currentPlanState ${component}:`, response[component as keyof typeof response]);
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

// Main function to handle chat messages and update the lesson plan
const handleChatMessage = async (message: string) => {
  // Early exit if no current plan or selected lesson
  if (!currentPlan.value || !selectedLesson.value) return;

  try {
    chatLoading.value = true; // Set loading state

    // Enhance the message with contexts
    const enhancedMessage = enhanceMessage(message, contextSelected.value);
    console.log('Enhanced message:', enhancedMessage);

    // Analyze the enhanced message
    const analysis = await analyzeMessage(enhancedMessage, currentPlan.value);

    // Add analysis to the chat window
    const analysisMessage = `I understand you want to ${analysis.intent}.. ${analysis.rationale}`;
    lessonChat.value?.addSystemMessage(analysisMessage);

    // Update the components based on the analysis
    console.log('analysis', analysis);
    await updateComponents(analysis, selectedLesson.value, enhancedMessage, currentPlan.value);
  } catch (err) {
    console.error('Error in chat message:', err);
    error.value = err instanceof Error ? err.message : 'An error occurred'; // Set error message
  } finally {
    chatLoading.value = false; // Reset loading state
  }
};

// Handles selecting a lesson
const handleSelectLesson = (lesson: Lesson) => {
  if (!displayLoading.value) {
    console.log('Selecting lesson:', lesson);
    selectedLesson.value = lesson; // Update selected lesson
    if (lesson.content) {
      try {
        const parsedContent = JSON.parse(lesson.content);
        console.log('Parsed content:', parsedContent);
        if (parsedContent.lesson_plan) {
          currentPlan.value = parsedContent.lesson_plan; // Set current plan from lesson content
        } else {
          currentPlan.value = parsedContent; // Set current plan directly
        }
      } catch (err) {
        console.error('Error parsing lesson content:', err);
        error.value = 'Error loading lesson content'; // Set error message
      }
    } else {
      currentPlan.value = null; // Clear current plan if no content
    }
  }
};

// Handles selecting a lesson version
const handleSelectVersion = (version: LessonVersion) => {
  currentPlan.value = JSON.parse(version.content) as LessonPlan; // Update current plan with selected version
  versionsDialog.value = false; // Close versions dialog
  hasUnsavedChanges.value = true; // Set unsaved changes flag to true
};

// Fetches and displays lesson versions
const handleViewVersions = async (lessonId: string) => {
  try {
    await lessonStore.getLessonVersions(lessonId); // Fetch lesson versions
    versionsDialog.value = true; // Open versions dialog
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch versions'; // Set error message
  }
};

// Initiates lesson deletion process
const handleDeleteClick = (lesson: Lesson) => {
  lessonToDelete.value = lesson; // Set lesson to be deleted
  deleteDialog.value = true; // Open delete dialog
};

// Confirms and performs lesson deletion
const confirmDelete = async () => {
  if (!lessonToDelete.value?.lessonId) return;
  
  try {
    isDeleting.value = true; // Set deleting state
    await lessonStore.deleteLesson(lessonToDelete.value.lessonId); // Delete lesson
    
    if (selectedLesson.value?.lessonId === lessonToDelete.value.lessonId) {
      selectedLesson.value = null; // Clear selected lesson if deleted
      currentPlan.value = null; // Clear current plan if deleted
    }
    
    showSnackbar('Lesson deleted successfully', 'success');
    deleteDialog.value = false; // Close delete dialog
    lessonToDelete.value = null; // Clear lesson to delete
  } catch (err) {
    showSnackbar(
      err instanceof Error ? err.message : 'Failed to delete lesson',
      'error'
    );
  } finally {
    isDeleting.value = false; // Reset deleting state
  }
};

// Saves the current lesson plan
// Function to build lesson data for saving
const buildLessonData = (lesson: Lesson, plan: LessonPlan): Partial<Lesson> => {
  return {
    lessonId: lesson.lessonId,
    title: lesson.title,
    subject: lesson.subject,
    grade: lesson.grade,
    duration: plan.total_duration,
    content: JSON.stringify(plan),
    status: lesson.status,
    lastModified: new Date().toISOString()
  };
};

// Saves the current lesson plan
const handleSave = async () => {
  // Guard clause: Exit if required data is missing
  if (!selectedLesson.value || !currentPlan.value) {
    console.warn('Cannot save: selectedLesson or currentPlan is missing.');
    return;
  }

  try {
    // Build lesson data for saving
    const lessonData = buildLessonData(selectedLesson.value, currentPlan.value);

    // Save the lesson plan via the store
    await lessonStore.saveLessonPlan(lessonData);

    // Reset local state after successful save
    // Clear any previous error state to ensure UI reflects success
    if (error.value) {
      error.value = null;
    }

    // Notify user of successful save
    showSnackbar('Lesson plan saved successfully', 'success');
    hasUnsavedChanges.value = false; // Reset unsaved changes flag
    updatedComponents.value = [];    // Clear updated components list

  } catch (err) {
    // Log error for debugging purposes
    console.error('Error saving lesson plan:', err);

    // Notify user of failure
    showSnackbar(
      err instanceof Error ? err.message : 'Failed to save lesson plan',
      'error'
    );
  }
};

// Sorts components based on priority order
const sortComponentsByPriority = (
  components: string[],
  priorityOrder: string[] = [
    'standardsAddressed',
    'objectives',
    'lessonFlow',
    'assessments',
    'markupProblemSets',
    'markupProblemSetsAboveGradeLevel',
    'markupProblemSetsBelowGradeLevel',
    'accessibility',
    'materials'
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

// Handles chat messages and updates lesson plan components

// Handles new lesson creation
const handleLessonCreated = (lesson: Lesson) => {
  showSnackbar('Lesson created successfully', 'success');
  fetchLessons(); // Refresh lesson list
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
  lessonStore.clearSaveStatus(); // Clear save status in store
};

// Downloads the current lesson plan as HTML
const handleDownload = () => {
  if (!currentPlan.value || !selectedLesson.value) return;
  
  const lessonPlanElement = document.querySelector('.lesson-plan-card');
  if (!lessonPlanElement) return;

  const htmlContent = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>${selectedLesson.value.title} - Lesson Plan</title>
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

        .lesson-plan-card {
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

        /* Info Cards */
        .info-card {
            background-color: #f8f9fa;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 16px;
        }

        .info-card:last-child {
            margin-bottom: 0;
        }

        .info-label {
            font-weight: 600;
            margin-bottom: 8px;
            color: #5C6970;
        }

        /* Lists */
        .v-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .v-list-item {
            padding: 8px 0;
            font-size: 0.875rem;
            line-height: 1.4;
        }

        /* Chips and Tags */
        .v-chip {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 16px;
            background: #78C0E5;
            color: white;
            font-size: 14px;
            margin: 4px;
        }

        /* Headers */
        .text-h6 {
            font-family: 'Museo Moderno', sans-serif;
            font-size: 1.25rem;
            color: #5C6970;
            margin-bottom: 1rem;
        }

        /* Differentiation Section */
        .differentiation-section .diff-title {
            font-weight: 600;
            color: #78C0E5;
            margin-bottom: 8px;
        }

        .question-title {
            font-weight: 600;
            font-size: 1.1rem;
            color: #78C0E5;
            margin-bottom: 16px;
        }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            background: white;
        }

        th, td {
            padding: 12px 16px;
            border: 1px solid #e0e0e0;
            text-align: left;
        }

        th {
            background: #f8f9fa;
            font-weight: 600;
            color: #5C6970;
        }

        /* Lists */
        ul, ol {
            margin: 8px 0;
            padding-left: 24px;
        }

        li {
            margin-bottom: 8px;
        }

        /* Metadata Display */
        .metadata-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
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

            .lesson-plan-card {
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
    ${lessonPlanElement.outerHTML}
</body>
</html>`;

  const blob = new Blob([htmlContent], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `${selectedLesson.value.title.toLowerCase().replace(/\s+/g, '_')}_lesson_plan.html`;
  link.click();
  URL.revokeObjectURL(url);
};

// Toggles selection of lesson plan sections for chat context
const handleSectionSelect = (section: string) => {
  const index = contextSelected.value.indexOf(section);
  if (index === -1) {
    contextSelected.value.push(section); // Add section to selected contexts
  } else {
    contextSelected.value.splice(index, 1); // Remove section from selected contexts
  }
};
</script>

# Template Section

<template>
  <v-container fluid>
    <!-- Chat Component at the Top -->
    <div class="chat-top">
      <div v-if="selectedLesson" class="chat-wrapper" :style="{ height: chatHeight + 'px' }">
        <LessonChat
          ref="lessonChat"
          :is-generating="chatLoading"
          :initial-message="
            'How would you like to improve this lesson plan? ' +
            'I can help you refine specific sections or make general improvements.'
          "
          :selected-contexts="contextSelected"
          @send-message="handleChatMessage"
          @resize="(height) => chatHeight = height"
        />
      </div>
    </div>

    <!-- Main Content Below Chat -->
    <v-row>
      <!-- Left Column: Lesson List -->
      <v-col cols="12" md="3">
        <v-card elevation="1">
          <v-card-title class="py-4 px-4">
            <span class="text-h5">My Lessons</span>
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
              New Lesson
            </v-btn>
          </v-card-title>
          <ListLessons
            :lessons="lessonStore.getSortedLessons"
            :selected-lesson-id="selectedLesson?.lessonId"
            :is-loading="isLoading"
            @select-lesson="handleSelectLesson"
            @delete-lesson="handleDeleteClick"
          />
        </v-card>
      </v-col>

      <!-- Right Column: Lesson Plan Display -->
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
                  :loading="isSaving"
                  :disabled="isSaving"
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
              v-if="selectedLesson"
              color="info"
              variant="text"
              @click="handleViewVersions(selectedLesson.lessonId)"
            >
              <template v-slot:prepend>
                <History :size="20" />
              </template>
              View Versions
            </v-btn>
            <v-btn
              v-if="selectedLesson && currentPlan"
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

          <!-- Lesson Plan Display -->
          <LessonPlanDisplay
            :plan="currentPlan"
            :is-loading="chatLoading"
            :selected-sections="contextSelected"
            :updated-sections="updatedComponents"
            @section-select="handleSectionSelect"
            @update:updatedComponents="(component) => updatedComponents.push(component)"
          />
        </div>
      </v-col>
    </v-row>

    <!-- Create Lesson Modal -->
    <CreateLesson v-model="createDialog" @lesson-created="handleLessonCreated" />

    <!-- Delete Confirmation Dialog -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title class="text-h5 pa-4">Delete Lesson Plan</v-card-title>
        <v-card-text class="pa-4">
          Are you sure you want to delete "{{ lessonToDelete?.title }}"?
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
    <LessonVersions
      v-model="versionsDialog"
      :lesson-id="selectedLesson?.lessonId"
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
    .v-card-title {
      color: #5c6970; // Neutral Dark from style guide
    }
    
    .v-card-text {
      font-family: "Quicksand", sans-serif;
      color: #b7bbbe; // Neutral Medium from style guide
    }
  }
}

// Button styling using design system colors
.v-btn {
  font-family: "Quicksand", sans-serif;
  font-weight: 500;
  
  &.v-btn--variant-text {
    opacity: 0.85;
    
    &:hover {
      opacity: 1;
    }
  }

  &:has(> .lucide) {
    opacity: 0.85;
    transition: all 0.2s ease;
    
    &:hover {
      opacity: 1;
      transform: scale(1.1);
    }
  }
}

// Snackbar customization
.v-snackbar {
  .v-snackbar__wrapper {
    font-family: "Quicksand", sans-serif;
    
    .v-btn {
      font-weight: 600;
      text-transform: none;
    }
  }
}

// Custom scrollbar styling using primary color
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(120, 192, 229, 0.2); // Primary color with opacity
  border-radius: 3px;
  
  &:hover {
    background: rgba(120, 192, 229, 0.4);
  }
}

// Dark mode adjustments
:deep(.v-theme--dark) {
  .v-card {
    background-color: #394246; // Dark Mode Background from style guide
  }

  .create-button {
    &:hover {
      background-color: lighten(#78c0e5, 5%);
      box-shadow: 0 4px 12px rgba(120, 192, 229, 0.3);
    }
  }

  ::-webkit-scrollbar-thumb {
    background: rgba(120, 192, 229, 0.3);
    
    &:hover {
      background: rgba(120, 192, 229, 0.5);
    }
  }
}

// Responsive design adjustments
@media (max-width: 960px) {
  .v-container {
    padding: 12px;
  }
  
  .v-card {
    .v-card-title {
      padding: 12px;
      
      .text-h5 {
        font-size: 18pt;
      }
    }
  }
  
  .create-button {
    height: 36px;
    font-size: 14px;
  }
  
  .v-dialog {
    margin: 12px;
    
    .v-card {
      max-height: calc(100vh - 24px);
      overflow-y: auto;
    }
  }
}

// Chat positioning and styling
.chat-top {
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: white;
  padding: 16px 16px 36px 16px; /* Added padding at bottom for resize handle */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.chat-wrapper {
  height: 300px;
  min-height: 200px;
  max-height: 800px;
  position: relative;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: white;
  transition: height 0.1s ease;
}

.no-lesson-selected {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 24px;
  background: #fafafa;
  border-radius: 8px;
}

/* Dark theme support */
:deep(.v-theme--dark) {
  .chat-top {
    background-color: #1a1a1a;
  }

  .chat-wrapper {
    background-color: #1a1a1a;
    border-color: #2a2a2a;
  }

  .no-lesson-selected {
    background: #2a2a2a;
  }
}

// Enhanced visual highlighting for updated UI elements
:deep(.updated) {
  background-color: #e6f7ff; // Light blue for subtle highlight
  border-left: 4px solid #78c0e5; // Primary color border
  padding-left: 8px;
  animation: pulse 1s ease-in-out; // Pulse animation for emphasis
}

@keyframes pulse {
  0% {
    background-color: #e6f7ff;
  }
  50% {
    background-color: #bae7ff; // Slightly brighter mid-animation
  }
  100% {
    background-color: #e6f7ff;
  }
}
</style>