// Type declarations for Vue files
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

// Type declarations for planService
declare module '@/services/planService' {
  export interface Profile {
    currentStats?: {
      weight?: number;
      height?: number;
      bodyFat?: number;
      measurements?: Record<string, number>;
      strengthLevels?: Record<string, number>;
    };
    goals?: {
      primary?: string;
      secondary?: string;
      timeline?: string;
      targetWeight?: number;
      targetBodyFat?: number;
      competitionDate?: string;
      targetMeasurements?: Record<string, number>;
    };
    experience?: {
      level?: string;
      yearsTraining?: number;
      previousCompetitions?: string[];
      injuries?: string[];
      limitations?: string[];
    };
  }

  export interface Plan {
    planId: string;
    title: string;
    goal: string;
    experience: string;
    lastModified: string;
    status: string;
    content?: string;
  }

  export interface PlanVersion {
    planId: string;
    version: number;
    content: string;
    title: string;
    goal: string;
    experience: string;
    timestamp: string;
    userId: string;
    email: string;
  }

  export interface WorkoutPlan {
    metadata?: {
      planId?: string;
      userId?: string;
      email?: string;
      planName?: string;
      createdAt?: string;
      lastModified?: string;
      version?: number;
      status?: string;
    };
    profile?: Profile;
    workouts?: any;
    nutrition?: any;
    supplementation?: any;
    coachFeedback?: any;
    [key: string]: any;
  }

  export interface PlanGenerateRequest {
    title: string;
    goal?: string;
    experience?: string;
    existing_plan?: string;
    user_chat?: string;
    profile?: any;
  }
}

// Type declarations for stores/plans
declare module '@/stores/plans' {
  import type { Plan, PlanVersion, WorkoutPlan, PlanGenerateRequest } from '@/services/planService';
  
  export function usePlanStore(): {
    plans: Plan[];
    currentPlan: Plan | null;
    isLoading: boolean;
    error: string | null;
    saveStatus: string | null;
    isInitialized: boolean;
    planVersions: PlanVersion[];
    totalVersions: number;
    getPlanById: (id: string) => Plan | null;
    getSortedPlans: Plan[];
    isSaving: boolean;
    isSaved: boolean;
    hasSaveError: boolean;
    fetchUserPlans(): Promise<void>;
    getPlanVersions(planId: string): Promise<void>;
    generatePlan(params: any): Promise<Plan>;
    deletePlan(planId: string): Promise<void>;
    savePlan(plan: Partial<Plan>): Promise<void>;
    clearError(): void;
    clearSaveStatus(): void;
    resetStore(): void;
  }
}

// Type declarations for stores/chats
declare module '@/stores/chats' {
  export interface ChatMessage {
    role: 'user' | 'assistant';
    content: string;
    timestamp: string;
  }
  
  export interface AnalyzeResponse {
    components: string[];
    intent: string;
    tier: number;
    rationale: string;
    requires_foundation_update: boolean;
  }
  
  export function useChatStore(): {
    messages: Record<string, ChatMessage[]>;
    isLoading: boolean;
    error: string | null;
    analysis: AnalyzeResponse | null;
    currentAnalysis: AnalyzeResponse | null;
    getChatHistory: (lessonId: string) => ChatMessage[];
    sendMessage(lessonId: string, message: string, existingPlan?: string, analysis?: AnalyzeResponse): Promise<any>;
    fetchChatHistory(lessonId: string): Promise<void>;
    analyzeMessage(message: string, existingPlan: string): Promise<AnalyzeResponse>;
    sendComponentMessage(lessonId: string, message: string, existingPlan: string, component: string, analysis: any): Promise<any>;
    clearError(): void;
    resetStore(): void;
  }
}

// Type declarations for lucide-vue-next
declare module 'lucide-vue-next' {
  import type { DefineComponent } from 'vue';
  
  export const Save: DefineComponent<{}, {}, any>;
  export const History: DefineComponent<{}, {}, any>;
  export const Download: DefineComponent<{}, {}, any>;
} 