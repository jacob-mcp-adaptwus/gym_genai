# Script Section
<script setup lang="ts">
import { ref } from 'vue';
import { 
  ChevronDown, ChevronUp, Brain, Target,
  ClipboardCheck, Eye, Ear, CheckCircle2, Clock,
  ListTodo, Award, Lightbulb, Rocket, Crosshair, 
  CheckSquare, ListChecks, MessageCircle
} from 'lucide-vue-next';
import type { Problem } from '@/services/lessonService';
import 'katex/dist/katex.min.css';
import katex from 'katex';

interface ProblemSets {
  warmup: Problem[];
  corePractice: Problem[];
  extension: Problem[];
}

//this is passed to componenet to render
interface Props {
  problemSets: ProblemSets;
}

const props = defineProps<Props>();

// Track expanded state for each problem set section
const warmupExpanded = ref(true);
const coreExpanded = ref(true);
const extensionExpanded = ref(true);

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


// Enhanced difficulty indicators with icons
const getDifficultyInfo = (level: number) => {
  const icons = {
    1: { icon: CheckCircle2, color: 'success' },
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
  if (!text.includes('$')) return [{ type: 'text', content: text }];
  
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
      <Lightbulb :size="24" class="mr-2" />
      Learning Journey
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
              color="primary"
              class="mr-3"
              size="42"
            >
              <Brain :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Mind Warmup</div>
              <div class="text-caption text-medium-emphasis">
                Get started with these introductory exercises
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.warmup.length"
              color="primary"
              class="mr-3"
            >
              <component :is="Brain" :size="20" color="primary" />
            </v-badge>
            <v-btn
              :icon="warmupExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              color="primary"
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
                      color="primary"
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
    <!-- End of Warmup Problems -->
    <!-- Core Practice Problems -->
    <v-card class="mb-4 problem-section core-section">
      <v-card-item 
        @click="toggleSection('core')"
        class="section-header"
      >
        <div class="d-flex align-center justify-space-between">
          <div class="d-flex align-center">
            <v-avatar
              color="info"
              class="mr-3"
              size="42"
            >
              <Target :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Core Practice</div>
              <div class="text-caption text-medium-emphasis">
                Master the essential concepts
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.corePractice.length"
              color="info"
              class="mr-3"
            >
              <component :is="Target" :size="20" color="info" />
            </v-badge>
            <v-btn
              :icon="coreExpanded ? ChevronUp : ChevronDown"
              variant="tonal"
              density="comfortable"
              color="info"

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
              color="warning"
              class="mr-3"
              size="42"
            >
              <Rocket :size="24" class="section-icon" />
            </v-avatar>
            <div>
              <div class="text-h6 mb-1">Extension Challenges</div>
              <div class="text-caption text-medium-emphasis">
                Push your understanding further
              </div>
            </div>
          </div>
          <div class="d-flex align-center">
            <v-badge
              :content="problemSets.extension.length"
              color="warning"
              class="mr-3"
            >
              <component :is="Rocket" :size="24" color="warning" />
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
                      color="warning"
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

      .difficulty-stars {
        font-size: 0.9rem;
        font-weight: 600;
        background: linear-gradient(45deg, #FF7043, #FF9800);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent;
        text-shadow: 0 2px 4px rgba(255, 112, 67, 0.1);
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
</style>