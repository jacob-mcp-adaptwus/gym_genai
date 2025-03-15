// Script Section
<script setup lang="ts">
import { computed } from 'vue';
import { 
  ClipboardCheck, 
  Target, 
  Eye, 
  Ear, 
  CheckCircle2,
  Clock,
  ListTodo,
  Award,
  ArrowRight,
  HelpCircle,
  Lightbulb,
  Rocket,
  Crosshair,
  CheckSquare,
  ListChecks,
  Glasses,
  MessageCircle
} from 'lucide-vue-next';

interface Checkpoint {
  timing: string;
  task: string;
  successCriteria: string[];
  intervention: {
    support: string;
    extension: string;
  };
}

interface ObservationGuide {
  lookFor: string[];
  listenFor: string[];
}

interface FormativeAssessment {
  checkpoints: Checkpoint[];
  observationGuide: ObservationGuide;
}

interface SummativeTask {
  description: string;
  alignedObjectives: string[];
  scoringCriteria: string[];
}

interface SummativeAssessment {
  tasks: SummativeTask[];
}

interface AssessmentProps {
  assessments: {
    formative: FormativeAssessment;
    summative: SummativeAssessment;
  };
}

const props = defineProps<AssessmentProps>();

// Computed property to check if we have formative assessments
const hasFormative = computed(() => {
  return props.assessments?.formative?.checkpoints?.length > 0 ||
         (props.assessments?.formative?.observationGuide?.lookFor?.length > 0 &&
          props.assessments?.formative?.observationGuide?.listenFor?.length > 0);
});

// Computed property to check if we have summative assessments
const hasSummative = computed(() => {
  return props.assessments?.summative?.tasks?.length > 0;
});

// Computed property to combine look-for and listen-for items
const observationItems = computed(() => {
  const lookFor = props.assessments?.formative?.observationGuide?.lookFor || [];
  const listenFor = props.assessments?.formative?.observationGuide?.listenFor || [];
  
  return {
    lookFor,
    listenFor
  };
});
</script>

# Template Section
<template>
  <section class="lesson-assessments">
    <div class="d-flex align-center mb-4">
      <ClipboardCheck :size="24" class="mr-2" />
      <h2 class="text-h5">Assessments</h2>
    </div>

    <!-- Formative Assessments -->
    <div v-if="hasFormative" class="assessment-card mb-6">
      <div class="card-header">
        <ListChecks :size="20" class="mr-2" />
        <h3 class="text-h6">Formative Assessment</h3>
      </div>

      <!-- Checkpoints -->
      <div v-if="assessments.formative.checkpoints.length" class="checkpoints-grid">
        <div v-for="(checkpoint, index) in assessments.formative.checkpoints"
          :key="index"
          class="checkpoint-card">
          <div class="timing-header">
            <Clock :size="16" class="mr-2" />
            {{ checkpoint.timing }}
          </div>
          
          <div class="content-section">
            <div class="section-label">
              <ListTodo :size="16" class="mr-2" />
              Task
            </div>
            <div class="task-content">{{ checkpoint.task }}</div>
          </div>

          <div class="content-section">
            <div class="section-label">
              <Target :size="16" class="mr-2" />
              Success Criteria
            </div>
            <div class="criteria-list">
              <div v-for="(criteria, critIndex) in checkpoint.successCriteria"
                :key="critIndex"
                class="criteria-item">
                <CheckCircle2 :size="16" class="mr-2 text-success" />
                {{ criteria }}
              </div>
            </div>
          </div>

          <div class="content-section">
            <div class="section-label">
              <HelpCircle :size="16" class="mr-2" />
              Interventions
            </div>
            <div class="interventions-grid">
              <div class="intervention-item support">
                <div class="intervention-label">
                  <Lightbulb :size="16" class="mr-2" />
                  Support
                </div>
                {{ checkpoint.intervention.support }}
              </div>
              <div class="intervention-item extension">
                <div class="intervention-label">
                  <Rocket :size="16" class="mr-2" />
                  Extension
                </div>
                {{ checkpoint.intervention.extension }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Observation Guide -->
      <div v-if="observationItems.lookFor.length || observationItems.listenFor.length" 
        class="observation-card">
        <div class="guide-header">
          <Glasses :size="18" class="mr-2" />
          Observation Guide
        </div>
        
        <div class="guide-grid">
          <!-- Look For -->
          <div v-if="observationItems.lookFor.length" class="guide-section">
            <div class="guide-label">
              <Eye :size="16" class="mr-2 text-primary" />
              Look For
            </div>
            <div class="guide-items">
              <div v-for="(item, index) in observationItems.lookFor"
                :key="index"
                class="guide-item">
                <ArrowRight :size="14" class="mr-2" />
                {{ item }}
              </div>
            </div>
          </div>

          <!-- Listen For -->
          <div v-if="observationItems.listenFor.length" class="guide-section">
            <div class="guide-label">
              <MessageCircle :size="16" class="mr-2 text-info" />
              Listen For
            </div>
            <div class="guide-items">
              <div v-for="(item, index) in observationItems.listenFor"
                :key="index"
                class="guide-item">
                <ArrowRight :size="14" class="mr-2" />
                {{ item }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Summative Assessments -->
    <div v-if="hasSummative" class="assessment-card">
      <div class="card-header">
        <Award :size="20" class="mr-2" />
        <h3 class="text-h6">Summative Assessment</h3>
      </div>

      <div class="tasks-grid">
        <div v-for="(task, index) in assessments.summative.tasks"
          :key="index"
          class="task-card">
          <div class="task-header">
            <Crosshair :size="16" class="mr-2" />
            Task {{ index + 1 }}
          </div>
          
          <div class="content-section">
            <div class="section-label">
              <ListTodo :size="16" class="mr-2" />
              Description
            </div>
            <div class="task-description">{{ task.description }}</div>
          </div>

          <div class="content-section">
            <div class="section-label">
              <Target :size="16" class="mr-2" />
              Aligned Objectives
            </div>
            <div class="objectives-list">
              <div v-for="(objective, objIndex) in task.alignedObjectives"
                :key="objIndex"
                class="objective-item">
                <ArrowRight :size="14" class="mr-2 text-primary" />
                {{ objective }}
              </div>
            </div>
          </div>

          <div class="content-section">
            <div class="section-label">
              <CheckSquare :size="16" class="mr-2" />
              Scoring Criteria
            </div>
            <div class="criteria-list">
              <div v-for="(criteria, critIndex) in task.scoringCriteria"
                :key="critIndex"
                class="criteria-item">
                <CheckCircle2 :size="16" class="mr-2 text-success" />
                {{ criteria }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.lesson-assessments {
  .text-h5, .text-h6 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    color: #5C6970;
    margin: 0;
  }

  .assessment-card {
    background-color: rgb(var(--v-theme-background));
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

    .card-header {
      display: flex;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid rgba(120, 192, 229, 0.2);
    }
  }

  .checkpoints-grid, .tasks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    margin-bottom: 24px;
  }

  .checkpoint-card, .task-card {
    background-color: rgba(120, 192, 229, 0.05);
    border-radius: 8px;
    padding: 16px;

    .timing-header, .task-header {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      font-size: 16px;
      color: var(--v-theme-primary);
      margin-bottom: 16px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(120, 192, 229, 0.2);
    }
  }

  .content-section {
    margin-bottom: 16px;

    &:last-child {
      margin-bottom: 0;
    }

    .section-label {
      font-weight: 600;
      color: #5C6970;
      margin-bottom: 8px;
    }
  }

  .criteria-list, .objectives-list {
    display: flex;
    flex-direction: column;
    gap: 8px;

    .criteria-item, .objective-item {
      display: flex;
      align-items: flex-start;
      font-size: 14px;
      line-height: 1.4;
    }
  }

  .interventions-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;

    .intervention-item {
      background-color: rgba(120, 192, 229, 0.08);
      padding: 12px;
      border-radius: 6px;

      .intervention-label {
        font-weight: 600;
        margin-bottom: 4px;
        color: var(--v-theme-primary);
      }
    }
  }

  .observation-card {
    background-color: rgba(120, 192, 229, 0.05);
    border-radius: 8px;
    padding: 20px;

    .guide-header {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      font-size: 16px;
      display: flex;
      align-items: center;
      margin-bottom: 16px;
    }

    .guide-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
    }

    .guide-section {
      .guide-label {
        display: flex;
        align-items: center;
        font-weight: 600;
        margin-bottom: 12px;
      }

      .guide-items {
        display: flex;
        flex-direction: column;
        gap: 8px;

        .guide-item {
          background-color: rgba(120, 192, 229, 0.08);
          padding: 8px 12px;
          border-radius: 6px;
          font-size: 14px;
          line-height: 1.4;
        }
      }
    }
  }

  // Dark mode adjustments
  :deep(.v-theme--dark) {
    .assessment-card {
      background-color: #394246;
    }

    .checkpoint-card, .task-card, .observation-card {
      background-color: rgba(120, 192, 229, 0.08);
    }

    .intervention-item, .guide-item {
      background-color: rgba(120, 192, 229, 0.12);
    }
  }

  // Mobile optimizations
  @media (max-width: 960px) {
    .checkpoints-grid, .tasks-grid {
      grid-template-columns: 1fr;
    }

    .assessment-card {
      padding: 16px;
    }

    .text-h5 {
      font-size: 20px;
    }

    .text-h6 {
      font-size: 16px;
    }
  }
}
</style>