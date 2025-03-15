# Script Section
<script setup lang="ts">
import { ref } from 'vue';
import { 
  ChevronDown, ChevronUp, Brain, Target,
  ClipboardCheck, Eye, Ear, CheckCircle, Clock,
  ListTodo, Award, Rocket, Crosshair, 
  CheckSquare, ListChecks, MessageCircle, BookOpen,
  HelpCircle, CheckSquare as CheckSquare2
} from 'lucide-vue-next';
import type { Problem } from '@/services/lessonService';
import 'katex/dist/katex.min.css';
import katex from 'katex';

interface ProblemSets {
  warmup: Problem[];
  corePractice: Problem[];
  extension: Problem[];
}

interface Props {
  problemSets: ProblemSets;
}

const props = defineProps<Props>();

// Track expanded state for each problem set section - defaulting to true
const warmupExpanded = ref(true);
const coreExpanded = ref(true);
const extensionExpanded = ref(true);

// Track solution visibility states for each problem
const solutionVisibility = ref<{ [key: string]: boolean }>({});
const hintVisibility = ref<{ [key: string]: boolean }>({});

// Initialize visibility states
const initializeVisibilityStates = () => {
  // Set all solutions and hints to visible by default
  props.problemSets.warmup?.forEach((_, index) => {
    solutionVisibility.value[`warmup-${index}`] = true;
    hintVisibility.value[`warmup-${index}`] = true;
  });
  
  props.problemSets.corePractice?.forEach((_, index) => {
    solutionVisibility.value[`core-${index}`] = true;
    hintVisibility.value[`core-${index}`] = true;
  });
  
  props.problemSets.extension?.forEach((_, index) => {
    solutionVisibility.value[`extension-${index}`] = true;
    hintVisibility.value[`extension-${index}`] = true;
  });
};

// Call initialization on component creation
initializeVisibilityStates();

// Toggle section expansion
const toggleSection = (section: 'warmup' | 'core' | 'extension') => {
  switch(section) {
    case 'warmup':
      warmupExpanded.value = !warmupExpanded.value;
      break;
    case 'core':
      coreExpanded.value = !coreExpanded.value;
      break;
    case 'extension':
      extensionExpanded.value = !extensionExpanded.value;
      break;
  }
};

// Toggle solution visibility
const toggleSolution = (problemId: string) => {
  solutionVisibility.value[problemId] = !solutionVisibility.value[problemId];
};

// Toggle hint visibility
const toggleHint = (problemId: string) => {
  hintVisibility.value[problemId] = !hintVisibility.value[problemId];
};

// Enhanced difficulty indicators with icons
const getDifficultyInfo = (level: number) => {
  const icons = {
    1: { icon: CheckCircle, color: 'success' },
    2: { icon: Target, color: 'info' },
    3: { icon: Rocket, color: 'warning' },
    4: { icon: Brain, color: 'error' },
    5: { icon: Award, color: 'purple' }
  };
  return icons[level as keyof typeof icons] || icons[1];
};

// Get problem type icon
const getProblemTypeIcon = (type: string) => {
  const icons = {
    'multiple-choice': Eye,
    'open-ended': MessageCircle,
    'listening': Ear,
    'matching': ListChecks,
    'quick': Clock,
    'practice': ListTodo,
    'challenge': Crosshair,
    'assessment': ClipboardCheck,
    default: CheckSquare
  };
  return icons[type.toLowerCase() as keyof typeof icons] || icons.default;
};

interface RenderedPart {
  type: 'text' | 'latex';
  content: string;
}

const renderLatex = (tex: string): string => {
  return katex.renderToString(tex, { 
    throwOnError: false,
    displayMode: false 
  });
};

const renderMath = (text: string): RenderedPart[] => {
  if (!text?.includes('$')) return [{ type: 'text', content: text || '' }];
  
  return text.split(/(\$[^\$]+\$)/).map(part => {
    if (part.startsWith('$') && part.endsWith('$')) {
      return {
        type: 'latex',
        content: renderLatex(part.slice(1, -1))
      };
    }
    return {
      type: 'text',
      content: part
    };
  });
};
</script>
# Template Section
<template>
  <div class="problem-sets">
    <h3 class="text-h5 mb-4 d-flex align-center">
      <BookOpen :size="24" class="mr-2" />
      Below Grade Level Learning Journey
    </h3>

    <!-- Warmup Problems Section -->
    <v-card class="mb-4 problem-section warmup-section">
      <v-card-item 
        @click="toggleSection('warmup')"
        class="section-header"
      >
        <div class="d-flex align-center justify-space-between">
          <div class="d-flex align-center">
            <v-avatar
              color="success"
              class="mr-3"
              size="42"
            >
              <Brain :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Foundational Warmup</div>
              <div class="text-caption text-medium-emphasis">
                Start with these basic practice exercises
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.warmup?.length"
              color="success"
              class="mr-3"
            >
              <component :is="Brain" :size="20" color="success" />
            </v-badge>
            <v-btn
              :icon="warmupExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              color="success"
            />
          </div>
        </div>
      </v-card-item>

      <v-expand-transition>
        <div v-if="warmupExpanded">
          <v-divider></v-divider>
          <v-card-text>
            <v-list class="problem-list">
              <v-list-item
                v-for="(problem, index) in problemSets.warmup"
                :key="`warmup-${index}`"
                class="problem-item mb-3"
                rounded="lg"
              >
                <div class="d-flex flex-column w-100">
                  <!-- Problem Header -->
                  <div class="d-flex align-center mb-2">
                    <v-chip
                      size="small"
                      :color="getDifficultyInfo(problem.difficulty).color"
                      class="mr-2"
                      variant="flat"
                    >
                      Level {{ problem.difficulty }}
                    </v-chip>
                    <v-chip
                      size="small"
                      color="success"
                      variant="outlined"
                      class="text-caption"
                    >
                      <component 
                        :is="getProblemTypeIcon(problem.type)"
                        :size="14"
                        class="mr-1"
                      />
                      {{ problem.type }}
                    </v-chip>
                  </div>

                  <!-- Problem Content -->
                  <div class="problem-content mb-4">
                    <div class="text-body-1 mb-2">
                      <template v-for="(part, idx) in renderMath(problem.problem.stem)" :key="`stem-${index}-${idx}`">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <div v-if="problem.problem.context" class="text-body-2 text-medium-emphasis mb-4">
                      <template v-for="(part, idx) in renderMath(problem.problem.context)" :key="`context-${index}-${idx}`">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <!-- Hints Section -->
                    <div v-if="problem.hints" class="hints-section mb-4">
                      <v-card variant="outlined" class="pa-3">
                        <div class="d-flex align-center mb-2">
                          <HelpCircle :size="20" class="mr-2 text-warning" />
                          <span class="text-h6">Helpful Hints</span>
                          <v-btn
                            variant="text"
                            density="comfortable"
                            color="warning"
                            class="ml-auto"
                            @click="toggleHint(`warmup-${index}`)"
                          >
                            {{ hintVisibility[`warmup-${index}`] ? 'Hide' : 'Show' }} Hints
                          </v-btn>
                        </div>
                        <v-expand-transition>
                          <div v-if="hintVisibility[`warmup-${index}`]">
                            <div v-for="(hint, hintIdx) in problem.hints" :key="hintIdx" class="mb-2">
                              <div class="text-body-2">{{ hint.text }}</div>
                              <div v-if="hint.scaffold" class="text-caption text-medium-emphasis">
                                Scaffold: {{ hint.scaffold }}
                              </div>
                            </div>
                          </div>
                        </v-expand-transition>
                      </v-card>
                    </div>

                    <!-- Solution Section -->
                    <div v-if="problem.solution" class="solution-section">
                      <v-card variant="outlined" class="pa-3">
                        <div class="d-flex align-center mb-2">
                          <CheckSquare2 :size="20" class="mr-2 text-success" />
                          <span class="text-h6">Solution</span>
                          <v-btn
                            variant="text"
                            density="comfortable"
                            color="success"
                            class="ml-auto"
                            @click="toggleSolution(`warmup-${index}`)"
                          >
                            {{ solutionVisibility[`warmup-${index}`] ? 'Hide' : 'Show' }} Solution
                          </v-btn>
                        </div>
                        <v-expand-transition>
                          <div v-if="solutionVisibility[`warmup-${index}`]">
                            <div class="text-body-1 mb-2">
                              <strong>Answer:</strong>
                              <template v-for="(part, idx) in renderMath(problem.solution.answer)" :key="idx">
                                <span v-html="part.content"></span>
                              </template>
                            </div>
                            <div v-if="problem.solution.workingOut" class="text-body-2">
                              <strong>Working Out:</strong>
                              <template v-for="(part, idx) in renderMath(problem.solution.workingOut)" :key="idx">
                                <span v-html="part.content"></span>
                              </template>
                            </div>
                          </div>
                        </v-expand-transition>
                      </v-card>
                    </div>
                  </div>
                </div>
              </v-list-item>
            </v-list>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>

    <!-- Core Practice Problems -->
    <v-card class="mb-4 problem-section core-section">
      <v-card-item 
        @click="toggleSection('core')"
        class="section-header"
      >
        <div class="d-flex align-center justify-space-between">
          <div class="d-flex align-center">
            <v-avatar color="info" class="mr-3" size="42">
              <Target :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Core Building Blocks</div>
              <div class="text-caption text-medium-emphasis">
                Essential practice problems
              </div>
            </div>
          </div>
          <v-btn
            :icon="coreExpanded ? ChevronUp : ChevronDown"
            variant="tonal"
            density="comfortable"
            color="info"
          />
        </div>
      </v-card-item>

      <v-expand-transition>
        <div v-show="coreExpanded">
          <v-divider></v-divider>
          <v-card-text>
            <v-list class="problem-list">
              <v-list-item
                v-for="(problem, index) in problemSets.corePractice"
                :key="`core-${index}`"
                class="problem-item mb-3"
              >
                <!-- Problem Header -->
                <div class="d-flex align-center mb-2">
                  <v-chip
                    size="small"
                    :color="getDifficultyInfo(problem.difficulty).color"
                    class="mr-2"
                    variant="flat"
                  >
                    Level {{ problem.difficulty }}
                  </v-chip>
                  <v-chip
                    size="small"
                    color="info"
                    variant="outlined"
                    class="text-caption"
                  >
                    <component 
                      :is="getProblemTypeIcon(problem.type)"
                      :size="14"
                      class="mr-1"
                    />
                    {{ problem.type }}
                  </v-chip>
                </div>

                <!-- Problem Content -->
                <div class="problem-content mb-4">
                  <div class="text-body-1 mb-2">
                    <template v-for="(part, partIndex) in renderMath(problem.problem.stem)" :key="`core-${index}-stem-${partIndex}`">
                      <span v-html="part.content"></span>
                    </template>
                  </div>

                  <div v-if="problem.problem.context" class="text-body-2 text-medium-emphasis mb-4">
                    <template v-for="(part, partIndex) in renderMath(problem.problem.context)" :key="`core-${index}-context-${partIndex}`">
                      <span v-html="part.content"></span>
                    </template>
                  </div>

                  <!-- Solution Section -->
                  <div v-if="problem.solution" class="solution-section">
                    <v-card variant="outlined" class="pa-3">
                      <div class="d-flex align-center mb-2">
                        <CheckSquare2 :size="20" class="mr-2 text-info" />
                        <span class="text-h6">Solution</span>
                        <v-btn
                          variant="text"
                          density="comfortable"
                          color="info"
                          class="ml-auto"
                          @click="toggleSolution(`core-${index}`)"
                        >
                          {{ solutionVisibility[`core-${index}`] ? 'Hide' : 'Show' }} Solution
                        </v-btn>
                      </div>
                      <v-expand-transition>
                        <div v-if="solutionVisibility[`core-${index}`]">
                          <div class="text-body-1 mb-2">
                            <strong>Answer:</strong>
                            <template v-for="(part, partIndex) in renderMath(problem.solution.answer)" :key="`core-${index}-answer-${partIndex}`">
                              <span v-html="part.content"></span>
                            </template>
                          </div>
                          <div v-if="problem.solution.workingOut" class="text-body-2">
                            <strong>Working Out:</strong>
                            <template v-for="(part, partIndex) in renderMath(problem.solution.workingOut)" :key="`core-${index}-working-${partIndex}`">
                              <span v-html="part.content"></span>
                            </template>
                          </div>
                        </div>
                      </v-expand-transition>
                    </v-card>
                  </div>
                </div>
              </v-list-item>
            </v-list>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>

    <!-- Extension Problems -->
    <v-card class="problem-section extension-section">
      <v-card-item 
        @click="toggleSection('extension')"
        class="section-header"
      >
        <div class="d-flex align-center justify-space-between">
          <div class="d-flex align-center">
            <v-avatar
              color="warning"
              class="mr-3"
              size="42"
            >
              <Rocket :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Extension Activities</div>
              <div class="text-caption text-medium-emphasis">
                Try these supported challenge activities
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.extension?.length"
              color="warning"
              class="mr-3"
            >
              <component :is="Rocket" :size="20" color="warning" />
            </v-badge>
            <v-btn
              :icon="extensionExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              color="warning"
            />
          </div>
        </div>
      </v-card-item>

      <v-expand-transition>
        <div v-show="extensionExpanded">
          <v-divider></v-divider>
          <v-card-text>
            <v-list class="problem-list">
              <v-list-item
                v-for="(problem, index) in problemSets.extension"
                :key="`extension-${index}`"
                class="problem-item mb-3"
              >
                <div v-for="part in renderMath(problem.problem.stem)" :key="part.content">
                  <span v-if="part.type === 'text'" v-text="part.content"></span>
                  <span v-else v-html="part.content"></span>
                </div>
              </v-list-item>
            </v-list>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </div>
</template>

# Style Section
<style lang="scss" scoped>
.problem-sets {
  .problem-section {
    border: none;
    background: linear-gradient(145deg, var(--v-theme-surface) 0%, var(--v-theme-surface-variant) 100%);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    border-radius: 16px;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }

    // Specific styles for each section
    &.warmup-section {
      border-left: 4px solid rgb(var(--v-theme-success));
    }

    &.core-section {
      border-left: 4px solid rgb(var(--v-theme-info));
    }

    &.extension-section {
      border-left: 4px solid rgb(var(--v-theme-warning));
    }
  }

  .section-header {
    padding: 20px 24px;
    
    .text-h6 {
      font-family: 'Museo Moderno', sans-serif;
      font-weight: 600;
      color: rgb(var(--v-theme-primary));
      letter-spacing: -0.3px;
    }

    .section-icon {
      color: rgb(var(--v-theme-primary));
      transition: transform 0.3s ease;
    }
  }

  .problem-item {
    margin: 12px 0;
    padding: 16px;
    border-radius: 12px;
    background: rgba(var(--v-theme-surface), 0.7);
    border: 1px solid rgba(var(--v-theme-primary), 0.1);
    transition: all 0.2s ease;

    &:hover {
      background: rgba(var(--v-theme-primary), 0.05);
      transform: translateX(4px);
    }

    // Solution and Hints sections styling
    .solution-section, .hints-section {
      .v-card {
        background: rgba(var(--v-theme-surface), 0.8);
        border: 1px solid rgba(var(--v-theme-primary), 0.1);
        transition: all 0.2s ease;

        &:hover {
          background: rgba(var(--v-theme-surface), 0.9);
        }

        .text-h6 {
          font-family: 'Quicksand', sans-serif;
          font-size: 1.1rem;
          font-weight: 600;
        }
      }
    }

    .solution-section {
      .v-card {
        border-left: 4px solid rgb(var(--v-theme-success));
      }
    }

    .hints-section {
      .v-card {
        border-left: 4px solid rgb(var(--v-theme-warning));
      }
    }

    .difficulty-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 12px;
      background: rgba(var(--v-theme-surface-variant), 0.3);
      border-radius: 12px;
      min-width: 100px;
      border: 1px solid rgba(var(--v-theme-primary), 0.1);
      transition: all 0.2s ease;

      &:hover {
        transform: scale(1.02);
        background: rgba(var(--v-theme-surface-variant), 0.4);
      }

      .difficulty-icon {
        width: 20px;
        height: 20px;
        
        &.success { 
          color: #00C853;
          filter: drop-shadow(0 2px 4px rgba(0, 200, 83, 0.2));
        }
        &.info { 
          color: #2196F3;
          filter: drop-shadow(0 2px 4px rgba(33, 150, 243, 0.2));
        }
        &.warning { 
          color: #FFC107;
          filter: drop-shadow(0 2px 4px rgba(255, 193, 7, 0.2));
        }
        &.error { 
          color: #FF5252;
          filter: drop-shadow(0 2px 4px rgba(255, 82, 82, 0.2));
        }
        &.purple { 
          color: #9C27B0;
          filter: drop-shadow(0 2px 4px rgba(156, 39, 176, 0.2));
        }
      }
    }

    .problem-type-icon {
      color: rgb(var(--v-theme-primary));
      opacity: 0.8;
    }

    :deep(.v-list-item-title) {
      font-family: 'Quicksand', sans-serif;
      font-size: 1.1rem;
      line-height: 1.5;
      color: rgb(var(--v-theme-on-surface));
      
      .katex {
        font-size: 1.1em;
      }
    }

    :deep(.v-list-item-subtitle) {
      margin-top: 8px;
      opacity: 0.85;
      line-height: 1.4;

      strong {
        color: rgb(var(--v-theme-primary));
      }
    }

    .v-chip {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      letter-spacing: 0.3px;
    }
  }
}

// Dark mode adjustments
:deep(.v-theme--dark) {
  .problem-section {
    background: linear-gradient(145deg, rgba(var(--v-theme-surface), 0.8) 0%, rgba(var(--v-theme-surface-variant), 0.8) 100%);
  }

  .problem-item {
    background: rgba(var(--v-theme-surface), 0.4);
    border-color: rgba(var(--v-theme-primary), 0.15);

    &:hover {
      background: rgba(var(--v-theme-primary), 0.1);
    }

    .solution-section, .hints-section {
      .v-card {
        background: rgba(var(--v-theme-surface), 0.6);
        
        &:hover {
          background: rgba(var(--v-theme-surface), 0.7);
        }
      }
    }
  }
}

// Add styles for LaTeX rendering
:deep(.katex) {
  font-size: 1.1em !important;
  line-height: 1.2;
}

:deep(.katex-display) {
  margin: 0.5em 0;
  overflow-x: auto;
  overflow-y: hidden;
}

// Accessibility improvements
@media (prefers-reduced-motion: reduce) {
  .problem-section,
  .problem-item {
    transition: none;
    transform: none;
    
    &:hover {
      transform: none;
    }
  }
}
</style>