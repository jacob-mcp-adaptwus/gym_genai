// LessonChat.vue
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import ChatHistory from '@/components/apps/lessons/ChatSections/ChatHistory.vue';
import ChatInput from '@/components/apps/lessons/ChatSections/ChatInput.vue';
import { GripHorizontal } from 'lucide-vue-next';

interface ChatMessage {
  type: 'user' | 'system';
  content: string;
  timestamp: Date;
}

interface Props {
  isGenerating?: boolean;
  initialMessage?: string;
  selectedContexts?: string[];
}

const props = withDefaults(defineProps<Props>(), {
  isGenerating: false,
  initialMessage: '',
  selectedContexts: () => []
});

const emit = defineEmits<{
  (e: 'send-message', message: string): void;
  (e: 'resize', height: number): void;
}>();

// State
const messages = ref<ChatMessage[]>([]);
const chatHeight = ref(300); // Default height
const isResizing = ref(false);
const startY = ref(0);
const startHeight = ref(0);

// Methods
const addSystemMessage = (content: string) => {
  if (!content) return;
  
  messages.value.push({
    type: 'system',
    content,
    timestamp: new Date()
  });
};

const handleSendMessage = (message: string) => {
  // Add user message to chat
  messages.value.push({
    type: 'user',
    content: message,
    timestamp: new Date()
  });
  
  // Emit message to parent for processing
  emit('send-message', message);
};

// Resize handlers
const startResize = (event: MouseEvent) => {
  isResizing.value = true;
  startY.value = event.clientY;
  startHeight.value = chatHeight.value;
  document.addEventListener('mousemove', handleResize);
  document.addEventListener('mouseup', stopResize);
};

const handleResize = (event: MouseEvent) => {
  if (!isResizing.value) return;
  
  const deltaY = event.clientY - startY.value;
  const newHeight = Math.max(200, Math.min(800, startHeight.value + deltaY));
  chatHeight.value = newHeight;
  emit('resize', newHeight);
};

const stopResize = () => {
  isResizing.value = false;
  document.removeEventListener('mousemove', handleResize);
  document.removeEventListener('mouseup', stopResize);
};

// Cleanup
onUnmounted(() => {
  document.removeEventListener('mousemove', handleResize);
  document.removeEventListener('mouseup', stopResize);
});

// Initialize with system message if provided
if (props.initialMessage) {
  addSystemMessage(props.initialMessage);
}

// Expose methods to parent
defineExpose({
  addSystemMessage,
  messages
});
</script>
<!-- LessonChat.vue -->
<template>
  <div class="lesson-chat" :style="{ height: chatHeight + 'px' }">
    <!-- Main Chat Layout -->
    <div class="chat-container">
      <!-- Chat History Section -->
      <ChatHistory
        :messages="messages"
        :is-generating="isGenerating"
        :selected-contexts="selectedContexts"
      />

      <!-- Chat Input Section -->
      <ChatInput
        :is-generating="isGenerating"
        placeholder="How would you like to improve this lesson plan?"
        @send="handleSendMessage"
      />
    </div>

    <!-- Loading Overlay -->
    <div 
      v-if="isGenerating"
      class="loading-overlay"
      role="alert"
      aria-busy="true"
    >
      <v-progress-circular
        indeterminate
        color="primary"
        size="32"
      />
    </div>

    <!-- Resize Control -->
    <div class="resize-control" @mousedown="startResize">
      <GripHorizontal
        :size="16"
        class="resize-icon"
      />
    </div>
  </div>
</template>
<style scoped>
.lesson-chat {
  height: 100%;
  position: relative;
  background-color: white;
  border-radius: 8px;
  overflow: visible;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: height 0.1s ease;
}

.chat-container {
  height: calc(100% - 20px);
  position: relative;
  overflow: hidden;
  background-color: white;
  display: grid;
  grid-template-columns: 65% 35%;
  gap: 1px;
  border-radius: 8px;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  backdrop-filter: blur(2px);
}

.resize-control {
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: ns-resize;
  background-color: #f0f0f0;
  border-radius: 0 0 4px 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;
  z-index: 10;
}

.resize-control:hover {
  background-color: #e0e0e0;
  transform: translateX(-50%) scale(1.05);
}

.resize-control:active {
  background-color: #d0d0d0;
  transform: translateX(-50%) scale(0.95);
}

.resize-icon {
  color: #666;
  opacity: 0.7;
  transition: opacity 0.2s ease;
}

.resize-control:hover .resize-icon {
  opacity: 1;
}

/* Dark theme support */
:deep(.v-theme--dark) {
  .lesson-chat {
    background-color: #1a1a1a;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }

  .chat-container {
    background-color: #1a1a1a;
  }

  .loading-overlay {
    background-color: rgba(26, 26, 26, 0.8);
  }

  .resize-control {
    background-color: #2a2a2a;
  }

  .resize-control:hover {
    background-color: #333333;
  }

  .resize-control:active {
    background-color: #404040;
  }

  .resize-icon {
    color: #999;
  }
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .chat-container {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr auto;
  }

  .chat-history {
    order: 1;
    overflow-y: auto;
    padding-bottom: 120px;
  }

  .chat-input {
    order: 2;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    max-height: 200px;
    background-color: white;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    z-index: 10;
  }
}

/* Print styles */
@media print {
  .lesson-chat {
    box-shadow: none;
  }

  .chat-input {
    display: none;
  }

  .loading-overlay {
    display: none;
  }

  .resize-control {
    display: none;
  }
}
</style>
