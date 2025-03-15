import { defineStore } from 'pinia';
import { chatService, type ChatMessage, type ChatResponse, type AnalyzeResponse } from '../services/chatService';

interface ChatState {
  messages: Record<string, ChatMessage[]>; // Keyed by lessonId
  isLoading: boolean;
  error: string | null;
  analysis: AnalyzeResponse | null;
  currentAnalysis: AnalyzeResponse | null;
}

export const useChatStore = defineStore('chats', {
  state: (): ChatState => ({
    messages: {},
    isLoading: false,
    error: null,
    analysis: null,
    currentAnalysis: null
  }),

  getters: {
    getChatHistory: (state) => {
      return (lessonId: string) => state.messages[lessonId] || [];
    }
  },

  actions: {
    async sendMessage(lessonId: string, message: string, existingPlan?: string, analysis?: AnalyzeResponse) {
      this.isLoading = true;
      try {
        const response = await chatService.sendMessage(message, existingPlan, lessonId, analysis);
        // Initialize messages array for this lesson if it doesn't exist
        if (!this.messages[lessonId]) {
          this.messages[lessonId] = [];
        }

        // Add user message
        this.messages[lessonId].push({
          role: 'user',
          content: message,
          timestamp: new Date().toISOString()
        });

        // Add assistant response
        this.messages[lessonId].push({
          role: 'assistant',
          content: response.chatResponse,
          timestamp: new Date().toISOString()
        });

        this.error = null;
        return response;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to send message';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async fetchChatHistory(lessonId: string) {
      this.isLoading = true;
      try {
        const response = await chatService.getChatHistory(lessonId);
        this.messages[lessonId] = response.chatHistory;
        this.error = null;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to fetch chat history';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async analyzeMessage(message: string, existingPlan: string) {
      this.isLoading = true;
      try {
        const response = await chatService.analyzeMessage(message, existingPlan);
        this.analysis = response;
        this.currentAnalysis = response;
        return response;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to analyze message';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async sendComponentMessage(
      lessonId: string,
      message: string,
      existingPlan: string,
      component: string,
      analysis: any
    ): Promise<ChatResponse> {
      this.isLoading = true;
      try {
        const response = await chatService.sendComponentMessage(
          lessonId,
          message,
          existingPlan,
          component,
          analysis
        );
        this.error = null;
        return response;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to send message';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    clearError() {
      this.error = null;
    },

    // Reset store state
    resetStore() {
      this.messages = {};
      this.error = null;
      this.analysis = null;
      this.currentAnalysis = null;
    }
  }
});