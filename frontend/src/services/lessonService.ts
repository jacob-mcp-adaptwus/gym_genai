import { fetchWrapper } from '@/utils/helpers/fetch-wrapper';

const API_URL = `${import.meta.env.VITE_API_URL}/lessons`;

export interface PedagogicalContext {
  bigIdeas: string[];
  prerequisites: string[];
  misconceptions: {
    common: string[];
    addressingStrategies: string[];
  };
  mathematicalProgressions: {
    priorKnowledge: string[];
    futureConnections: string[];
    crossCutting: string[];
  };
}
export interface Assessment {
  formative: {
    checkpoints: Array<{
      timing: string;
      task: string;
      successCriteria: string[];
      intervention: {
        support: string;
        extension: string;
      };
    }>;
    observationGuide: {
      lookFor: string[];
      listenFor: string[];
    };
  };
  summative: {
    tasks: Array<{
      description: string;
      alignedObjectives: string[];
      scoringCriteria: string[];
    }>;
  };
}

export interface Accessibility {
  languageSupports: {
    vocabulary: Array<{
      term: string;
      definition: string;
      representation: string;
    }>;
    sentenceFrames: string[];
    comprehensionStrategies: string[];
  };
  visualSupports: string[];
  accommodations: {
    presentation: string[];
    response: string[];
    setting: string[];
    timing: string[];
  };
}

export interface Objectives {
  content: string[];
  language: string[];
  mathematical_practice: string[];
  success_criteria: string[];
}

export interface LessonFlow {
  launch: {
    duration: string;
    hook: {
      description: string;
      rationale: string;
    };
    priorKnowledgeActivation: string[];
    teacherMoves: string[];
  };
  explore: {
    activities: Array<{
      title: string;
      description: string;
      grouping: string;
      steps: string[];
      differentiationNotes: {
        acceleration: string[];
        support: string[];
        ell: string[];
      };
    }>;
  };
  discussion: {
    keyQuestions: Array<{
      question: string;
      purpose: string;
      anticipatedResponses: string[];
    }>;
    studentDiscoursePrompts: string[];
  };
  closure: {
    synthesisTasks: string[];
    reflectionPrompts: string[];
    exitTicket: {
      question: string;
      expectedResponse: string;
      scoringGuidance: string;
    };
  };
}


export interface LessonPlan {
  metadata: {
    topic: string;
    grade: string;
    subject: string;
    lastModified: string;
    standardsAddressed: {
      focalStandard: string[];
      supportingStandards: string[];
    };
    profileName?: string;
  };
  pedagogicalContext: PedagogicalContext;
  objectives: Objectives;
  lessonFlow: LessonFlow;
  markupProblemSets: {
    warmup: Array<Problem>;
    corePractice: Array<Problem>;
    extension: Array<Problem>;
  };
  markupProblemSetsAboveGradeLevel: {
    warmup: Array<Problem>;
    corePractice: Array<Problem>;
    extension: Array<Problem>;
  };
  markupProblemSetsBelowGradeLevel: {
    warmup: Array<Problem>;
    corePractice: Array<Problem>;
    extension: Array<Problem>;
  };

  assessments: Assessment;
  accessibility: Accessibility;
  studentProfile?: {
    profileName: string;
    adaptations: string[];
    teachingStrategies: string[];
  };
  grade: string;
  subject: string;
  total_duration: string;
}

export interface Problem {
  type: string;
  difficulty: number;
  problem: {
    stem: string;
    context?: string;
    scaffoldLevel?: number;
    openEndedPrompt?: string;
  };
  solution: {
    answer: string;
    workingOut: string;
  };
  hints: Array<{
    text: string;
    scaffold: string;
  }>;
}

export interface Lesson {
  lessonId: string;
  title: string;
  subject: string;
  grade: string;
  lastModified: string;
  status: string;
  content?: string;
  duration?: string;
}

export interface LessonVersion {
  lessonId: string;
  profileVersion: string;
  content: string;
  title: string;
  grade: string;
  subject: string;
  timestamp: string;
  version: number;
  profileId: string;
  email: string;
}

export interface LessonGenerateRequest {
  topic: string;
  grade?: string;
  subject?: string;
  existing_plan?: string;
  user_chat?: string; // Add this new optional parameter
  profile?: {
    profileName: string;
    demographics: string;
    generalBackground: string;
    mathAbility: string;
    engagement: string;
    specialConsiderations: string;
  };
}

export interface SaveLessonResponse {
  message: string;
  lesson?: Lesson;
}

export interface ListLessonsResponse {
  lessons: Lesson[];
  message?: string;
}

export interface ListVersionsResponse {
  versions: LessonVersion[];
  totalVersions: number;
}
export const lessonService = {
  listLessons: async (): Promise<ListLessonsResponse> => {
    const response = await fetchWrapper.get(`${API_URL}/list`);
    return response as unknown as ListLessonsResponse;
  },

  generateLessonPlan: async (request: LessonGenerateRequest): Promise<LessonPlan> => {
    const response = await fetchWrapper.post(`${API_URL}/create`, request);
    return response as unknown as LessonPlan;
  },

  getLessonVersions: async (lessonId: string): Promise<ListVersionsResponse> => {
    const response = await fetchWrapper.get(`${API_URL}/versions/${lessonId}`);
    return response as unknown as ListVersionsResponse;
  },

  saveLessonPlan: async (lesson: Partial<Lesson>): Promise<SaveLessonResponse> => {
    const response = await fetchWrapper.post(`${API_URL}/save`, lesson);
    return response as unknown as SaveLessonResponse;
  },

  deleteLesson: async (lessonId: string): Promise<void> => {
    await fetchWrapper.delete(`${API_URL}/${lessonId}`);
  },
};