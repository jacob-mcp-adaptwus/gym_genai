// src/stores/lessons.ts
import { defineStore } from 'pinia';
import { lessonService, type Lesson, type LessonVersion, type LessonGenerateRequest } from '@/services/lessonService';
import type { Profile } from '@/services/profileService';



//// interfaces
interface LessonState {
  lessons: Lesson[];
  currentLesson: Lesson | null;
  isLoading: boolean;
  error: string | null;
  saveStatus: string | null;
  isInitialized: boolean;
  lessonVersions: LessonVersion[];
  totalVersions: number;
}

interface ApiResponse {
  lessons: Lesson[];
  message?: string;
}


interface GenerateLessonParams {
  topic: string;
  grade?: string;
  subject?: string;
  profile?: Profile | null;
  existingPlan?: string;
  userChat?: string;  // Add new optional parameter
}

export const useLessonStore = defineStore('lessons', {
  state: (): LessonState => ({
    lessons: [],
    currentLesson: null,
    isLoading: false,
    error: null,
    saveStatus: null,
    isInitialized: false,
    lessonVersions: [],
    totalVersions: 0
  }),

  getters: {
    getLessonById: (state) => {
      return (id: string) => state.lessons.find(lesson => lesson.lessonId === id) || null;
    },
    
    getSortedLessons: (state): Lesson[] => {
      if (!state.lessons || !Array.isArray(state.lessons)) {
        console.warn('Lessons array is invalid:', state.lessons);
        return [];
      }
      
      return [...state.lessons].sort((a, b) => {
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
    async fetchUserLessons() {
      if (this.isLoading) return;
      
      this.isLoading = true;
      
      try {
        const response = await lessonService.listLessons();
        
        // Check if response is an object with a lessons property
        if (response && typeof response === 'object' && 'lessons' in response) {
          const apiResponse = response as ApiResponse;
          if (Array.isArray(apiResponse.lessons)) {
            this.lessons = apiResponse.lessons;
          } else {
            console.warn('Lessons property is not an array:', apiResponse.lessons);
            this.lessons = [];
          }
        } else if (Array.isArray(response)) {
          // Handle case where response is directly an array
          this.lessons = response;
        } else {
          console.warn('Invalid response format:', response);
          this.lessons = [];
        }
        
        this.error = null;
        this.isInitialized = true;
      } catch (error) {
        console.error('Error fetching lessons:', error);
        this.lessons = [];
        this.error = error instanceof Error ? error.message : 'Failed to fetch lessons';
      } finally {
        this.isLoading = false;
      }
    },

    

    async getLessonVersions(lessonId: string) {
      if (this.isLoading) return;
      
      this.isLoading = true;
      try {
        const response = await lessonService.getLessonVersions(lessonId);
        if (response && Array.isArray(response.versions)) {
          this.lessonVersions = response.versions;
          this.totalVersions = response.totalVersions;
        }
        this.error = null;
      } catch (error) {
        console.error('Error fetching lesson versions:', error);
        this.error = error instanceof Error ? error.message : 'Failed to fetch lesson versions';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async generateLessonPlan(params: GenerateLessonParams) {
      this.isLoading = true;
      try {
        const payload: LessonGenerateRequest = {
          topic: params.topic
        };

        // Add grade and subject only for new lessons
        if (!params.existingPlan) {
          if (!params.grade || !params.subject) {
            throw new Error('Grade and subject are required for new lessons');
          }
          payload.grade = params.grade;
          payload.subject = params.subject;
        }

        // Add existing plan if available
        if (params.existingPlan) {
          payload.existing_plan = params.existingPlan;
        }

        // Add user chat if available
        if (params.userChat) {
          payload.user_chat = params.userChat;
        }

        // Add profile information if provided
        if (params.profile) {
          payload.profile = {
            profileName: params.profile.profileName,
            demographics: params.profile.demographics,
            generalBackground: params.profile.generalBackground,
            mathAbility: params.profile.mathAbility,
            engagement: params.profile.engagement,
            specialConsiderations: params.profile.specialConsiderations
          };
        }

        const lessonPlan = await lessonService.generateLessonPlan(payload);
        this.error = null;
        return lessonPlan;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to generate lesson plan';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },
    async deleteLesson(lessonId: string) {
      this.isLoading = true;
      try {
        await lessonService.deleteLesson(lessonId);
        // Remove the lesson from the local state
        this.lessons = this.lessons.filter(lesson => lesson.lessonId !== lessonId);
        this.error = null;
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Failed to delete lesson';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async saveLessonPlan(lesson: Partial<Lesson>) {
      this.saveStatus = 'saving';
      try {
        const response = await lessonService.saveLessonPlan(lesson);
        this.saveStatus = 'saved';
        
        // Refresh the lessons list after saving
        await this.fetchUserLessons();
        
        return response;
      } catch (error) {
        this.saveStatus = 'error';
        throw error;
      }
    },

    clearError() {
      this.error = null;
    },

    clearSaveStatus() {
      this.saveStatus = null;
    },

    // Reset store state
    resetStore() {
      this.lessons = [];
      this.currentLesson = null;
      this.error = null;
      this.saveStatus = null;
      this.isInitialized = false;
    }
  }
});