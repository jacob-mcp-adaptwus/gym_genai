# Script Section
<script setup lang="ts">
import { ref } from 'vue';
import { 
  ChevronDown, ChevronUp, Brain, Target,
  ClipboardCheck, Eye, Ear, CheckCircle2, Clock,
  ListTodo, Award, Rocket, Crosshair, 
  CheckSquare, ListChecks, MessageCircle, BookOpen,
  HelpCircle
} from 'lucide-vue-next';
import type { Problem } from '@/services/lessonService';
import 'katex/dist/katex.min.css';
import katex from 'katex';

// Design Style Guide Colors
const COLORS = {
  primary: '#78C0E5',
  secondary: '#EF8D61',
  accent1: '#B7E6F2',
  accent2: '#FFCDB5',
  accent3: '#C8E0D9',
  neutralDark: '#5C6970',
  neutralMedium: '#B7BBBE',
  neutralLight: '#F1F1F2'
};

interface ProblemSets {
  warmup: Problem[];
  corePractice: Problem[];
  extension: Problem[];
}

interface Props {
  problemSets: ProblemSets;
}

const props = defineProps<Props>();

// Track expanded state for each problem set section
const warmupExpanded = ref(true);
const coreExpanded = ref(true);
const extensionExpanded = ref(true);

// Track hint visibility states for each problem
const hintVisibility = ref<{ [key: string]: boolean }>({});

// Initialize visibility states
const initializeVisibilityStates = () => {
  props.problemSets.warmup?.forEach((_, index) => {
    hintVisibility.value[`warmup-${index}`] = false;
  });
  
  props.problemSets.corePractice?.forEach((_, index) => {
    hintVisibility.value[`core-${index}`] = false;
  });
  
  props.problemSets.extension?.forEach((_, index) => {
    hintVisibility.value[`extension-${index}`] = false;
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

// Toggle hint visibility
const toggleHint = (problemId: string) => {
  hintVisibility.value[problemId] = !hintVisibility.value[problemId];
};

// Enhanced difficulty indicators with icons
const getDifficultyInfo = (level: number) => {
  const icons = {
    1: { icon: CheckCircle2, color: COLORS.accent1 },
    2: { icon: Target, color: COLORS.accent2 },
    3: { icon: Rocket, color: COLORS.accent3 },
    4: { icon: Brain, color: COLORS.secondary },
    5: { icon: Award, color: COLORS.primary }
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
      Advanced Learning Challenges
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
              :color="COLORS.primary"
              class="mr-3"
              size="42"
            >
              <Brain :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Advanced Warmup</div>
              <div class="text-caption text-medium-emphasis">
                Challenge your understanding with these preparatory exercises
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.warmup?.length"
              :color="COLORS.primary"
              class="mr-3"
            >
              <component :is="Brain" :size="20" :color="COLORS.primary" />
            </v-badge>
            <v-btn
              :icon="warmupExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              :color="COLORS.primary"
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
                      :color="COLORS.primary"
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
                      <template v-for="(part, idx) in renderMath(problem.problem.stem)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <div v-if="problem.problem.context" class="text-body-2 text-medium-emphasis mb-4">
                      <template v-for="(part, idx) in renderMath(problem.problem.context)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <!-- Hints Section -->
                    <div v-if="problem.hints" class="hints-section mb-4">
                      <v-card variant="outlined" class="pa-3">
                        <div class="d-flex align-center mb-2">
                          <HelpCircle :size="20" class="mr-2" :color="COLORS.accent2" />
                          <span class="text-h6">Strategic Hints</span>
                          <v-btn
                            variant="text"
                            density="comfortable"
                            :color="COLORS.accent2"
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
            <v-avatar
              :color="COLORS.secondary"
              class="mr-3"
              size="42"
            >
              <Target :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Advanced Practice</div>
              <div class="text-caption text-medium-emphasis">
                Master complex concepts and applications
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.corePractice?.length"
              :color="COLORS.secondary"
              class="mr-3"
            >
              <component :is="Target" :size="20" :color="COLORS.secondary" />
            </v-badge>
            <v-btn
              :icon="coreExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              :color="COLORS.secondary"
            />
          </div>
        </div>
      </v-card-item>

      <v-expand-transition>
        <div v-if="coreExpanded">
          <v-divider></v-divider>
          <v-card-text>
            <v-list class="problem-list">
              <v-list-item
                v-for="(problem, index) in problemSets.corePractice"
                :key="`core-${index}`"
                class="problem-item mb-3"
                rounded="lg"
              >
                <!-- Similar structure to warmup problems -->
                <div class="d-flex flex-column w-100">
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
                      :color="COLORS.secondary"
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

                  <div class="problem-content">
                    <div class="text-body-1 mb-2">
                      <template v-for="(part, idx) in renderMath(problem.problem.stem)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <div v-if="problem.problem.context" class="text-body-2 text-medium-emphasis">
                      <template v-for="(part, idx) in renderMath(problem.problem.context)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>
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
              :color="COLORS.accent1"
              class="mr-3"
              size="42"
            >
              <Rocket :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Expert Challenges</div>
              <div class="text-caption text-medium-emphasis">
                Push beyond standard boundaries
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.extension?.length"
              :color="COLORS.accent1"
              class="mr-3"
            >
              <component :is="Rocket" :size="20" :color="COLORS.accent1" />
            </v-badge>
            <v-btn
              :icon="extensionExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              :color="COLORS.accent1"
            />
          </div>
        </div>
      </v-card-item>

      <v-expand-transition>
        <div v-if="extensionExpanded">
          <v-divider></v-divider>
          <v-card-text>
            <v-list class="problem-list">
              <v-list-item
                v-for="(problem, index) in problemSets.extension"
                :key="`extension-${index}`"
                class="problem-item mb-3"
                rounded="lg"
              >
                <div class="d-flex flex-column w-100">
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
                      :color="COLORS.accent1"
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

                  <div class="problem-content">
                    <div class="text-body-1 mb-2">
                      <template v-for="(part, idx) in renderMath(problem.problem.stem)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>

                    <div v-if="problem.problem.openEndedPrompt" class="text-body-2 text-medium-emphasis">
                      <strong>Challenge:</strong>
                      <template v-for="(part, idx) in renderMath(problem.problem.openEndedPrompt)" :key="idx">
                        <span v-html="part.content"></span>
                      </template>
                    </div>
                  </div>
                </div>
              </v-list-item>
            </v-list>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </div>
</template>

<style lang="scss" scoped>
.problem-sets {
  .problem-section {
    border: none;
    background: #FFFFFF; // Light Mode Background from style guide
    box-shadow: 0 4px 20px rgba(92, 105, 112, 0.05); // Using neutralDark with opacity
    border-radius: 16px;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(92, 105, 112, 0.08);
    }

    // Specific styles for each section using style guide colors
    &.warmup-section {
      border-left: 4px solid #78C0E5; // Primary
    }

    &.core-section {
      border-left: 4px solid #EF8D61; // Secondary
    }

    &.extension-section {
      border-left: 4px solid #B7E6F2; // Accent 1
    }
  }

  .section-header {
    padding: 20px 24px;
    
    .text-h6 {
      font-family: 'Museo Moderno', sans-serif;
      font-weight: 600;
      color: #5C6970; // Neutral Dark
      letter-spacing: -0.3px;
    }

    .section-icon {
      color: #78C0E5; // Primary
      transition: transform 0.3s ease;
    }

    .text-caption {
      color: #B7BBBE; // Neutral Medium
    }
  }

  .problem-item {
    margin: 12px 0;
    padding: 16px;
    border-radius: 12px;
    background: #F1F1F2; // Neutral Light
    border: 1px solid #B7BBBE; // Neutral Medium
    transition: all 0.2s ease;

    &:hover {
      background: #FFFFFF; // Light Mode Background
      transform: translateX(4px);
    }

    // Hints section styling
    .hints-section {
      .v-card {
        background: #FFFFFF; // Light Mode Background
        border: 1px solid #B7E6F2; // Accent 1
        transition: all 0.2s ease;

        &:hover {
          background: #F1F1F2; // Neutral Light
        }

        .text-h6 {
          font-family: 'Quicksand', sans-serif;
          font-size: 1.1rem;
          font-weight: 600;
          color: #5C6970; // Neutral Dark
        }
      }

      .v-card {
        border-left: 4px solid #FFCDB5; // Accent 2
      }
    }

    .difficulty-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 12px;
      background: #F1F1F2; // Neutral Light
      border-radius: 12px;
      min-width: 100px;
      border: 1px solid #B7BBBE; // Neutral Medium
      transition: all 0.2s ease;

      &:hover {
        transform: scale(1.02);
        background: #FFFFFF; // Light Mode Background
      }

      .difficulty-text {
        color: #5C6970; // Neutral Dark
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
      }
    }

    .problem-type-icon {
      color: #78C0E5; // Primary
      opacity: 0.8;
    }

    :deep(.v-list-item-title) {
      font-family: 'Quicksand', sans-serif;
      font-size: 1.1rem;
      line-height: 1.5;
      color: #5C6970; // Neutral Dark
      
      .katex {
        font-size: 1.1em;
      }
    }

    :deep(.v-list-item-subtitle) {
      margin-top: 8px;
      color: #B7BBBE; // Neutral Medium
      line-height: 1.4;

      strong {
        color: #78C0E5; // Primary
      }
    }

    .v-chip {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      letter-spacing: 0.3px;
      
      &.primary {
        background-color: #78C0E5; // Primary
      }
      
      &.secondary {
        background-color: #EF8D61; // Secondary
      }
      
      &.accent-1 {
        background-color: #B7E6F2; // Accent 1
      }
    }
  }
}

// Dark mode adjustments
:deep(.v-theme--dark) {
  .problem-section {
    background: #394246; // Dark Mode Background
  }

  .problem-item {
    background: #5C6970; // Neutral Dark
    border-color: #B7BBBE; // Neutral Medium

    &:hover {
      background: #394246; // Dark Mode Background
    }

    .hints-section {
      .v-card {
        background: #394246; // Dark Mode Background
        
        &:hover {
          background: #5C6970; // Neutral Dark
        }
      }
    }
  }
}

// Add styles for LaTeX rendering
:deep(.katex) {
  font-size: 1.1em;
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