// Script Section
<script setup lang="ts">
import { Target, List, Globe, CheckCircle } from 'lucide-vue-next';

interface Objectives {
    content: string[];
    language: string[];
    mathematical_practice: string[];
    success_criteria: string[];
}

interface Props {
    objectives: Objectives;
}

const props = defineProps<Props>();
</script>
# Template Section
<template>
  <div class="objectives-section">
    <h3 class="text-h6 mb-4">
      <Target :size="20" class="mr-2" />
      Lesson Objectives
    </h3>

    <!-- Content Objectives -->
    <div class="objective-group mb-6">
      <h4 class="objective-title">
        <List :size="18" class="mr-2" />
        Content Objectives
      </h4>
      <v-list>
        <v-list-item
          v-for="(objective, index) in objectives.content"
          :key="index"
          density="compact"
          class="objective-item"
        >
          <template v-slot:prepend>
            <div class="objective-bullet"></div>
          </template>
          {{ objective }}
        </v-list-item>
      </v-list>
    </div>

    <!-- Language Objectives -->
    <div class="objective-group mb-6">
      <h4 class="objective-title">
        <Globe :size="18" class="mr-2" />
        Language Objectives
      </h4>
      <v-list>
        <v-list-item
          v-for="(objective, index) in objectives.language"
          :key="index"
          density="compact"
          class="objective-item"
        >
          <template v-slot:prepend>
            <div class="objective-bullet"></div>
          </template>
          {{ objective }}
        </v-list-item>
      </v-list>
    </div>

    <!-- Mathematical Practice -->
    <div class="objective-group mb-6">
      <h4 class="objective-title">
        <Target :size="18" class="mr-2" />
        Mathematical Practice
      </h4>
      <v-list>
        <v-list-item
          v-for="(practice, index) in objectives.mathematical_practice"
          :key="index"
          density="compact"
          class="objective-item"
        >
          <template v-slot:prepend>
            <div class="objective-bullet"></div>
          </template>
          {{ practice }}
        </v-list-item>
      </v-list>
    </div>

    <!-- Success Criteria -->
    <div class="objective-group">
      <h4 class="objective-title">
        <CheckCircle :size="18" class="mr-2" />
        Success Criteria
      </h4>
      <v-list>
        <v-list-item
          v-for="(criteria, index) in objectives.success_criteria"
          :key="index"
          density="compact"
          class="objective-item"
        >
          <template v-slot:prepend>
            <div class="objective-bullet"></div>
          </template>
          {{ criteria }}
        </v-list-item>
      </v-list>
    </div>
  </div>
</template>
# Style Section
<style lang="scss" scoped>
.objectives-section {
  .text-h6 {
    font-family: 'Museo Moderno', sans-serif;
    color: #5C6970;
    display: flex;
    align-items: center;
  }
}

.objective-group {
  .objective-title {
    font-family: 'Quicksand', sans-serif;
    font-size: 16pt;
    font-weight: 600;
    margin-bottom: 12px;
    color: #78C0E5;
    display: flex;
    align-items: center;
  }
}

.objective-item {
  font-family: 'Quicksand', sans-serif;
  font-size: 14pt;
  line-height: 1.5;
  padding: 8px 16px;
  
  .objective-bullet {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: #78C0E5;
    margin-right: 12px;
  }
}

:deep(.v-theme--dark) {
  .objective-group {
    .objective-title {
      color: #B7E6F2;
    }
  }
  
  .objective-item {
    .objective-bullet {
      background-color: #B7E6F2;
    }
  }
}

@media (max-width: 960px) {
  .objective-group {
    .objective-title {
      font-size: 14pt;
    }
  }

  .objective-item {
    font-size: 12pt;
    padding: 6px 12px;
  }
}
</style>