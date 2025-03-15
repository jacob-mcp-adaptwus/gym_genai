// Script Section
<script setup lang="ts">
interface VocabularyTerm {
  term: string;
  definition: string;
  representation: string;
}


interface Accommodations {
  presentation: string[];
  response: string[];
  setting: string[];
  timing: string[];
}

interface VisualSupport {
  type: string;
  description: string;
}

interface AccessibilityProps {
  accommodations?: Accommodations;
  differentiationStrategies?: string[];
  inclusionStrategies?: string[];
}
// example
// {
//     "presentation": [
//         "Present updated fraction problems using both verbal and visual formats to cater to the learner's strengths.",
//         "Use bilingual resources to support understanding of mathematical concepts.",
//         "Incorporate storytelling into the revised fraction problems to increase engagement and relevance."
//     ],
//     "response": [
//         "Allow the learner to explain their problem-solving process verbally before writing it down.",
//         "Provide sentence frames and graphic organizers to support written responses.",
//         "Offer the option to record verbal explanations as an alternative to written computation."
//     ],
//     "setting": [
//         "Create a collaborative learning environment where the learner can share and discuss the updated fraction concepts with peers.",
//         "Provide a quiet space for focused work when the learner needs to translate verbal explanations to written computation."
//     ],
//     "timing": [
//         "Allow extra time for the learner to process and respond to the updated fraction problems, especially when translating verbal explanations to written computation.",
//         "Break down complex fraction problems into smaller, manageable steps with designated time for each step."
//     ]
// }



// Define props with default values
const props = withDefaults(defineProps<{
  accessibility?: AccessibilityProps;
}>(), {
  accessibility: () => ({
    languageSupports: {
      vocabulary: [],
      sentenceFrames: [],
      comprehensionStrategies: []
    },
    accommodations: {
      presentation: [],
      response: [],
      setting: [],
      timing: []
    },
    differentiationStrategies: [],
    inclusionStrategies: []
  })
});

// Import icons
import { 
  Languages, 
  Eye, 
  Settings, 
  BookOpen, 
  MessageSquare, 
  Brain,
  Clock,
  Users,
  PanelLeft,
  Heart
} from 'lucide-vue-next';

</script>
# Template Section
<template>
  <section class="accessibility-section">
    <h2 class="text-h5 mb-4 d-flex align-center">
      <Settings :size="24" class="mr-2" />
      Accessibility & Support
    </h2>



    <!-- Accommodations -->
    <div v-if="accessibility.accommodations" class="support-card">
      <div class="card-header">
        <Settings :size="20" class="mr-2" />
        Accommodations
      </div>
      
      <div class="accommodations-grid">
        <!-- Presentation -->
        <div v-if="accessibility.accommodations.presentation?.length" class="accommodation-section">
          <h4 class="section-title">
            <PanelLeft :size="18" class="mr-2" />
            Presentation
          </h4>
          <div class="info-list">
            <div v-for="(item, index) in accessibility.accommodations.presentation" 
              :key="index" 
              class="info-item">
              {{ item }}
            </div>
          </div>
        </div>

        <!-- Response -->
        <div v-if="accessibility.accommodations.response?.length" class="accommodation-section">
          <h4 class="section-title">
            <MessageSquare :size="18" class="mr-2" />
            Response
          </h4>
          <div class="info-list">
            <div v-for="(item, index) in accessibility.accommodations.response" 
              :key="index" 
              class="info-item">
              {{ item }}
            </div>
          </div>
        </div>

        <!-- Setting -->
        <div v-if="accessibility.accommodations.setting?.length" class="accommodation-section">
          <h4 class="section-title">
            <Users :size="18" class="mr-2" />
            Setting
          </h4>
          <div class="info-list">
            <div v-for="(item, index) in accessibility.accommodations.setting" 
              :key="index" 
              class="info-item">
              {{ item }}
            </div>
          </div>
        </div>

        <!-- Timing -->
        <div v-if="accessibility.accommodations.timing?.length" class="accommodation-section">
          <h4 class="section-title">
            <Clock :size="18" class="mr-2" />
            Timing
          </h4>
          <div class="info-list">
            <div v-for="(item, index) in accessibility.accommodations.timing" 
              :key="index" 
              class="info-item">
              {{ item }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Differentiation Strategies -->
    <div v-if="accessibility.differentiationStrategies?.length" class="support-card mb-4">
      <div class="card-header">
        <Users :size="20" class="mr-2" />
        Differentiation Strategies
      </div>
      <div class="strategy-grid">
        <div v-for="(strategy, index) in accessibility.differentiationStrategies" 
          :key="index" 
          class="info-item">
          {{ strategy }}
        </div>
      </div>
    </div>

    <!-- Inclusion Strategies -->
    <div v-if="accessibility.inclusionStrategies?.length" class="support-card mb-4">
      <div class="card-header">
        <Heart :size="20" class="mr-2" />
        Inclusion Strategies
      </div>
      <div class="strategy-grid">
        <div v-for="(strategy, index) in accessibility.inclusionStrategies" 
          :key="index" 
          class="info-item">
          {{ strategy }}
        </div>
      </div>
    </div>
  </section>
</template>

# Style Section
<style lang="scss" scoped>
.accessibility-section {
  .text-h5 {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 600;
    color: #5C6970;
  }

  .support-card {
    background-color: rgb(var(--v-theme-background));
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    
    .card-header {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      font-size: 18px;
      color: #5C6970;
      display: flex;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid rgba(120, 192, 229, 0.2);
    }
  }

  .section-title {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 500;
    color: #5C6970;
    font-size: 16px;
    display: flex;
    align-items: center;
    margin-bottom: 16px;
  }

  .vocab-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }

  .vocab-card {
    background-color: rgba(120, 192, 229, 0.05);
    padding: 16px;
    border-radius: 8px;

    .term {
      font-weight: 600;
      font-size: 16px;
      margin-bottom: 8px;
      color: var(--v-theme-primary);
    }

    .definition, .example {
      font-size: 14px;
      margin-bottom: 8px;
      line-height: 1.4;
    }
  }

  .info-item {
    background-color: rgba(120, 192, 229, 0.05);
    padding: 12px 16px;
    border-radius: 6px;
    font-size: 14px;
    line-height: 1.4;
  }

  .accommodations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 24px;
  }

  .info-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  // Dark mode adjustments
  :deep(.v-theme--dark) {
    .support-card {
      background-color: #394246;
    }
    
    .vocab-card, .info-item {
      background-color: rgba(120, 192, 229, 0.08);
    }
  }

  // Mobile optimizations
  @media (max-width: 960px) {
    .vocab-grid, .accommodations-grid {
      grid-template-columns: 1fr;
    }

    .support-card {
      padding: 16px;
    }

    .card-header {
      font-size: 16px;
    }

    .section-title {
      font-size: 15px;
    }
  }
}
</style>