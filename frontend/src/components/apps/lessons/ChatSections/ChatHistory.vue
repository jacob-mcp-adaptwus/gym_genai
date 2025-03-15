// ChatHistory.vue
<script setup lang="ts">
import { ref, watch, nextTick, onMounted, computed, onUnmounted } from 'vue';
import { 
  User, 
  Loader, 
  MessageCircle,
  MessagesSquare,
  ArrowDown
} from 'lucide-vue-next';
import mathtilda from '@/assets/images/users/mathtilda-2.png';
import PerfectScrollbar from 'perfect-scrollbar';
import 'perfect-scrollbar/css/perfect-scrollbar.css';

interface ChatMessage {
  type: 'user' | 'system';
  content: string;
  timestamp: Date;
}

interface Props {
  messages: ChatMessage[];
  isGenerating?: boolean;
  selectedContexts?: string[];
}

const props = withDefaults(defineProps<Props>(), {
  isGenerating: false,
  selectedContexts: () => []
});

// State management
const chatContainer = ref<HTMLElement | null>(null);
const isScrolledUp = ref(false);
const showScrollButton = ref(false);
const lastScrollPosition = ref(0);
const isNearBottom = ref(true);
let ps: PerfectScrollbar | null = null;

// Computed values for scroll behavior
const scrollThreshold = 100; // pixels from bottom to trigger auto-scroll

const isAtBottom = computed(() => {
  if (!chatContainer.value) return true;
  const { scrollHeight, scrollTop, clientHeight } = chatContainer.value;
  return scrollHeight - scrollTop - clientHeight < scrollThreshold;
});

// Scroll handling methods
const handleScroll = () => {
  if (!chatContainer.value) return;
  
  const { scrollHeight, scrollTop, clientHeight } = chatContainer.value;
  const currentPosition = scrollTop;
  
  // Update scroll direction and position
  isScrolledUp.value = currentPosition < lastScrollPosition.value;
  lastScrollPosition.value = currentPosition;
  
  // Show/hide scroll button based on position and direction
  isNearBottom.value = scrollHeight - scrollTop - clientHeight < scrollThreshold;
  showScrollButton.value = !isNearBottom.value;
};

const scrollToBottom = async (force = false) => {
  await nextTick();
  if (!chatContainer.value) return;
  
  if (force || isAtBottom.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    showScrollButton.value = false;
    isNearBottom.value = true;
  }
};

// Format timestamp
const formatTimestamp = (date: Date): string => {
  return date.toLocaleTimeString([], { 
    hour: '2-digit', 
    minute: '2-digit',
    hour12: true 
  });
};

// Display names for contexts
const getContextDisplayName = (context: string): string => {
  const displayNames: Record<string, string> = {
    metadata: 'Metadata',
    pedagogicalContext: 'Pedagogical Context',
    objectives: 'Objectives',
    lessonFlow: 'Lesson Flow',
    markupProblemSets: 'Problem Sets',
    assessments: 'Assessments',
    accessibility: 'Accessibility',
    studentProfile: 'Student Profile'
  };
  return displayNames[context] || context;
};

// Initialize perfect-scrollbar
onMounted(() => {
  if (chatContainer.value) {
    ps = new PerfectScrollbar(chatContainer.value);
    chatContainer.value.addEventListener('scroll', handleScroll);
    // Initial scroll to bottom
    scrollToBottom(true);
  }
});

// Watch for new messages and update scroll
watch(() => props.messages.length, async () => {
  await nextTick();
  scrollToBottom(true); // Force scroll to bottom for new messages
  ps?.update();
});

// Cleanup
onUnmounted(() => {
  if (ps) {
    ps.destroy();
    ps = null;
  }
  if (chatContainer.value) {
    chatContainer.value.removeEventListener('scroll', handleScroll);
  }
});
</script>
<!-- ChatHistory.vue -->
<template>
    <div class="chat-history">
      <!-- Header -->
      <div class="chat-header">
        <div class="header-content">
          <MessagesSquare class="icon" />
          <span class="header-title">Ask Tilly</span>
        </div>
        <div class="status-chip">
          <v-chip
            size="small"
            :color="isGenerating ? 'warning' : 'success'"
          >
            <Loader
              v-if="isGenerating"
              class="status-icon spinning"
            />
            <MessageCircle
              v-else
              class="status-icon"
            />
            {{ isGenerating ? 'Generating...' : 'Ready' }}
          </v-chip>
        </div>
      </div>
  
      <!-- Selected Contexts -->
      <div v-if="selectedContexts.length > 0" class="contexts-container">
        <div class="contexts-label">
          <span>Selected Contexts:</span>
        </div>
        <div class="contexts-chips">
          <v-chip
            v-for="context in selectedContexts"
            :key="context"
            size="small"
            color="primary"
            variant="flat"
          >
            {{ getContextDisplayName(context) }}
          </v-chip>
        </div>
      </div>
  
      <!-- Messages Container -->
      <div 
        ref="chatContainer"
        class="messages-container"
        @scroll="handleScroll"
      >
        <div
          v-for="(message, index) in messages"
          :key="index"
          class="message-wrapper"
          :class="message.type === 'user' ? 'user-message' : 'system-message'"
        >
          <!-- Avatar -->
          <div class="avatar-container">
            <v-avatar size="32" :class="message.type === 'system' ? 'system-avatar' : 'user-avatar'">
              <v-img 
                v-if="message.type === 'system'"
                :src="mathtilda"
                alt="Mathtilda AI Assistant"
                cover
              />
              <User 
                v-else
                class="avatar-icon"
              />
            </v-avatar>
          </div>
  
          <!-- Message Content -->
          <div 
            class="message-content"
            :class="message.type === 'system' ? 'system-bubble' : 'user-bubble'"
          >
            <div class="message-text">{{ message.content }}</div>
            <div class="message-timestamp">
              {{ formatTimestamp(message.timestamp) }}
            </div>
          </div>
        </div>
      </div>
  
      <!-- Scroll to Bottom Button -->
      <button
        v-show="showScrollButton"
        @click="scrollToBottom(true)"
        class="scroll-button"
      >
        <ArrowDown class="scroll-icon" />
      </button>
    </div>
  </template>
  <style>
  
.chat-history {
  display: flex;
  flex-direction: column;
  height: 100%;
  border-right: 1px solid #e0e0e0;
  position: relative;
  background-color: white;
  overflow: hidden; /* Contain the scroll */
}

.chat-header {
  padding: 1rem;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  z-index: 2;
  flex-shrink: 0; /* Prevent header from shrinking */

  .header-content {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .header-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1a1a1a;
  }

  .icon {
    width: 1.25rem;
    height: 1.25rem;
  }
}

.status-chip {
  .status-icon {
    width: 1rem;
    height: 1rem;
    margin-right: 0.25rem;

    &.spinning {
      animation: spin 1s linear infinite;
    }
  }
}

.contexts-container {
  padding: 1rem;
  border-bottom: 1px solid #e0e0e0;
  background-color: #f8f9fa;
  z-index: 2;
  flex-shrink: 0; /* Prevent contexts from shrinking */

  .contexts-label {
    margin-bottom: 0.25rem;
    font-size: 0.875rem;
    color: #6b7280;
  }

  .contexts-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  position: relative;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  min-height: 0; /* Allow container to scroll */
}

.message-wrapper {
  flex-shrink: 0;
  margin-bottom: 1rem;
  display: flex;
  gap: 0.75rem;

  &.user-message {
    flex-direction: row-reverse;
  }
}

.avatar-container {
  flex-shrink: 0;

  .system-avatar {
    background-color: #e5f2ff;
  }

  .user-avatar {
    background-color: #f0f0f0;
  }

  .avatar-icon {
    width: 20px;
    height: 20px;
    color: #666;
  }
}

.message-content {
  max-width: 70%;
  padding: 0.75rem 1rem;
  border-radius: 1rem;
  position: relative;

  &.system-bubble {
    background-color: #f8f9fa;
    border-top-left-radius: 0.25rem;
  }

  &.user-bubble {
    background-color: #e5f2ff;
    border-top-right-radius: 0.25rem;
  }

  .message-text {
    font-size: 0.875rem;
    line-height: 1.5;
    white-space: pre-wrap;
    word-break: break-word;
  }

  .message-timestamp {
    font-size: 0.75rem;
    color: #6b7280;
    margin-top: 0.25rem;
    text-align: right;
  }
}

.scroll-button {
  position: absolute;
  bottom: 1rem;
  right: 1rem;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 3;

  &:hover {
    background-color: #f8f9fa;
    transform: translateY(-2px);
  }

  .scroll-icon {
    width: 1.25rem;
    height: 1.25rem;
    color: #666;
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Dark theme support */
:deep(.v-theme--dark) {
  .chat-history {
    background-color: #1a1a1a;
    border-color: rgba(255, 255, 255, 0.1);
  }

  .chat-header {
    background-color: #1a1a1a;
    border-color: rgba(255, 255, 255, 0.1);

    .header-title {
      color: white;
    }
  }

  .contexts-container {
    background-color: #2d2d2d;
    border-color: rgba(255, 255, 255, 0.1);
  }

  .message-content {
    &.system-bubble {
      background-color: #2d2d2d;
      color: white;
    }

    &.user-bubble {
      background-color: #1e3a5f;
      color: white;
    }

    .message-timestamp {
      color: #a0aec0;
    }
  }

  .scroll-button {
    background-color: #2d2d2d;
    
    &:hover {
      background-color: #3d3d3d;
    }

    .scroll-icon {
      color: #a0aec0;
    }
  }
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .messages-container {
    padding: 0.75rem;
  }

  .message-content {
    max-width: 85%;
  }

  .scroll-button {
    bottom: 0.75rem;
    right: 0.75rem;
  }
}
  </style>