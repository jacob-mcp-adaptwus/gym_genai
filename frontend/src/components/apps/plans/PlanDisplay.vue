<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import type { WorkoutPlan } from '@/services/planService';

// Define props for the component
const props = defineProps<{
  plan: WorkoutPlan | null;
  isLoading: boolean;
  selectedSections: string[];
  updatedSections: string[];
}>();

// Define emits for the component
const emit = defineEmits<{
  (e: 'section-select', section: string): void;
  (e: 'update:updatedComponents', component: string): void;
}>();

// Track expanded sections
const expandedSections = ref<Record<string, boolean>>({
  profile: true,
  workouts: true,
  nutrition: true,
  supplementation: true,
  coachFeedback: true
});

// Toggle section expansion
const toggleSection = (section: string) => {
  expandedSections.value[section] = !expandedSections.value[section];
};

// Check if a section is selected for chat context
const isSectionSelected = (section: string) => {
  return props.selectedSections.includes(section);
};

// Check if a section has been updated
const isSectionUpdated = (section: string) => {
  return props.updatedSections.includes(section);
};

// Handle section selection for chat context
const handleSectionSelect = (section: string) => {
  emit('section-select', section);
};

// Get section icon based on section name
const getSectionIcon = (section: string) => {
  switch (section) {
    case 'profile':
      return 'mdi-account';
    case 'workouts':
      return 'mdi-clock';
    case 'nutrition':
      return 'mdi-food-apple';
    case 'supplementation':
      return 'mdi-pill';
    case 'coachFeedback':
      return 'mdi-message';
    default:
      return 'mdi-clock';
  }
};

// Format section title for display
const formatSectionTitle = (section: string) => {
  switch (section) {
    case 'profile':
      return 'Athlete Profile';
    case 'workouts':
      return 'Workout Program';
    case 'nutrition':
      return 'Nutrition Plan';
    case 'supplementation':
      return 'Supplementation';
    case 'coachFeedback':
      return 'Coach Feedback';
    default:
      return section.charAt(0).toUpperCase() + section.slice(1);
  }
};

// Get section class based on selection and update status
const getSectionClass = (section: string) => {
  const classes = ['section-card'];
  
  if (isSectionSelected(section)) {
    classes.push('section-selected');
  }
  
  if (isSectionUpdated(section)) {
    classes.push('section-updated');
  }
  
  return classes.join(' ');
};

// Format experience level for display
const formatExperienceLevel = (level: string | undefined) => {
  if (!level) return 'Not specified';
  return level.charAt(0).toUpperCase() + level.slice(1);
};

// Format date for display
const formatDate = (dateString: string | undefined) => {
  if (!dateString) return '';
  
  try {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: 'numeric'
    }).format(date);
  } catch (e) {
    console.error('Error formatting date:', e);
    return dateString;
  }
};

// Get color for experience level badge
const getExperienceLevelColor = (level: string | undefined) => {
  if (!level) return 'grey';
  
  switch (level.toLowerCase()) {
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

// Reset updated sections when plan changes
watch(() => props.plan, () => {
  // Clear the updated components array
  props.updatedSections.forEach(section => {
    emit('update:updatedComponents', section);
  });
}, { deep: true });
</script>

<template>
  <div class="plan-display">
    <!-- Loading State -->
    <div
      v-if="isLoading || !plan"
      class="loading-skeleton"
    >
      <v-skeleton-loader type="card"></v-skeleton-loader>
      <v-skeleton-loader type="text"></v-skeleton-loader>
      <v-skeleton-loader type="text"></v-skeleton-loader>
      <v-skeleton-loader type="text"></v-skeleton-loader>
      <v-skeleton-loader type="card"></v-skeleton-loader>
      <v-skeleton-loader type="text"></v-skeleton-loader>
      <v-skeleton-loader type="text"></v-skeleton-loader>
    </div>

    <!-- Empty State -->
    <v-card v-else-if="!plan" class="empty-state" elevation="1">
      <v-card-text class="d-flex flex-column align-center justify-center pa-8">
        <v-icon icon="mdi-weight-lifter" size="64" color="grey-lighten-1" class="mb-4"></v-icon>
        <span class="text-h6 text-grey-darken-1">No Plan Selected</span>
        <span class="text-body-1 text-grey text-center mt-2">
          Select a plan from the list or create a new one to get started
        </span>
      </v-card-text>
    </v-card>

    <!-- Plan Display -->
    <div v-else class="plan-card">
      <!-- Plan Header -->
      <div class="plan-header mb-6">
        <h1 class="text-h4 font-weight-bold">{{ plan.metadata?.planName || 'Workout Plan' }}</h1>
        
        <div class="d-flex flex-wrap gap-2 mt-2">
          <v-chip
            v-if="plan.profile?.experience?.level"
            :color="getExperienceLevelColor(plan.profile.experience.level)"
            size="small"
            label
          >
            {{ formatExperienceLevel(plan.profile.experience.level) }}
          </v-chip>
          
          <v-chip
            v-if="plan.profile?.goals?.primary"
            color="primary"
            size="small"
            variant="outlined"
            label
          >
            {{ plan.profile.goals.primary }}
          </v-chip>
          
          <v-chip
            v-if="plan.metadata?.lastModified"
            color="grey"
            size="small"
            variant="flat"
            label
          >
            Updated: {{ formatDate(plan.metadata.lastModified) }}
          </v-chip>
        </div>
      </div>

      <!-- Plan Sections -->
      <div class="plan-sections">
        <!-- Profile Section -->
        <div 
          :class="getSectionClass('profile')"
          @click="handleSectionSelect('profile')"
        >
          <v-card-title class="d-flex justify-space-between align-center">
            <div class="d-flex align-center">
              <v-icon :icon="getSectionIcon('profile')" class="mr-2" size="20"></v-icon>
              <span>{{ formatSectionTitle('profile') }}</span>
            </div>
            <div class="d-flex align-center">
              <v-icon
                v-if="isSectionSelected('profile')"
                icon="mdi-check-circle"
                color="primary"
                size="20"
                class="mr-2"
              ></v-icon>
              <v-btn
                icon
                variant="text"
                size="small"
                @click.stop="toggleSection('profile')"
              >
                <v-icon :icon="expandedSections.profile ? 'mdi-chevron-up' : 'mdi-chevron-down'" size="20"></v-icon>
              </v-btn>
            </div>
          </v-card-title>
          
          <v-expand-transition>
            <v-card-text v-if="expandedSections.profile && plan.profile">
              <div class="profile-section">
                <!-- Current Stats -->
                <div v-if="plan.profile.currentStats" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Current Stats</h3>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Weight</div>
                          <div class="text-h6">{{ plan.profile.currentStats.weight }} kg</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Height</div>
                          <div class="text-h6">{{ plan.profile.currentStats.height }} cm</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Body Fat</div>
                          <div class="text-h6">{{ plan.profile.currentStats.bodyFat }}%</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
                
                <!-- Goals -->
                <div v-if="plan.profile.goals" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Goals</h3>
                  <v-card variant="outlined" class="mb-2">
                    <v-card-text>
                      <div class="text-overline">Primary Goal</div>
                      <div class="text-body-1">{{ plan.profile.goals.primary }}</div>
                    </v-card-text>
                  </v-card>
                  <v-row>
                    <v-col cols="12" sm="6" v-if="plan.profile.goals.targetWeight">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Target Weight</div>
                          <div class="text-h6">{{ plan.profile.goals.targetWeight }} kg</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="6" v-if="plan.profile.goals.targetBodyFat">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Target Body Fat</div>
                          <div class="text-h6">{{ plan.profile.goals.targetBodyFat }}%</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
                
                <!-- Experience -->
                <div v-if="plan.profile.experience" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Experience</h3>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Level</div>
                          <div class="text-h6">{{ formatExperienceLevel(plan.profile.experience.level) }}</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="6" v-if="plan.profile.experience.yearsTraining">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Years Training</div>
                          <div class="text-h6">{{ plan.profile.experience.yearsTraining }}</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
              </div>
            </v-card-text>
          </v-expand-transition>
        </div>
        
        <!-- Workouts Section -->
        <div 
          :class="getSectionClass('workouts')"
          @click="handleSectionSelect('workouts')"
        >
          <v-card-title class="d-flex justify-space-between align-center">
            <div class="d-flex align-center">
              <v-icon :icon="getSectionIcon('workouts')" class="mr-2" size="20"></v-icon>
              <span>{{ formatSectionTitle('workouts') }}</span>
            </div>
            <div class="d-flex align-center">
              <v-icon
                v-if="isSectionSelected('workouts')"
                icon="mdi-check-circle"
                color="primary"
                size="20"
                class="mr-2"
              ></v-icon>
              <v-btn
                icon
                variant="text"
                size="small"
                @click.stop="toggleSection('workouts')"
              >
                <v-icon :icon="expandedSections.workouts ? 'mdi-chevron-up' : 'mdi-chevron-down'" size="20"></v-icon>
              </v-btn>
            </div>
          </v-card-title>
          
          <v-expand-transition>
            <v-card-text v-if="expandedSections.workouts && plan.workouts">
              <div class="workouts-section">
                <!-- Split Structure -->
                <div v-if="plan.workouts.splitStructure" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Split Structure</h3>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Type</div>
                          <div class="text-h6">{{ plan.workouts.splitStructure.type }}</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Days Per Week</div>
                          <div class="text-h6">{{ plan.workouts.splitStructure.daysPerWeek }}</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
                
                <!-- Weekly Schedule -->
                <div v-if="plan.workouts.weeklySchedule && plan.workouts.weeklySchedule.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Weekly Schedule</h3>
                  
                  <v-expansion-panels variant="accordion">
                    <v-expansion-panel
                      v-for="(day, index) in plan.workouts.weeklySchedule"
                      :key="index"
                    >
                      <v-expansion-panel-title>
                        <div class="d-flex align-center">
                          <strong>{{ day.day }}</strong>
                          <v-chip
                            size="x-small"
                            color="primary"
                            class="ml-2"
                          >
                            {{ day.focus }}
                          </v-chip>
                        </div>
                      </v-expansion-panel-title>
                      <v-expansion-panel-text>
                        <div v-if="day.exercises && day.exercises.length > 0">
                          <h4 class="text-subtitle-2 font-weight-bold mb-2">Exercises</h4>
                          <v-table density="compact">
                            <thead>
                              <tr>
                                <th>Exercise</th>
                                <th>Sets</th>
                                <th>Reps</th>
                                <th>Rest</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr v-for="(exercise, exIndex) in day.exercises" :key="exIndex">
                                <td>{{ exercise.name }}</td>
                                <td>{{ exercise.sets }}</td>
                                <td>{{ exercise.repsRange }}</td>
                                <td>{{ exercise.rest }}</td>
                              </tr>
                            </tbody>
                          </v-table>
                        </div>
                        
                        <div v-if="day.cardio" class="mt-4">
                          <h4 class="text-subtitle-2 font-weight-bold mb-2">Cardio</h4>
                          <v-chip size="small" color="info" class="mr-2">{{ day.cardio.type }}</v-chip>
                          <v-chip size="small" color="info" class="mr-2">{{ day.cardio.duration }}</v-chip>
                          <v-chip size="small" color="info">{{ day.cardio.intensity }}</v-chip>
                        </div>
                      </v-expansion-panel-text>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </div>
              </div>
            </v-card-text>
          </v-expand-transition>
        </div>
        
        <!-- Nutrition Section -->
        <div 
          :class="getSectionClass('nutrition')"
          @click="handleSectionSelect('nutrition')"
        >
          <v-card-title class="d-flex justify-space-between align-center">
            <div class="d-flex align-center">
              <v-icon :icon="getSectionIcon('nutrition')" class="mr-2" size="20"></v-icon>
              <span>{{ formatSectionTitle('nutrition') }}</span>
            </div>
            <div class="d-flex align-center">
              <v-icon
                v-if="isSectionSelected('nutrition')"
                icon="mdi-check-circle"
                color="primary"
                size="20"
                class="mr-2"
              ></v-icon>
              <v-btn
                icon
                variant="text"
                size="small"
                @click.stop="toggleSection('nutrition')"
              >
                <v-icon :icon="expandedSections.nutrition ? 'mdi-chevron-up' : 'mdi-chevron-down'" size="20"></v-icon>
              </v-btn>
            </div>
          </v-card-title>
          
          <v-expand-transition>
            <v-card-text v-if="expandedSections.nutrition && plan.nutrition">
              <div class="nutrition-section">
                <!-- Calorie Targets -->
                <div v-if="plan.nutrition.calorieTargets" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Calorie Targets</h3>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Training Days</div>
                          <div class="text-h6">{{ plan.nutrition.calorieTargets.trainingDays }} kcal</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Rest Days</div>
                          <div class="text-h6">{{ plan.nutrition.calorieTargets.restDays }} kcal</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Weekly Average</div>
                          <div class="text-h6">{{ plan.nutrition.calorieTargets.weeklyAverage }} kcal</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
                
                <!-- Macro Breakdown -->
                <div v-if="plan.nutrition.macroBreakdown" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Macro Breakdown</h3>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Protein</div>
                          <div class="text-h6">{{ plan.nutrition.macroBreakdown.protein.grams }}g ({{ plan.nutrition.macroBreakdown.protein.percentage }}%)</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Carbs</div>
                          <div class="text-h6">{{ plan.nutrition.macroBreakdown.carbs.grams }}g ({{ plan.nutrition.macroBreakdown.carbs.percentage }}%)</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-card variant="outlined" class="info-card">
                        <v-card-text>
                          <div class="text-overline">Fats</div>
                          <div class="text-h6">{{ plan.nutrition.macroBreakdown.fats.grams }}g ({{ plan.nutrition.macroBreakdown.fats.percentage }}%)</div>
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
              </div>
            </v-card-text>
          </v-expand-transition>
        </div>
        
        <!-- Supplementation Section -->
        <div 
          :class="getSectionClass('supplementation')"
          @click="handleSectionSelect('supplementation')"
        >
          <v-card-title class="d-flex justify-space-between align-center">
            <div class="d-flex align-center">
              <v-icon :icon="getSectionIcon('supplementation')" class="mr-2" size="20"></v-icon>
              <span>{{ formatSectionTitle('supplementation') }}</span>
            </div>
            <div class="d-flex align-center">
              <v-icon
                v-if="isSectionSelected('supplementation')"
                icon="mdi-check-circle"
                color="primary"
                size="20"
                class="mr-2"
              ></v-icon>
              <v-btn
                icon
                variant="text"
                size="small"
                @click.stop="toggleSection('supplementation')"
              >
                <v-icon :icon="expandedSections.supplementation ? 'mdi-chevron-up' : 'mdi-chevron-down'" size="20"></v-icon>
              </v-btn>
            </div>
          </v-card-title>
          
          <v-expand-transition>
            <v-card-text v-if="expandedSections.supplementation && plan.supplementation">
              <div class="supplementation-section">
                <!-- Performance Enhancers -->
                <div v-if="plan.supplementation.performanceEnhancers && plan.supplementation.performanceEnhancers.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Performance Enhancers</h3>
                  <v-table density="compact">
                    <thead>
                      <tr>
                        <th>Supplement</th>
                        <th>Category</th>
                        <th>Dosage</th>
                        <th>Timing</th>
                        <th>Purpose</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(supplement, index) in plan.supplementation.performanceEnhancers" :key="index">
                        <td>{{ supplement.name }}</td>
                        <td>{{ supplement.category }}</td>
                        <td>{{ supplement.dosage }}</td>
                        <td>{{ supplement.timing }}</td>
                        <td>{{ supplement.purpose }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </div>
                
                <!-- Recovery Aids -->
                <div v-if="plan.supplementation.recoveryAids && plan.supplementation.recoveryAids.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Recovery Aids</h3>
                  <v-table density="compact">
                    <thead>
                      <tr>
                        <th>Supplement</th>
                        <th>Dosage</th>
                        <th>Timing</th>
                        <th>Purpose</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(supplement, index) in plan.supplementation.recoveryAids" :key="index">
                        <td>{{ supplement.name }}</td>
                        <td>{{ supplement.dosage }}</td>
                        <td>{{ supplement.timing }}</td>
                        <td>{{ supplement.purpose }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </div>
                
                <!-- Health Supports -->
                <div v-if="plan.supplementation.healthSupports && plan.supplementation.healthSupports.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Health Supports</h3>
                  <v-table density="compact">
                    <thead>
                      <tr>
                        <th>Supplement</th>
                        <th>Dosage</th>
                        <th>Timing</th>
                        <th>Purpose</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(supplement, index) in plan.supplementation.healthSupports" :key="index">
                        <td>{{ supplement.name }}</td>
                        <td>{{ supplement.dosage }}</td>
                        <td>{{ supplement.timing }}</td>
                        <td>{{ supplement.purpose }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </div>
                
                <!-- Hormone Protocols -->
                <div v-if="plan.supplementation.hormoneProtocols && plan.supplementation.hormoneProtocols.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Hormone Protocols</h3>
                  <v-table density="compact">
                    <thead>
                      <tr>
                        <th>Compound</th>
                        <th>Dosage</th>
                        <th>Frequency</th>
                        <th>Duration</th>
                        <th>Cycle Weeks</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(protocol, index) in plan.supplementation.hormoneProtocols" :key="index">
                        <td>{{ protocol.compound }}</td>
                        <td>{{ protocol.dosage }}</td>
                        <td>{{ protocol.frequency }}</td>
                        <td>{{ protocol.duration }}</td>
                        <td>{{ protocol.cycleWeeks }}</td>
                      </tr>
                    </tbody>
                  </v-table>
                </div>
              </div>
            </v-card-text>
          </v-expand-transition>
        </div>
        
        <!-- Coach Feedback Section -->
        <div 
          :class="getSectionClass('coachFeedback')"
          @click="handleSectionSelect('coachFeedback')"
        >
          <v-card-title class="d-flex justify-space-between align-center">
            <div class="d-flex align-center">
              <v-icon :icon="getSectionIcon('coachFeedback')" class="mr-2" size="20"></v-icon>
              <span>{{ formatSectionTitle('coachFeedback') }}</span>
            </div>
            <div class="d-flex align-center">
              <v-icon
                v-if="isSectionSelected('coachFeedback')"
                icon="mdi-check-circle"
                color="primary"
                size="20"
                class="mr-2"
              ></v-icon>
              <v-btn
                icon
                variant="text"
                size="small"
                @click.stop="toggleSection('coachFeedback')"
              >
                <v-icon :icon="expandedSections.coachFeedback ? 'mdi-chevron-up' : 'mdi-chevron-down'" size="20"></v-icon>
              </v-btn>
            </div>
          </v-card-title>
          
          <v-expand-transition>
            <v-card-text v-if="expandedSections.coachFeedback && plan.coachFeedback">
              <div class="coach-feedback-section">
                <!-- Last Updated -->
                <div v-if="plan.coachFeedback.lastUpdated" class="mb-4">
                  <v-chip size="small" color="grey" class="mb-2">
                    Last Updated: {{ formatDate(plan.coachFeedback.lastUpdated) }}
                  </v-chip>
                </div>
                
                <!-- Adjustments -->
                <div v-if="plan.coachFeedback.adjustments && plan.coachFeedback.adjustments.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Recommended Adjustments</h3>
                  <v-timeline density="compact" align="start">
                    <v-timeline-item
                      v-for="(adjustment, index) in plan.coachFeedback.adjustments"
                      :key="index"
                      dot-color="primary"
                      size="small"
                    >
                      <div class="d-flex flex-column">
                        <div class="d-flex align-center">
                          <v-chip size="x-small" color="primary" class="mr-2">{{ adjustment.component }}</v-chip>
                          <span class="text-caption">{{ adjustment.implementationDate }}</span>
                        </div>
                        <div class="text-body-1 mt-1">{{ adjustment.recommendation }}</div>
                        <div class="text-caption text-grey-darken-1 mt-1">{{ adjustment.reason }}</div>
                      </div>
                    </v-timeline-item>
                  </v-timeline>
                </div>
                
                <!-- Progress Notes -->
                <div v-if="plan.coachFeedback.progressNotes && plan.coachFeedback.progressNotes.length > 0" class="mb-4">
                  <h3 class="text-subtitle-1 font-weight-bold mb-2">Progress Notes</h3>
                  <v-timeline density="compact" align="start">
                    <v-timeline-item
                      v-for="(note, index) in plan.coachFeedback.progressNotes"
                      :key="index"
                      dot-color="info"
                      size="small"
                    >
                      <div class="d-flex flex-column">
                        <div class="d-flex align-center">
                          <span class="text-caption">{{ note.date }}</span>
                        </div>
                        <div class="text-body-1 mt-1">{{ note.observations }}</div>
                        <div class="text-caption text-grey-darken-1 mt-1">{{ note.nextStepsRecommendation }}</div>
                      </div>
                    </v-timeline-item>
                  </v-timeline>
                </div>
              </div>
            </v-card-text>
          </v-expand-transition>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.plan-display {
  height: 100%;
  
  .loading-skeleton {
    border-radius: 8px;
    height: 100%;
  }
  
  .empty-state {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
  }
  
  .plan-card {
    height: 100%;
    overflow-y: auto;
    padding: 24px;
    background-color: rgb(var(--v-theme-background));
    border-radius: 8px;
    
    .plan-header {
      h1 {
        font-family: "Museo Moderno", sans-serif;
        color: #5c6970;
        letter-spacing: -0.5px;
      }
    }
    
    .plan-sections {
      display: flex;
      flex-direction: column;
      gap: 16px;
      
      .section-card {
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 8px;
        overflow: hidden;
        transition: all 0.2s ease;
        cursor: pointer;
        
        &:hover {
          border-color: rgba(120, 192, 229, 0.5);
          box-shadow: 0 2px 8px rgba(120, 192, 229, 0.1);
        }
        
        .v-card-title {
          background-color: rgba(120, 192, 229, 0.05);
          font-family: "Quicksand", sans-serif;
          font-weight: 600;
          font-size: 1.1rem;
          color: #5C6970;
          padding: 16px;
          border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .v-card-text {
          padding: 16px;
        }
      }
      
      .section-selected {
        border-color: rgba(120, 192, 229, 0.8);
        box-shadow: 0 2px 12px rgba(120, 192, 229, 0.2);
        
        .v-card-title {
          background-color: rgba(120, 192, 229, 0.1);
        }
      }
      
      .section-updated {
        border-color: rgba(76, 175, 80, 0.8);
        box-shadow: 0 2px 12px rgba(76, 175, 80, 0.2);
        
        .v-card-title {
          background-color: rgba(76, 175, 80, 0.1);
        }
      }
    }
  }
  
  // Section styling
  .profile-section,
  .workouts-section,
  .nutrition-section,
  .supplementation-section,
  .coach-feedback-section {
    h3 {
      font-family: "Quicksand", sans-serif;
      color: #5C6970;
      margin-bottom: 12px;
    }
    
    .info-card {
      height: 100%;
      
      .v-card-text {
        padding: 12px;
        
        .text-overline {
          font-size: 0.75rem;
          font-weight: 600;
          color: rgba(0, 0, 0, 0.6);
          text-transform: uppercase;
          letter-spacing: 0.0625rem;
        }
      }
    }
  }
  
  // Table styling
  .v-table {
    border-radius: 8px;
    overflow: hidden;
    
    th {
      font-weight: 600;
      color: #5C6970;
      background-color: rgba(120, 192, 229, 0.05);
    }
  }
  
  // Timeline styling
  .v-timeline {
    .v-timeline-item {
      margin-bottom: 8px;
    }
  }
  
  // Expansion panels styling
  .v-expansion-panels {
    border-radius: 8px;
    overflow: hidden;
    
    .v-expansion-panel-title {
      font-weight: 600;
      color: #5C6970;
    }
  }
}

// Responsive adjustments
@media (max-width: 960px) {
  .plan-display {
    .plan-card {
      padding: 16px;
      
      .plan-header {
        h1 {
          font-size: 1.5rem;
        }
      }
    }
  }
}
</style>
