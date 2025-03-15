import { fetchWrapper } from '@/utils/helpers/fetch-wrapper';

const API_URL = `${import.meta.env.VITE_API_URL}/lessons`;

export interface ChatMessage {
    role: 'user' | 'assistant';
    content: string;
    timestamp: string;
  }
  
  export interface ChatResponse {
    chatResponse: string;
    updatedPlan?: any;
    updatedComponents?: string[];
  }
  
  export interface ChatHistory {
    chatHistory: ChatMessage[];
  }
  
  export interface ChatApiResponse {
    chatResponse: string;
    updatedPlan?: any;
    updatedComponents?: string[];
  }

  export interface AnalyzeResponse {
    components: string[];
    intent: string;
    tier: number;
    rationale: string;
    requires_foundation_update: boolean;
  }

  export const chatService = {
    sendMessage: async (
      message: string, 
      existingPlan: string | undefined, 
      lessonId: string,
      analysis?: AnalyzeResponse
    ): Promise<ChatResponse> => {
      const response = await fetchWrapper.post(`${API_URL}/chat`, {
        message,
        existing_plan: existingPlan,
        lessonId,
        analysis
      });
      return response as unknown as ChatResponse;
    },
  
    analyzeMessage: async (message: string, existingPlan: string): Promise<AnalyzeResponse> => {
      const response = await fetchWrapper.post(`${API_URL}/analyze`, {
        message,
        existing_plan: existingPlan
      });
      return response as unknown as AnalyzeResponse;
    },
  
    getChatHistory: async (lessonId: string): Promise<ChatHistory> => {
      const response = await fetchWrapper.get(`${API_URL}/${lessonId}/chat-history`);
      return response as unknown as ChatHistory;
    },
  
    sendComponentMessage: async (
      lessonId: string,
      message: string,
      existingPlan: string,
      component: string,
      analysis: any
    ): Promise<ChatResponse> => {
      const response = await fetchWrapper.post(`${API_URL}/chat/component`, {
        lessonId,
        message,
        existing_plan: existingPlan,
        component,
        analysis
      });
      return response as unknown as ChatResponse;
    }
  };