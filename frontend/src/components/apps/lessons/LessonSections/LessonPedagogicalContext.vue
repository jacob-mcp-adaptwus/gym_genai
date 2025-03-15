<script setup lang="ts">
import { 
  Brain, School, AlertCircle, GitBranch,
  ClipboardCheck, Target, Eye, Ear, CheckCircle2,
  Clock, ListTodo, Award, ArrowRight, HelpCircle,
  Lightbulb, Rocket, Crosshair, CheckSquare,
  ListChecks, Glasses, MessageCircle
} from 'lucide-vue-next';

interface MathematicalProgressions {
  priorKnowledge: string[];
  futureConnections: string[];
  crossCutting: string[];
}

interface Misconceptions {
  common: string[];
  addressingStrategies: string[];
}

interface PedagogicalContext {
  bigIdeas: string[];
  prerequisites: string[];
  misconceptions: Misconceptions;
  mathematicalProgressions: MathematicalProgressions;
}

interface Props {
  context: PedagogicalContext;
}

defineProps<Props>();
</script>

# Template Section
<template>
  <section class="pedagogical-context">
    <!-- Big Ideas - Updated with additional visual cues -->
    <div class="section-block">
      <div class="section-header">
        <div class="icon-group">
          <Brain :size="24" class="icon primary" />
          <Lightbulb :size="20" class="icon secondary" />
        </div>
        <h3 class="text-h6">Big Ideas</h3>
      </div>
      <ul class="mt-2">
        <li v-for="(idea, index) in context.bigIdeas" :key="index">
          {{ idea }}
        </li>
      </ul>
    </div>

    <!-- Prerequisites - Updated with visual indicators -->
    <div class="section-block">
      <div class="section-header">
        <div class="icon-group">
          <School :size="24" class="icon primary" />
          <Clock :size="20" class="icon secondary" />
        </div>
        <h3 class="text-h6">Prerequisites</h3>
      </div>
      <ul class="mt-2 checklist">
        <li v-for="(prereq, index) in context.prerequisites" :key="index">
          <CheckCircle2 :size="18" class="list-icon" />
          {{ prereq }}
        </li>
      </ul>
    </div>

    <!-- Learning Modalities - New Section -->
    <div class="section-block">
      <div class="section-header">
        <div class="icon-group">
          <Glasses :size="24" class="icon primary" />
          <ListChecks :size="20" class="icon secondary" />
        </div>
        <h3 class="text-h6">Learning Modalities</h3>
      </div>
      <div class="modalities-grid mt-2">
        <div class="modality-item">
          <Eye :size="20" class="modality-icon" />
          <span>Visual</span>
        </div>
        <div class="modality-item">
          <Ear :size="20" class="modality-icon" />
          <span>Auditory</span>
        </div>
        <div class="modality-item">
          <MessageCircle :size="20" class="modality-icon" />
          <span>Verbal</span>
        </div>
      </div>
    </div>

    <!-- Misconceptions - Updated with new icons -->
    <div class="section-block">
      <div class="section-header">
        <div class="icon-group">
          <AlertCircle :size="24" class="icon primary" />
          <HelpCircle :size="20" class="icon secondary" />
        </div>
        <h3 class="text-h6">Misconceptions & Strategies</h3>
      </div>
      <div class="misconceptions-grid mt-2">
        <div class="common-misconceptions">
          <h4 class="text-subtitle-1 mb-2">Common Misconceptions</h4>
          <ul>
            <li v-for="(item, index) in context.misconceptions.common" :key="index">
              {{ item }}
            </li>
          </ul>
        </div>
        <div class="addressing-strategies">
          <h4 class="text-subtitle-1 mb-2">Addressing Strategies</h4>
          <ul>
            <li v-for="(strategy, index) in context.misconceptions.addressingStrategies" :key="index">
              {{ strategy }}
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Mathematical Progressions - Updated with new icons -->
    <div class="section-block">
      <div class="section-header">
        <div class="icon-group">
          <GitBranch :size="24" class="icon primary" />
          <Rocket :size="20" class="icon secondary" />
        </div>
        <h3 class="text-h6">Mathematical Progressions</h3>
      </div>
      <div class="progressions-stack mt-2">
        <div class="progression-block">
          <div class="progression-header">
            <Clock :size="20" class="progression-icon" />
            <h4 class="text-subtitle-1">Prior Knowledge</h4>
          </div>
          <ul>
            <li v-for="(item, index) in context.mathematicalProgressions.priorKnowledge" :key="index">
              {{ item }}
            </li>
          </ul>
        </div>
        <div class="progression-block">
          <div class="progression-header">
            <ArrowRight :size="20" class="progression-icon" />
            <h4 class="text-subtitle-1">Future Connections</h4>
          </div>
          <ul>
            <li v-for="(item, index) in context.mathematicalProgressions.futureConnections" :key="index">
              {{ item }}
            </li>
          </ul>
        </div>
        <div class="progression-block">
          <div class="progression-header">
            <Crosshair :size="20" class="progression-icon" />
            <h4 class="text-subtitle-1">Cross-Cutting Concepts</h4>
          </div>
          <ul>
            <li v-for="(item, index) in context.mathematicalProgressions.crossCutting" :key="index">
              {{ item }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>


# Style Section
<style lang="scss" scoped>
.pedagogical-context {
  .section-block {
    background-color: rgb(var(--v-theme-background));
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(var(--v-theme-on-surface), 0.12);

    &:last-child {
      margin-bottom: 0;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
      
      .icon-group {
        display: flex;
        align-items: center;
        position: relative;

        .icon.primary {
          color: #78C0E5;
        }

        .icon.secondary {
          color: #5C6970;
          position: absolute;
          right: -12px;
          bottom: -8px;
          transform: scale(0.8);
        }
      }

      h3 {
        font-family: 'Museo Moderno', sans-serif;
        color: #5C6970;
        margin: 0;
      }
    }

    ul {
      list-style-type: none;
      padding: 0;
      margin: 0;

      li {
        font-family: 'Quicksand', sans-serif;
        font-size: 16pt;
        margin-bottom: 0.75rem;
        padding-left: 1.5rem;
        position: relative;

        &:before {
          content: "•";
          color: #78C0E5;
          position: absolute;
          left: 0;
        }

        &:last-child {
          margin-bottom: 0;
        }
      }
    }
  }

  .misconceptions-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;

    @media (min-width: 768px) {
      grid-template-columns: repeat(2, 1fr);
    }

    h4 {
      font-family: 'Museo Moderno', sans-serif;
      color: #5C6970;
    }
  }

  .progressions-stack {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;

    .progression-block {
      padding: 1rem;
      background-color: rgba(120, 192, 229, 0.05);
      border-radius: 6px;
      
      .progression-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1rem;

        .progression-icon {
          color: #78C0E5;
        }

        h4 {
          margin: 0;
          font-family: 'Museo Moderno', sans-serif;
          color: #5C6970;
        }
      }
    }
  }

  .list-icon {
    position: absolute;
    left: 0;
    color: #78C0E5;
  }

  .modalities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 1rem;

    .modality-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem;
      background-color: rgba(120, 192, 229, 0.1);
      border-radius: 6px;

      .modality-icon {
        color: #78C0E5;
      }

      span {
        font-family: 'Quicksand', sans-serif;
        font-size: 14pt;
      }
    }
  }
}

:deep(.v-theme--dark) {
  .section-block {
    background-color: #394246;
    border-color: rgba(255, 255, 255, 0.12);
  }
}
</style>