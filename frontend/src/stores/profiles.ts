// src/stores/profiles.ts
import { defineStore } from 'pinia';
import { profileService, type Profile, type CreateProfileRequest, type UpdateProfileRequest } from '@/services/profileService';

interface ProfileState {
  profiles: Profile[];
  currentProfile: Profile | null;
  isLoading: boolean;
  error: string | null;
  saveStatus: 'idle' | 'saving' | 'saved' | 'error';
  isInitialized: boolean;
}

export const useProfileStore = defineStore('profiles', {
  state: (): ProfileState => ({
    profiles: [],
    currentProfile: null,
    isLoading: false,
    error: null,
    saveStatus: 'idle',
    isInitialized: false
  }),

  getters: {
    getProfileByName: (state) => {
      return (profileName: string) => 
        state.profiles.find(profile => profile.profileName === profileName) || null;
    },

    getSortedProfiles: (state): Profile[] => {
      if (!state.profiles || !Array.isArray(state.profiles)) {
        console.warn('Profiles array is invalid:', state.profiles);
        return [];
      }

      return [...state.profiles].sort((a, b) => {
        // Sort by active status first (active profiles first)
        if (a.active !== b.active) {
          return b.active ? 1 : -1;
        }
        // Then sort alphabetically by name
        return a.profileName.localeCompare(b.profileName);
      });
    },

    isSaving: (state) => state.saveStatus === 'saving',
    isSaved: (state) => state.saveStatus === 'saved',
    hasSaveError: (state) => state.saveStatus === 'error',

    // Add getters for specific profile attributes if needed
    getProfileDemographics: (state) => (profileName: string) => {
      const profile = state.profiles.find(p => p.profileName === profileName);
      return profile?.demographics || '';
    },

    getProfileBackground: (state) => (profileName: string) => {
      const profile = state.profiles.find(p => p.profileName === profileName);
      return profile?.generalBackground || '';
    }
  },

  actions: {
    async fetchProfiles() {
      if (this.isLoading) return;

      console.log('Fetching user profiles...');
      this.isLoading = true;

      try {
        const profiles = await profileService.listProfiles();
        this.profiles = profiles;
        this.error = null;
        this.isInitialized = true;
        console.log('Profiles updated in store:', this.profiles);
      } catch (error) {
        console.error('Error fetching profiles:', error);
        this.profiles = [];
        this.error = error instanceof Error ? error.message : 'Failed to fetch profiles';
      } finally {
        this.isLoading = false;
      }
    },

    async createProfile(profileData: CreateProfileRequest) {
      this.saveStatus = 'saving';
      try {
        const response = await profileService.createProfile(profileData);
        if (response.error) {
          throw new Error(response.error);
        }
        this.saveStatus = 'saved';
        
        // Refresh the profiles list after creating
        await this.fetchProfiles();
        
        return response;
      } catch (error) {
        this.saveStatus = 'error';
        const errorMessage = error instanceof Error ? error.message : 'Failed to create profile';
        this.error = errorMessage;
        throw new Error(errorMessage);
      }
    },

    async updateProfile(profileName: string, profileData: UpdateProfileRequest) {
      this.saveStatus = 'saving';
      try {
        const response = await profileService.updateProfile(profileName, profileData);
        if (response.error) {
          throw new Error(response.error);
        }
        this.saveStatus = 'saved';
        
        // Refresh the profiles list after updating
        await this.fetchProfiles();
        
        return response;
      } catch (error) {
        this.saveStatus = 'error';
        const errorMessage = error instanceof Error ? error.message : 'Failed to update profile';
        this.error = errorMessage;
        throw new Error(errorMessage);
      }
    },

    async deleteProfile(profileName: string) {
      this.isLoading = true;
      try {
        const response = await profileService.deleteProfile(profileName);
        if (response.error) {
          throw new Error(response.error);
        }
        
        // Remove the profile from local state
        this.profiles = this.profiles.filter(p => p.profileName !== profileName);
        
        // Clear current profile if it was deleted
        if (this.currentProfile?.profileName === profileName) {
          this.currentProfile = null;
        }
        
        return response;
      } catch (error) {
        const errorMessage = error instanceof Error ? error.message : 'Failed to delete profile';
        this.error = errorMessage;
        throw new Error(errorMessage);
      } finally {
        this.isLoading = false;
      }
    },

    setCurrentProfile(profile: Profile | null) {
      this.currentProfile = profile;
    },

    clearError() {
      this.error = null;
    },

    clearSaveStatus() {
      this.saveStatus = 'idle';
    },

    // Reset store state
    resetStore() {
      this.profiles = [];
      this.currentProfile = null;
      this.error = null;
      this.saveStatus = 'idle';
      this.isInitialized = false;
    }
  }
});