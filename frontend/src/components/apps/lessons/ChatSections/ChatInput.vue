// ChatInput.vue
<script setup lang="ts">
import { ref } from 'vue';
import { Send } from 'lucide-vue-next';

interface Props {
  isGenerating?: boolean;
  placeholder?: string;
}

const props = withDefaults(defineProps<Props>(), {
  isGenerating: false,
  placeholder: 'Type your message...'
});

const emit = defineEmits<{
  (e: 'send', message: string): void;
}>();

// State
const newMessage = ref('');
const textareaHeight = ref('100px'); // Default height for textarea

// Methods
const sendMessage = () => {
  if (!newMessage.value.trim() || props.isGenerating) return;
  
  emit('send', newMessage.value);
  newMessage.value = '';
};

const handleKeyPress = (event: KeyboardEvent) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
};

// Method to handle textarea resize
const handleResize = (element: HTMLTextAreaElement) => {
  const minHeight = 100; // Minimum height in pixels
  const maxHeight = 200; // Maximum height in pixels
  
  // Reset height to recalculate
  element.style.height = 'auto';
  
  // Calculate new height
  const newHeight = Math.min(Math.max(element.scrollHeight, minHeight), maxHeight);
  element.style.height = `${newHeight}px`;
  textareaHeight.value = `${newHeight}px`;
};
</script>
<!-- ChatInput.vue -->
<template>
  <div class="chat-input-container">
    <!-- Main content area -->
    <div class="input-content">
      <!-- Send button positioned above textarea -->
      Chat with Tilly
      <!-- Helper text -->
      <div class="input-helper" aria-live="polite">
        <!-- Press Enter to send, Shift + Enter for new line -->
      </div>
    </div>

    <!-- Sticky textarea footer -->
    <div class="textarea-footer">
      <v-btn
          @click="sendMessage"
          :disabled="!newMessage.trim() || isGenerating"
          color="primary"
          class="send-button"
          :aria-label="isGenerating ? 'Message generation in progress' : 'Send message'"
        >
          <Send class="send-icon" />
          <span class="send-text">Send Message</span>
        </v-btn>

      <v-textarea
        v-model="newMessage"
        :placeholder="placeholder"
        variant="outlined"
        density="comfortable"
        hide-details
        auto-grow
        rows="1"
        row-height="20"
        max-rows="4"
        @keydown="handleKeyPress"
        :disabled="isGenerating"
        class="message-textarea"
        @input="(e: Event) => handleResize((e.target as HTMLTextAreaElement))"
      />
    </div>
  </div>
</template>
<style>
.chat-input-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  position: relative;
  background-color: white;
}

.input-content {
  flex: 1;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.button-wrapper {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 0.5rem;
}

.send-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background-color: #78C0E5;
  transition: all 0.2s ease;

  &:not(:disabled) {
    &:hover {
      background-color: darken(#78C0E5, 10%);
      transform: translateY(-1px);
    }

    &:active {
      transform: translateY(0);
    }
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .send-icon {
    width: 1.25rem;
    height: 1.25rem;
  }

  .send-text {
    font-family: 'Quicksand', sans-serif;
    font-size: 0.875rem;
  }
}

.input-helper {
  text-align: right;
  font-size: 0.75rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.textarea-footer {
  position: sticky;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: white;
  padding: 1rem;
  border-top: 1px solid #e0e0e0;
  z-index: 10;

  .message-textarea {
    :deep(.v-field) {
      background-color: white;
    }

    :deep(.v-field__input) {
      min-height: unset !important;
      padding: 0.75rem;
      font-size: 0.875rem;
      line-height: 1.5;
      resize: none;
    }

    :deep(.v-field__outline) {
      border-color: #e0e0e0;
      
      &__start,
      &__end,
      &__notch {
        border-color: #e0e0e0;
      }
    }

    &:hover {
      :deep(.v-field__outline) {
        border-color: #b0b0b0;
      }
    }

    &:focus-within {
      :deep(.v-field__outline) {
        border-color: #78C0E5;
        border-width: 2px;
      }
    }
  }
}

/* Dark theme support */
:deep(.v-theme--dark) {
  .chat-input-container,
  .textarea-footer {
    background-color: #1a1a1a;
  }

  .textarea-footer {
    border-color: rgba(255, 255, 255, 0.1);

    .message-textarea {
      :deep(.v-field) {
        background-color: #2d2d2d;
      }

      :deep(.v-field__input) {
        color: white;
      }

      :deep(.v-field__outline) {
        border-color: rgba(255, 255, 255, 0.1);
      }

      &:hover {
        :deep(.v-field__outline) {
          border-color: rgba(255, 255, 255, 0.2);
        }
      }
    }
  }

  .input-helper {
    color: #a0aec0;
  }
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .input-content {
    padding: 0.75rem;
  }

  .textarea-footer {
    padding: 0.75rem;
  }

  .send-button {
    padding: 0.5rem 1rem;

    .send-text {
      display: none;
    }
  }
}

/* Perfect Scrollbar customization */
.ps {
  .ps__rail-y {
    background-color: transparent !important;
    width: 6px;
    
    .ps__thumb-y {
      background-color: rgba(120, 192, 229, 0.2);
      border-radius: 3px;
      width: 6px;
      
      &:hover {
        background-color: rgba(120, 192, 229, 0.4);
      }
    }
  }
}
</style>