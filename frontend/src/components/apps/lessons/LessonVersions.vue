<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import { useLessonStore } from '@/stores/lessons';
import { Clock, Tag, History, Search } from 'lucide-vue-next';
import type { Lesson, LessonVersion } from '@/services/lessonService';

interface Props {
  modelValue: boolean;
  lessonId?: string;
}

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void;
  (e: 'select-version', version: LessonVersion): void;
}>();

const lessonStore = useLessonStore();
const searchQuery = ref('');
const error = ref<string | null>(null);

const filteredVersions = computed(() => {
  if (!searchQuery.value) return lessonStore.lessonVersions;
  
  const query = searchQuery.value.toLowerCase();
  return lessonStore.lessonVersions.filter(version => 
    version.title.toLowerCase().includes(query) ||
    version.profileId.toLowerCase().includes(query)
  );
});

const handleClose = () => {
  emit('update:modelValue', false);
};

const handleSelectVersion = (version: LessonVersion) => {
  // Convert LessonVersion to Lesson format
  const lesson: Lesson = {
    lessonId: version.lessonId,
    title: version.title,
    subject: version.subject,
    grade: version.grade,
    lastModified: version.timestamp,
    status: 'saved',
    content: version.content
  };
  
  emit('select-version', version);
};

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};
</script>
<template>
    <v-dialog
      :model-value="modelValue"
      @update:model-value="emit('update:modelValue', $event)"
      max-width="800"
      persistent
      class="versions-dialog"
    >
      <v-card>
        <!-- Dialog Header -->
        <v-card-title class="d-flex justify-space-between align-center pa-4">
          <span class="text-h5">Lesson Versions</span>
          <v-btn
            icon
            variant="text"
            @click="handleClose"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
   
        <v-divider></v-divider>
   
        <v-card-text class="pa-4">
          <!-- Search -->
          <v-text-field
            v-model="searchQuery"
            label="Search versions"
            variant="outlined"
            density="comfortable"
            hide-details
            class="mb-4"
          >
            <template v-slot:prepend-inner>
              <Search :size="20" />
            </template>
          </v-text-field>
   
          <!-- Versions List -->
          <v-list v-if="filteredVersions.length > 0" lines="two">
            <v-list-item
              v-for="version in filteredVersions"
              :key="`${version.lessonId}-${version.version}`"
              @click="handleSelectVersion(version)"
              class="mb-2 rounded version-item"
            >
              <v-list-item-title class="d-flex align-center gap-2 mb-1">
                <v-chip size="small" color="primary">
                  <template v-slot:prepend>
                    <Tag :size="14" />
                  </template>
                  v{{ version.version }}
                </v-chip>
                {{ version.title }}
              </v-list-item-title>
   
              <v-list-item-subtitle>
                <div class="d-flex align-center gap-2">
                  <v-chip size="x-small" :color="version.profileId ? 'info' : 'grey'">
                    {{ version.profileId || 'No Profile' }}
                  </v-chip>
                  <span class="text-caption text-medium-emphasis">
                    <Clock :size="14" class="mr-1" />
                    {{ formatDate(version.timestamp) }}
                  </span>
                </div>
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>
   
          <!-- Empty State -->
          <div v-else class="text-center pa-4">
            <History :size="48" class="mb-4 text-primary" />
            <h3 class="text-h6 mb-2">No versions found</h3>
            <p class="text-medium-emphasis">
              {{ searchQuery ? 'Try different search terms' : 'No versions available for this lesson' }}
            </p>
          </div>
        </v-card-text>
      </v-card>
    </v-dialog>
   </template>
   <style lang="scss" scoped>
   .versions-dialog {
    .v-card {
      border-radius: 8px;
      background-color: rgb(var(--v-theme-background));
      
      .v-card-title {
        font-family: 'Museo Moderno', sans-serif;
        font-size: 22pt;
        color: #5C6970;
      }
    }
   
    .v-list {
      .version-item {
        margin-bottom: 8px;
        padding: 12px;
        border-radius: 6px;
        transition: all 0.2s ease;
        
        &:hover {
          background-color: rgba(120, 192, 229, 0.05);
          transform: translateX(4px);
        }
   
        .v-list-item-title {
          font-family: 'Quicksand', sans-serif;
          font-weight: 600;
          font-size: 16pt;
        }
   
        .v-list-item-subtitle {
          font-family: 'Quicksand', sans-serif;
          font-size: 14pt;
        }
   
        .v-chip {
          background-color: #78C0E5;
          
          &.v-chip--size-x-small {
            font-size: 12pt;
          }
        }
      }
    }
   
    .v-text-field {
      :deep(.v-field__input) {
        padding: 8px 16px;
        min-height: 48px;
        font-family: 'Quicksand', sans-serif;
      }
      
      :deep(.v-field__outline) {
        border-radius: 8px;
      }
    }
   
    .text-center {
      .text-h6 {
        font-family: 'Museo Moderno', sans-serif;
        color: #78C0E5;
      }
   
      p {
        font-family: 'Quicksand', sans-serif;
        color: #B7BBBE;
      }
   
      .lucide {
        color: #78C0E5;
        opacity: 0.7;
      }
    }
   }
   
   @media (max-width: 960px) {
    .versions-dialog {
      margin: 12px;
   
      .v-card-title {
        font-size: 18pt;
      }
   
      .version-item {
        .v-list-item-title {
          font-size: 14pt;
        }
   
        .v-list-item-subtitle {
          font-size: 12pt;
        }
   
        &:hover {
          transform: none;
        }
      }
    }
   }
   
   :deep(.v-theme--dark) {
    .versions-dialog {
      .v-card {
        background-color: #394246;
      }
   
      .version-item:hover {
        background-color: rgba(120, 192, 229, 0.1);
      }
    }
   }
   </style>