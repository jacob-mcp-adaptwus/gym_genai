// src/stores/plans.ts
import { defineStore } from 'pinia';
import { planService, type Plan, type PlanVersion, type PlanGenerateRequest } from '@/services/planService';
import type { Profile } from '@/services/planService';

//// interfaces
interface PlanState {
  plans: Plan[];
  currentPlan: Plan | null;
  isLoading: boolean;
  error: string | null;
  saveStatus: string | null;
  isInitialized: boolean;
  planVersions: PlanVersion[];
  totalVersions: number;
}

interface ApiResponse {
  plans: Plan[];
  message?: string;
}

interface GeneratePlanParams {
  title: string;
  goal?: string;
  experience?: string;
  profile?: Profile | null;
  existingPlan?: string;
  userChat?: string;
}

export const usePlanStore = defineStore('plans', {
  state: (): PlanState => ({
    plans: [],
    currentPlan: null,
    isLoading: false,
    error: null,
    saveStatus: null,
    isInitialized: false,
    planVersions: [],
    totalVersions: 0
  }),

  getters: {
    getPlanById: (state) => {
      return (id: string) => state.plans.find(plan => plan.planId === id) || null;
    },
    
    getSortedPlans: (state): Plan[] => {
      if (!state.plans || !Array.isArray(state.plans)) {
        console.warn('Plans array is invalid:', state.plans);
        return [];
      }
      
      return [...state.plans].sort((a, b) => {
        const dateA = a.lastModified ? new Date(a.lastModified).getTime() : 0;
        const dateB = b.lastModified ? new Date(b.lastModified).getTime() : 0;
        return dateB - dateA;
      });
    },
    isSaving: (state) => state.saveStatus === 'saving',
    isSaved: (state) => state.saveStatus === 'saved',
    hasSaveError: (state) => state.saveStatus === 'error'
  },

  actions: {
    async fetchUserPlans() {
      if (this.isLoading) return;
      
      this.isLoading = true;
      
      try {
        const response = await planService.listPlans();
        
        // Check if response is an object with a plans property
        if (response && typeof response === 'object' && 'plans' in response) {
          const apiResponse = response as ApiResponse;
          if (Array.isArray(apiResponse.plans)) {
            this.plans = apiResponse.plans;
          } else {
            console.warn('Plans property is not an array:', apiResponse.plans);
            this.plans = [];
          }
        } else if (Array.isArray(response)) {
          // Handle case where response is directly an array
          this.plans = response;
        } else {
          console.warn('Invalid response format:', response);
          this.plans = [];
        }
        
        this.error = null;
        this.isInitialized = true;
      } catch (error) {
        console.error('Error fetching plans:', error);
        this.plans = [];
        this.error = error instanceof Error ? error.message : 'Failed to fetch plans';
      } finally {
        this.isLoading = false;
      }
    },

    async getPlanVersions(planId: string) {
      this.isLoading = true;
      
      try {
        const response = await planService.getPlanVersions(planId);
        
        if (response && typeof response === 'object') {
          this.planVersions = response.versions || [];
          this.totalVersions = response.totalVersions || 0;
        } else {
          this.planVersions = [];
          this.totalVersions = 0;
        }
        
        this.error = null;
      } catch (error) {
        console.error('Error fetching plan versions:', error);
        this.planVersions = [];
        this.totalVersions = 0;
        this.error = error instanceof Error ? error.message : 'Failed to fetch plan versions';
      } finally {
        this.isLoading = false;
      }
    },

    async generatePlan(params: GeneratePlanParams) {
      this.isLoading = true;
      this.error = null;
      
      try {
        // Convert to API request format
        const request: PlanGenerateRequest = {
          title: params.title,
          goal: params.goal,
          experience: params.experience,
          existing_plan: params.existingPlan,
          user_chat: params.userChat
        };
        
        // Add profile if provided
        if (params.profile) {
          request.profile = {
            weight: params.profile.currentStats?.weight || 0,
            height: params.profile.currentStats?.height || 0,
            bodyFat: params.profile.currentStats?.bodyFat || 0,
            age: 30, // Default value, should be provided by user
            gender: 'male', // Default value, should be provided by user
            fitnessLevel: params.profile.experience?.level || '',
            trainingHistory: `${params.profile.experience?.yearsTraining || 0} years of training`,
            injuries: params.profile.experience?.injuries?.join(', ') || '',
            goals: params.profile.goals?.primary || ''
          };
        }
        
        const workoutPlan = await planService.generatePlan(request);
        
        // Create a new plan object
        const newPlan: Plan = {
          planId: workoutPlan.metadata?.planId || '',
          title: params.title,
          goal: params.goal || '',
          experience: params.experience || '',
          lastModified: new Date().toISOString(),
          status: 'active',
          content: JSON.stringify(workoutPlan)
        };
        
        this.currentPlan = newPlan;
        return newPlan;
      } catch (error) {
        console.error('Error generating plan:', error);
        this.error = error instanceof Error ? error.message : 'Failed to generate plan';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async deletePlan(planId: string) {
      this.isLoading = true;
      
      try {
        await planService.deletePlan(planId);
        
        // Remove the deleted plan from the local state
        this.plans = this.plans.filter(plan => plan.planId !== planId);
        
        // Clear current plan if it was deleted
        if (this.currentPlan?.planId === planId) {
          this.currentPlan = null;
        }
        
        this.error = null;
      } catch (error) {
        console.error('Error deleting plan:', error);
        this.error = error instanceof Error ? error.message : 'Failed to delete plan';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async savePlan(plan: Partial<Plan>) {
      this.saveStatus = 'saving';
      
      try {
        const response = await planService.savePlan(plan);
        
        // Update the plan in the local state if it exists
        if (plan.planId) {
          const index = this.plans.findIndex(p => p.planId === plan.planId);
          
          if (index !== -1) {
            // Update existing plan
            this.plans[index] = { ...this.plans[index], ...plan };
          } else if (response.plan) {
            // Add new plan
            this.plans.push(response.plan);
          }
        }
        
        this.saveStatus = 'saved';
        this.error = null;
      } catch (error) {
        console.error('Error saving plan:', error);
        this.saveStatus = 'error';
        this.error = error instanceof Error ? error.message : 'Failed to save plan';
        throw error;
      }
    },

    clearError() {
      this.error = null;
    },
    
    clearSaveStatus() {
      this.saveStatus = null;
    },
    
    resetStore() {
      this.plans = [];
      this.currentPlan = null;
      this.isLoading = false;
      this.error = null;
      this.saveStatus = null;
      this.isInitialized = false;
      this.planVersions = [];
      this.totalVersions = 0;
    }
  }
}); 