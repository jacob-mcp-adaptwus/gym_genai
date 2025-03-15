import { fetchWrapper } from '@/utils/helpers/fetch-wrapper';

const API_URL = `${import.meta.env.VITE_API_URL}/plans`;

export interface Profile {
  currentStats: {
    weight: number;
    height: number;
    bodyFat: number;
    measurements: {
      chest: number;
      waist: number;
      hips: number;
      arms: number;
      legs: number;
      shoulders: number;
    };
    strengthLevels: {
      bench: number;
      squat: number;
      deadlift: number;
      overhead: number;
    };
  };
  goals: {
    primary: string;
    secondary: string;
    timeline: string;
    targetWeight: number;
    targetBodyFat: number;
    competitionDate: string;
    targetMeasurements: {
      chest: number;
      waist: number;
      hips: number;
      arms: number;
      legs: number;
      shoulders: number;
    };
  };
  experience: {
    level: string;
    yearsTraining: number;
    previousCompetitions: string[];
    injuries: string[];
    limitations: string[];
  };
}

export interface Workout {
  splitStructure: {
    type: string;
    daysPerWeek: number;
    restDays: string[];
    cycleLength: number;
  };
  weeklySchedule: Array<{
    day: string;
    focus: string;
    exercises: Array<{
      name: string;
      muscleGroup: string;
      sets: number;
      repsRange: string;
      intensity: string;
      rest: string;
      techniques: string[];
      notes: string;
    }>;
    cardio: {
      type: string;
      duration: string;
      intensity: string;
      timing: string;
    };
  }>;
  progression: {
    scheme: string;
    deloadFrequency: string;
    adaptationStrategy: string;
    volumeAdjustments: Array<{
      week: number;
      adjustment: string;
    }>;
  };
}

export interface Nutrition {
  calorieTargets: {
    trainingDays: number;
    restDays: number;
    weeklyAverage: number;
    adjustmentRate: number;
  };
  macroBreakdown: {
    protein: {
      grams: number;
      percentage: number;
    };
    carbs: {
      grams: number;
      percentage: number;
    };
    fats: {
      grams: number;
      percentage: number;
    };
  };
  mealTiming: Array<{
    meal: string;
    time: string;
    calories: number;
    protein: number;
    carbs: number;
    fats: number;
    purpose: string;
  }>;
  foodSelections: {
    proteinSources: string[];
    carbSources: string[];
    fatSources: string[];
    vegetables: string[];
    beverages: string[];
    supplements: string[];
  };
  peakWeekProtocol: {
    waterManipulation: string[];
    sodiumManipulation: string[];
    carbLoadingStrategy: string;
  };
}

export interface Supplementation {
  performanceEnhancers: Array<{
    name: string;
    category: string;
    dosage: string;
    frequency: string;
    timing: string;
    duration: string;
    purpose: string;
    notes: string;
  }>;
  recoveryAids: Array<{
    name: string;
    dosage: string;
    frequency: string;
    timing: string;
    purpose: string;
  }>;
  hormoneProtocols: Array<{
    compound: string;
    dosage: string;
    frequency: string;
    duration: string;
    cycleWeeks: number;
    pctProtocol: string;
    bloodworkSchedule: string[];
  }>;
  healthSupports: Array<{
    name: string;
    dosage: string;
    purpose: string;
    timing: string;
  }>;
}

export interface CoachFeedback {
  lastUpdated: string;
  adjustments: Array<{
    component: string;
    recommendation: string;
    reason: string;
    implementationDate: string;
  }>;
  progressNotes: Array<{
    date: string;
    metrics: {
      weightChange: number;
      measurementChanges: {
        chest: number;
        waist: number;
        arms: number;
        legs: number;
      };
      strengthChanges: {
        bench: number;
        squat: number;
        deadlift: number;
      };
    };
    observations: string;
    nextStepsRecommendation: string;
  }>;
}

export interface WorkoutPlan {
  metadata: {
    planId: string;
    userId: string;
    email: string;
    planName: string;
    createdAt: string;
    lastModified: string;
    version: number;
    status: string;
  };
  profile: Profile;
  workouts: Workout;
  nutrition: Nutrition;
  supplementation: Supplementation;
  coachFeedback: CoachFeedback;
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

export interface PlanGenerateRequest {
  title: string;
  goal?: string;
  experience?: string;
  existing_plan?: string;
  user_chat?: string;
  profile?: {
    weight: number;
    height: number;
    bodyFat: number;
    age: number;
    gender: string;
    fitnessLevel: string;
    trainingHistory: string;
    injuries: string;
    goals: string;
  };
}

export interface SavePlanResponse {
  message: string;
  plan?: Plan;
}

export interface ListPlansResponse {
  plans: Plan[];
  message?: string;
}

export interface ListVersionsResponse {
  versions: PlanVersion[];
  totalVersions: number;
}

export const planService = {
  listPlans: async (): Promise<ListPlansResponse> => {
    const response = await fetchWrapper.get(`${API_URL}/list`);
    return response as unknown as ListPlansResponse;
  },

  generatePlan: async (request: PlanGenerateRequest): Promise<WorkoutPlan> => {
    const response = await fetchWrapper.post(`${API_URL}/create`, request);
    return response as unknown as WorkoutPlan;
  },

  getPlanVersions: async (planId: string): Promise<ListVersionsResponse> => {
    const response = await fetchWrapper.get(`${API_URL}/versions/${planId}`);
    return response as unknown as ListVersionsResponse;
  },

  savePlan: async (plan: Partial<Plan>): Promise<SavePlanResponse> => {
    const response = await fetchWrapper.post(`${API_URL}/save`, plan);
    return response as unknown as SavePlanResponse;
  },

  deletePlan: async (planId: string): Promise<void> => {
    await fetchWrapper.delete(`${API_URL}/${planId}`);
  },
}; 