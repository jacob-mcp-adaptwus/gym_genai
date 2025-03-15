// src/services/profileService.ts
import { fetchWrapper } from '@/utils/helpers/fetch-wrapper';

const API_URL = `${import.meta.env.VITE_API_URL}/profiles`;

export interface Profile {
  profileName: string;
  demographics: string;
  generalBackground: string;
  mathAbility: string;
  engagement: string;
  specialConsiderations: string;
  active: boolean;
}

export interface CreateProfileRequest {
  profileName: string;
  demographics: string;
  generalBackground: string;
  mathAbility: string;
  engagement: string;
  specialConsiderations: string;
}

export interface UpdateProfileRequest {
  demographics?: string;
  generalBackground?: string;
  mathAbility?: string;
  engagement?: string;
  specialConsiderations?: string;
  active?: boolean;
}

export interface ApiResponse {
  message: string;
  profile?: Profile;
  profiles?: Profile[];
  error?: string;
}

export const profileService = {
  listProfiles: async (): Promise<Profile[]> => {
    const response = await fetchWrapper.get(`${API_URL}/list`);
    return (response as unknown as ApiResponse).profiles || [];
  },

  createProfile: async (request: CreateProfileRequest): Promise<ApiResponse> => {
    const response = await fetchWrapper.post(
      `${API_URL}/create`,
      request
    ) as unknown;
    return response as ApiResponse;
  },

  updateProfile: async (profileName: string, request: UpdateProfileRequest): Promise<ApiResponse> => {
    const response = await fetchWrapper.put(
      `${API_URL}/${profileName}`,
      request
    ) as unknown;
    return response as ApiResponse;
  },

  deleteProfile: async (profileName: string): Promise<ApiResponse> => {
    const response = await fetchWrapper.delete(
      `${API_URL}/${profileName}`
    ) as unknown;
    return response as ApiResponse;
  }
};