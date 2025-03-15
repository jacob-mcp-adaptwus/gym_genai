// Script Section
<script setup lang="ts">
import { ref, computed } from 'vue';
import { Trash2, Search, BookOpen } from 'lucide-vue-next';
import type { Lesson } from '@/services/lessonService';

interface Props {
  lessons: Lesson[];
  selectedLessonId?: string;
  isLoading?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  lessons: () => [],
  selectedLessonId: undefined,
  isLoading: false
});

const emit = defineEmits<{
  (e: 'select-lesson', lesson: Lesson): void;
  (e: 'delete-lesson', lesson: Lesson): void;
}>();

// Search functionality
const searchQuery = ref('');

// Filtered lessons based on search
const filteredLessons = computed(() => {
  if (!searchQuery.value) return props.lessons;
  
  const query = searchQuery.value.toLowerCase();
  return props.lessons.filter(lesson => 
    lesson.title.toLowerCase().includes(query) ||
    lesson.subject.toLowerCase().includes(query) ||
    lesson.grade.toLowerCase().includes(query)
  );
});

// Helper function to format date
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  });
};

// Subject color mapping
const getSubjectColor = (subject: string): string => {
  const subjectColors: Record<string, string> = {
    'math': 'blue',
    'science': 'green',
    'english': 'purple',
    'history': 'orange',
    'art': 'pink',
    'music': 'deep-purple',
    'physical education': 'red'
  };
  
  return subjectColors[subject.toLowerCase()] || 'primary';
};

// Event handlers
const handleSelectLesson = (lesson: Lesson) => {
  if (!props.isLoading) {
    emit('select-lesson', lesson);
  }
};

const handleDeleteClick = (lesson: Lesson) => {
  emit('delete-lesson', lesson);
};
</script>

<template>
  <div class="lessons-container">
    <!-- Compact Search Section -->
    <div class="search-wrapper">
      <v-text-field
        v-model="searchQuery"
        placeholder="Search..."
        variant="outlined"
        density="compact"
        hide-details
        class="search-field"
      >
        <template v-slot:prepend-inner>
          <Search 
            class="text-medium-emphasis" 
            :size="16" 
          />
        </template>
      </v-text-field>
    </div>

    <!-- Lessons List Section -->
    <div class="lessons-list">
      <v-list 
        v-if="filteredLessons.length > 0" 
        lines="three"
      >
        <v-list-item
          v-for="lesson in filteredLessons"
          :key="lesson.lessonId"
          :active="selectedLessonId === lesson.lessonId"
          @click="handleSelectLesson(lesson)"
          class="lesson-item"
        >
          <!-- Subject Indicator -->
          <div class="subject-indicator" :class="getSubjectColor(lesson.subject)"></div>

          <!-- Lesson Content -->
          <v-list-item-title>
            {{ lesson.title }}
          </v-list-item-title>

          <v-list-item-subtitle>
            <!-- Grade and Subject Tags -->
            <div class="d-flex align-center gap-2">
              <v-chip
                size="x-small"
                color="primary"
                variant="flat"
              >
                {{ lesson.grade }}
              </v-chip>

              <v-chip
                size="x-small"
                :color="getSubjectColor(lesson.subject)"
                variant="flat"
              >
                {{ lesson.subject }}
              </v-chip>
            </div>

            <!-- Last Modified Date -->
            <span class="metadata-line text-caption text-medium-emphasis">
              Last modified: {{ formatDate(lesson.lastModified) }}
            </span>
          </v-list-item-subtitle>

          <!-- Action Buttons -->
          <template v-slot:append>
            <v-btn
              variant="text"
              color="error"
              size="small"
              class="action-button"
              @click.stop="handleDeleteClick(lesson)"
            >
              <Trash2 :size="18" />
            </v-btn>
          </template>
        </v-list-item>
      </v-list>

      <!-- Empty State -->
      <div 
        v-else
        class="empty-state"
      >
        <BookOpen
          :size="48"
          class="empty-icon"
        />
        <h3 class="empty-title">No lessons found</h3>
        <p class="empty-description">
          {{ searchQuery 
            ? 'Try different search terms' 
            : 'Your lesson list is empty' }}
        </p>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
// Main container layout
.lessons-container {
  background-color: rgb(var(--v-theme-background));
  border-radius: 8px;
  height: calc(100vh - 180px);
  display: flex;
  flex-direction: column;
}

// Search section styling
.search-wrapper {
  padding: 12px;
  border-bottom: 1px solid rgba(var(--v-theme-on-surface), 0.12);
  
  .search-field {
    max-width: 300px;
    
    :deep(.v-field__input) {
      min-height: 36px;
      font-family: 'Quicksand', sans-serif;
      font-size: 13px;
    }
    
    :deep(.v-field__outline) {
      border-radius: 6px;
    }
    
    :deep(.v-field__prepend-inner) {
      padding-inline-start: 8px;
    }
  }
}

// List container
.lessons-list {
  overflow-y: auto;
  flex-grow: 1;
  padding: 12px;
  
  &::-webkit-scrollbar {
    width: 4px;
    height: 4px;
  }

  &::-webkit-scrollbar-track {
    background: transparent;
  }

  &::-webkit-scrollbar-thumb {
    background: rgba(var(--v-theme-primary), 0.2);
    border-radius: 2px;
    
    &:hover {
      background: rgba(var(--v-theme-primary), 0.4);
    }
  }
}

// Individual lesson item styling
.lesson-item {
  position: relative;
  margin-bottom: 8px;
  border: 1px solid transparent;
  border-radius: 6px;
  transition: all 0.2s ease;
  min-height: 80px;
  padding: 12px;
  padding-left: 16px;
  overflow: hidden;
  
  // Subject indicator bar
  .subject-indicator {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    transition: width 0.2s ease;
    
    // Subject colors
    &.blue { background-color: rgb(var(--v-theme-blue)); }
    &.green { background-color: rgb(var(--v-theme-green)); }
    &.purple { background-color: rgb(var(--v-theme-purple)); }
    &.orange { background-color: rgb(var(--v-theme-orange)); }
    &.pink { background-color: rgb(var(--v-theme-pink)); }
    &.deep-purple { background-color: rgb(var(--v-theme-deep-purple)); }
    &.red { background-color: rgb(var(--v-theme-red)); }
  }
  
  &:hover {
    background-color: rgba(var(--v-theme-primary), 0.05);
    transform: translateX(4px);
    
    .subject-indicator {
      width: 6px;
    }
  }
  
  &--active {
    background-color: rgba(var(--v-theme-primary), 0.1);
    border-color: rgba(var(--v-theme-primary), 0.2);
    
    .subject-indicator {
      width: 6px;
    }
  }

  // Title styling
  .v-list-item-title {
    font-family: 'Museo Moderno', sans-serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.3px;
    line-height: 1.4;
    margin-bottom: 6px;
  }
  
  // Subtitle and metadata
  .v-list-item-subtitle {
    font-family: 'Quicksand', sans-serif;
    font-size: 12px;
    line-height: 1.5;
    opacity: 0.85;
    
    .metadata-line {
      display: block;
      margin-top: 4px;
      font-size: 11px;
    }
  }
  
  // Chip styling
  .v-chip {
    font-family: 'Quicksand', sans-serif;
    font-size: 11px;
    font-weight: 500;
    height: 18px;
    
    &.v-chip--size-x-small {
      font-size: 10px;
    }
  }
  
  // Action button
  .action-button {
    opacity: 0.6;
    transition: all 0.2s ease;
    
    &:hover {
      opacity: 1;
      transform: scale(1.1);
    }
  }
}

// Empty state styling
.empty-state {
  text-align: center;
  padding: 32px 24px;
  
  .empty-icon {
    color: rgb(var(--v-theme-primary));
    opacity: 0.7;
    margin-bottom: 12px;
  }
  
  .empty-title {
    font-family: 'Museo Moderno', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: rgb(var(--v-theme-primary));
    margin-bottom: 6px;
  }
  
  .empty-description {
    font-family: 'Quicksand', sans-serif;
    font-size: 13px;
    color: rgba(var(--v-theme-on-surface), 0.7);
    max-width: 200px;
    margin: 0 auto;
    line-height: 1.5;
  }
}

// Dark mode adjustments
:deep(.v-theme--dark) {
  .lesson-item {
    &:hover {
      background-color: rgba(var(--v-theme-primary), 0.1);
    }
    
    &--active {
      background-color: rgba(var(--v-theme-primary), 0.15);
    }
  }

  .empty-state {
    .empty-icon {
      opacity: 0.5;
    }
  }
}

// Responsive adjustments
@media (max-width: 960px) {
  .lessons-container {
    height: auto;
    max-height: 600px;
  }
  
  .search-wrapper {
    padding: 8px;
    
    .search-field {
      max-width: 100%;
    }
  }
  
  .lesson-item {
    padding: 10px;
    min-height: 70px;
    
    &:hover {
      transform: none;
    }
  }
  
  .empty-state {
    padding: 24px 16px;
  }
}
</style>