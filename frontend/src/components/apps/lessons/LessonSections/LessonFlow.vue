// Script Section
<script setup lang="ts">
import { Clock, UserPlus, Users, MessageCircle, CheckCircle2 } from 'lucide-vue-next';

interface Launch {
  duration: string;
  hook: {
    description: string;
    rationale: string;
  };
  priorKnowledgeActivation: string[];
  teacherMoves: string[];
}

interface Activity {
  title: string;
  description: string;
  grouping: string;
  steps: string[];
  differentiationNotes: {
    acceleration: string[];
    support: string[];
    ell: string[];
  };
}

interface KeyQuestion {
  question: string;
  purpose: string;
  anticipatedResponses: string[];
}

interface ExitTicket {
  question: string;
  expectedResponse: string;
  scoringGuidance: string;
}

interface Closure {
  synthesisTasks: string[];
  reflectionPrompts: string[];
  exitTicket: ExitTicket;
}

interface LessonFlowProps {
  flow: {
    launch: Launch;
    explore: {
      activities: Activity[];
    };
    discussion: {
      keyQuestions: KeyQuestion[];
      studentDiscoursePrompts: string[];
    };
    closure: Closure;
  };
}

const props = defineProps<LessonFlowProps>();

const formatDuration = (duration: string): string => {
  if (!duration) return '';
  return duration.includes('min') || duration.includes('hour') 
    ? duration 
    : `${duration} minutes`;
};
</script>

<template>
  <section class="lesson-flow">
    <div class="text-h6 mb-4">Lesson Flow</div>

    <!-- Launch Section -->
    <v-card class="mb-4 section-card">
      <v-card-title class="d-flex align-center">
        <Clock class="mr-2" :size="20" />
        Launch
        <v-chip size="small" color="primary" class="ml-2">
          {{ formatDuration(props.flow.launch.duration) }}
        </v-chip>
      </v-card-title>
      <v-card-text>
        <!-- Hook -->
        <div class="content-section">
          <div class="section-title">Hook</div>
          <div class="info-card">
            <div class="info-label">Description</div>
            <div>{{ props.flow.launch.hook.description }}</div>
          </div>
          <div class="info-card">
            <div class="info-label">Rationale</div>
            <div>{{ props.flow.launch.hook.rationale }}</div>
          </div>
        </div>

        <!-- Prior Knowledge & Teacher Moves -->
        <div class="content-section">
          <div class="section-title">Prior Knowledge Activation</div>
          <v-list density="compact" class="transparent-list">
            <v-list-item v-for="(item, index) in props.flow.launch.priorKnowledgeActivation"
              :key="index" :title="item"></v-list-item>
          </v-list>
        </div>
      </v-card-text>
    </v-card>

    <!-- Explore Section -->
    <v-card class="mb-4 section-card">
      <v-card-title class="d-flex align-center">
        <Users class="mr-2" :size="20" />
        Explore
      </v-card-title>
      <v-card-text>
        <div v-for="(activity, index) in props.flow.explore.activities" :key="index" class="content-section">
          <div class="section-title">{{ activity.title }}</div>
          
          <div class="info-card">
            <div class="info-label">Description</div>
            <div>{{ activity.description }}</div>
          </div>

          <div class="mb-4">
            <div class="info-label">Grouping</div>
            <v-chip size="small" color="info">{{ activity.grouping }}</v-chip>
          </div>

          <div class="mb-4">
            <div class="info-label">Steps</div>
            <v-list density="compact" class="transparent-list">
              <v-list-item v-for="(step, stepIndex) in activity.steps"
                :key="stepIndex" :title="step"></v-list-item>
            </v-list>
          </div>

          <div class="differentiation-section">
            <div class="info-label">Differentiation Notes</div>
            <div class="info-card">
              <div class="diff-title">Acceleration</div>
              <v-list density="compact" class="transparent-list">
                <v-list-item v-for="(note, noteIndex) in activity.differentiationNotes.acceleration"
                  :key="noteIndex" :title="note"></v-list-item>
              </v-list>
            </div>

            <div class="info-card">
              <div class="diff-title">Support</div>
              <v-list density="compact" class="transparent-list">
                <v-list-item v-for="(note, noteIndex) in activity.differentiationNotes.support"
                  :key="noteIndex" :title="note"></v-list-item>
              </v-list>
            </div>

            <div class="info-card">
              <div class="diff-title">ELL Support</div>
              <v-list density="compact" class="transparent-list">
                <v-list-item v-for="(note, noteIndex) in activity.differentiationNotes.ell"
                  :key="noteIndex" :title="note"></v-list-item>
              </v-list>
            </div>
          </div>
        </div>
      </v-card-text>
    </v-card>

    <!-- Discussion Section -->
    <v-card class="mb-4 section-card">
      <v-card-title class="d-flex align-center">
        <MessageCircle class="mr-2" :size="20" />
        Discussion
      </v-card-title>
      <v-card-text>
        <!-- Key Questions -->
        <div class="content-section">
          <div class="section-title">Key Questions</div>
          <div v-for="(question, index) in props.flow.discussion.keyQuestions" 
            :key="index" 
            class="info-card">
            <div class="question-title">{{ question.question }}</div>
            <div class="mb-2">
              <div class="info-label">Purpose</div>
              <div>{{ question.purpose }}</div>
            </div>
            <div>
              <div class="info-label">Anticipated Responses</div>
              <v-list density="compact" class="transparent-list">
                <v-list-item v-for="(response, responseIndex) in question.anticipatedResponses"
                  :key="responseIndex" :title="response"></v-list-item>
              </v-list>
            </div>
          </div>
        </div>

        <!-- Discourse Prompts -->
        <div class="content-section">
          <div class="section-title">Student Discourse Prompts</div>
          <v-list density="compact">
            <v-list-item
              v-for="(prompt, index) in props.flow.discussion.studentDiscoursePrompts"
              :key="index"
              :title="prompt"
            ></v-list-item>
          </v-list>
        </div>
      </v-card-text>
    </v-card>

    <!-- Closure Section -->
    <v-card class="mb-4 section-card">
      <v-card-title class="d-flex align-center">
        <CheckCircle2 class="mr-2" :size="20" />
        Closure
      </v-card-title>
      <v-card-text>
        <!-- Synthesis Tasks -->
        <div class="content-section">
          <div class="section-title">Synthesis Tasks</div>
          <v-list density="compact">
            <v-list-item
              v-for="(task, index) in props.flow.closure.synthesisTasks"
              :key="index"
              :title="task"
            ></v-list-item>
          </v-list>
        </div>

        <!-- Reflection Prompts -->
        <div class="content-section">
          <div class="section-title">Reflection Prompts</div>
          <v-list density="compact">
            <v-list-item
              v-for="(prompt, index) in props.flow.closure.reflectionPrompts"
              :key="index"
              :title="prompt"
            ></v-list-item>
          </v-list>
        </div>

        <!-- Exit Ticket -->
        <div class="content-section">
          <div class="section-title">Exit Ticket</div>
          <v-card variant="outlined">
            <v-card-text>
              <div class="info-card">
                <div class="info-label">Question</div>
                <div>{{ props.flow.closure.exitTicket.question }}</div>
              </div>
              <div class="info-card">
                <div class="info-label">Expected Response</div>
                <div>{{ props.flow.closure.exitTicket.expectedResponse }}</div>
              </div>
              <div>
                <div class="info-label">Scoring Guidance</div>
                <div>{{ props.flow.closure.exitTicket.scoringGuidance }}</div>
              </div>
            </v-card-text>
          </v-card>
        </div>
      </v-card-text>
    </v-card>
  </section>
</template>

<style lang="scss" scoped>
.lesson-flow {
  .section-card {
    border: 1px solid rgba(var(--v-border-color), 0.12);
    margin-bottom: 24px;
    
    .v-card-title {
      background-color: rgba(var(--v-theme-primary), 0.05);
      padding: 16px;
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
    }
  }

  .content-section {
    margin-bottom: 24px;
    
    &:last-child {
      margin-bottom: 0;
    }
  }

  .section-title {
    font-family: 'Museo Moderno', sans-serif;
    font-size: 1.1rem;
    color: #5C6970;
    margin-bottom: 12px;
    font-weight: 600;
  }

  .info-card {
    background-color: rgba(var(--v-theme-surface), 0.06);
    padding: 16px;
    border-radius: 8px;
    margin-bottom: 12px;

    .info-label {
      font-weight: 600;
      margin-bottom: 8px;
    }
  }

  .transparent-list {
    background-color: transparent;
    padding: 0;

    .v-list-item {
      padding: 4px 0;
    }
  }

  .text-h6 {
    font-family: 'Museo Moderno', sans-serif;
    color: #5C6970;
    margin-bottom: 1rem;
  }

  .v-chip {
    font-family: 'Quicksand', sans-serif;
    font-size: 0.875rem;
  }

  .v-list {
    background-color: transparent;
    
    .v-list-item {
      min-height: 40px;
      padding: 4px 0;
      
      &-title {
        font-family: 'Quicksand', sans-serif;
        font-size: 0.875rem;
        line-height: 1.4;
      }
    }
  }

  .text-subtitle-1 {
    font-family: 'Museo Moderno', sans-serif;
    font-size: 1rem;
    color: #5C6970;
  }

  @media (max-width: 960px) {
    .v-expansion-panel-title {
      min-height: 44px;
      padding: 8px 12px;
    }

    .v-expansion-panel-text {
      padding: 12px;
    }
  }
}

:deep(.v-theme--dark) {
  .lesson-flow {
    .v-expansion-panel {
      background-color: #394246;
    }
  }
}

.differentiation-section {
  .info-card {
    margin-bottom: 12px;
  }

  .diff-title {
    font-weight: 600;
    color: var(--v-theme-primary);
    margin-bottom: 8px;
  }
}

.question-title {
  font-weight: 600;
  font-size: 1.1rem;
  color: var(--v-theme-primary);
  margin-bottom: 16px;
}

.info-card {
  background-color: rgba(var(--v-theme-surface), 0.06);
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 16px;

  &:last-child {
    margin-bottom: 0;
  }
}
</style>