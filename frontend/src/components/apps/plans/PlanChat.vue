<script setup lang="ts">
import { ref, onMounted, nextTick, watch } from 'vue';
import { Send, ChevronDown, ChevronUp } from 'lucide-vue-next';

const props = defineProps<{
  isGenerating: boolean;
  initialMessage?: string;
  selectedContexts?: string[];
}>();

const emit = defineEmits<{
  (e: 'send-message', message: string): void;
  (e: 'resize', height: number): void;
}>();

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'system' | 'assistant';
  timestamp: Date;
}

// Chat state
const messages = ref<Message[]>([]);
const newMessage = ref('');
const chatContainer = ref<HTMLElement | null>(null);
const isExpanded = ref(true);
const defaultHeight = 300;
const expandedHeight = 500;

// Initialize chat with welcome message
onMounted(() => {
  if (props.initialMessage) {
    messages.value.push({
      id: generateId(),
      text: props.initialMessage,
      sender: 'assistant',
      timestamp: new Date(),
    });
  }
  
  // Set initial height
  emit('resize', isExpanded.value ? expandedHeight : defaultHeight);
});

// Watch for changes in selected contexts
watch(() => props.selectedContexts, () => {
  scrollToBottom();
}, { deep: true });

// Methods
const sendMessage = () => {
  if (!newMessage.value.trim() || props.isGenerating) return;
  
  const message = newMessage.value.trim();
  
  // Add user message to chat
  messages.value.push({
    id: generateId(),
    text: message,
    sender: 'user',
    timestamp: new Date(),
  });
  
  // Clear input
  newMessage.value = '';
  
  // Scroll to bottom
  scrollToBottom();
  
  // Emit message to parent
  emit('send-message', message);
};

const addSystemMessage = (message: string) => {
  messages.value.push({
    id: generateId(),
    text: message,
    sender: 'system',
    timestamp: new Date(),
  });
  
  scrollToBottom();
};

const scrollToBottom = async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

const generateId = () => {
  return Math.random().toString(36).substring(2, 15);
};

const formatTime = (date: Date) => {
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value;
  emit('resize', isExpanded.value ? expandedHeight : defaultHeight);
};

// Expose methods to parent
defineExpose({
  addSystemMessage,
});
</script>

<template>
  <div class="chat-container" :class="{ 'expanded': isExpanded }">
    <!-- Chat Header -->
    <div class="chat-header">
      <div class="d-flex align-center">
        <v-icon icon="mdi-dumbbell" color="primary" class="mr-2"></v-icon>
        <span class="text-subtitle-1 font-weight-medium">Bodybuilding Coach</span>
      </div>
      
      <div class="d-flex align-center">
        <v-chip
          v-for="context in selectedContexts"
          :key="context"
          size="x-small"
          color="primary"
          variant="outlined"
          class="mr-1"
        >
          {{ context }}
        </v-chip>
        
        <v-btn
          icon
          variant="text"
          size="small"
          @click="toggleExpand"
          class="ml-2"
        >
          <ChevronUp v-if="isExpanded" :size="20" />
          <ChevronDown v-else :size="20" />
        </v-btn>
      </div>
    </div>
    
    <!-- Chat Messages -->
    <div ref="chatContainer" class="chat-messages">
      <div
        v-for="message in messages"
        :key="message.id"
        class="message"
        :class="message.sender"
      >
        <div class="message-content">
          <div class="message-text" v-html="message.text.replace(/\n/g, '<br>')"></div>
          <div class="message-time">{{ formatTime(message.timestamp) }}</div>
        </div>
      </div>
      
      <div v-if="isGenerating" class="message assistant">
        <div class="message-content">
          <div class="message-text">
            <v-progress-linear indeterminate color="primary" class="mt-2"></v-progress-linear>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Chat Input -->
    <div class="chat-input">
      <v-textarea
        v-model="newMessage"
        placeholder="Ask about your workout plan..."
        rows="1"
        auto-grow
        hide-details
        density="compact"
        variant="outlined"
        @keydown.enter.prevent="sendMessage"
      ></v-textarea>
      
      <v-btn
        icon
        color="primary"
        :disabled="!newMessage.trim() || isGenerating"
        @click="sendMessage"
        class="send-button"
      >
        <Send :size="20" />
      </v-btn>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: #f8f9fa;
  border-radius: 12px;
  overflow: hidden;
  transition: height 0.3s ease;
  
  &.expanded {
    height: v-bind('expandedHeight + "px"');
  }
  
  .chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background-color: white;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    font-family: "Museo Moderno", sans-serif;
  }
  
  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    
    .message {
      display: flex;
      max-width: 80%;
      
      &.user {
        align-self: flex-end;
        
        .message-content {
          background-color: #78c0e5;
          color: white;
          border-radius: 12px 12px 0 12px;
          
          .message-time {
            color: rgba(255, 255, 255, 0.8);
          }
        }
      }
      
      &.assistant {
        align-self: flex-start;
        
        .message-content {
          background-color: white;
          border-radius: 12px 12px 12px 0;
        }
      }
      
      &.system {
        align-self: center;
        max-width: 90%;
        
        .message-content {
          background-color: #f0f0f0;
          border-radius: 12px;
          font-style: italic;
          color: #666;
        }
      }
      
      .message-content {
        padding: 12px 16px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        
        .message-text {
          font-size: 14px;
          line-height: 1.5;
          word-break: break-word;
        }
        
        .message-time {
          font-size: 10px;
          margin-top: 4px;
          text-align: right;
          color: rgba(0, 0, 0, 0.5);
        }
      }
    }
  }
  
  .chat-input {
    display: flex;
    align-items: flex-end;
    padding: 12px 16px;
    background-color: white;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    
    .v-textarea {
      flex: 1;
      
      :deep(.v-field__input) {
        padding-top: 8px;
        padding-bottom: 8px;
        min-height: unset;
      }
    }
    
    .send-button {
      margin-left: 8px;
    }
  }
}
</style> 