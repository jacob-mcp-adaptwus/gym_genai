// src/components/WelcomeBanner.vue
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useProfileStore } from '@/stores/profiles';
import { useLessonStore } from '@/stores/lessons';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const profileStore = useProfileStore();
const lessonStore = useLessonStore();
const authStore = useAuthStore();

const { cognitoUser } = useAuthStore();
const { getSortedProfiles } = storeToRefs(profileStore);
const { getSortedLessons } = storeToRefs(lessonStore);

const recentLessons = ref(0);
const activeProfiles = ref(0);

const userFullName = computed(() => {
  if (cognitoUser?.profile) {
    const { given_name, family_name } = cognitoUser.profile;
    return `${given_name} ${family_name}`;
  }
  return 'Teacher';
});

// Navigation handlers
const navigateToLessonPlanner = () => router.push('/lessons/planner');
const navigateToProfiles = () => router.push('/profiles/myprofiles');
const navigateToLessons = () => router.push('/lessons/mylesson');

onMounted(async () => {
  try {
    await Promise.all([
      profileStore.fetchProfiles(),
      lessonStore.fetchUserLessons()
    ]);

    recentLessons.value = getSortedLessons.value.length;
    
    // Updated profile counting logic
    const profiles = getSortedProfiles.value;
    console.log('All profiles:', profiles); // Debug log
    
    // Count profiles that don't explicitly have active set to false
    activeProfiles.value = profiles.reduce((count, profile) => {
      // Consider a profile active if active is true or undefined
      return count + (profile.active !== false ? 1 : 0);
    }, 0);

  } catch (err) {
    console.error('Error loading welcome banner data:', err);
  }
});
</script>

<template>
  <v-card class="mathilda-banner text-surface overflow-hidden" elevation="0" rounded="lg">
    <v-card-text class="py-5 px-md-12 px-6">
      <v-row align="center">
        <v-col cols="12" xl="7" md="8" sm="12">
          <div class="pb-md-8 pt-md-7 pt-5 pb-6">
            <!-- Header using Museo Moderno font -->
            <h2 class="welcome-header text-sm-h2 text-h3 mb-4">
              Welcome back, {{ userFullName }}!
            </h2>
            
            <v-row class="mb-6">
              <v-col cols="6">
                <v-card class="stat-card pa-4" elevation="0">
                  <div class="text-h4 mb-1">{{ recentLessons }}</div>
                  <div class="text-body-2">Lesson Plans</div>
                </v-card>
              </v-col>
              <v-col cols="6">
                <v-card class="stat-card pa-4" elevation="0">
                  <div class="text-h4 mb-1">{{ activeProfiles }}</div>
                  <div class="text-body-2">Active Profiles</div>
                </v-card>
              </v-col>
            </v-row>

            <p class="banner-text text-h6 mb-7">
              Create personalized lesson plans, manage student profiles, and leverage AI
              to enhance your teaching experience.
            </p>

            <v-row class="action-buttons">
              <v-col cols="12" sm="auto">
                <v-btn
                  class="create-btn"
                  size="x-large"
                  block
                  @click="navigateToLessons()">
                  Create New Lesson
                </v-btn>
              </v-col>
              <v-col cols="12" sm="auto">
                <v-btn
                  class="profiles-btn"
                  size="x-large"
                  block
                  @click="navigateToProfiles"
                >
                  Manage Profiles
                </v-btn>
              </v-col>
              <v-col cols="12" sm="auto">
                <v-btn
                  class="lessons-btn"
                  size="x-large"
                  block
                  @click="navigateToLessons"
                >
                  View My Lessons
                </v-btn>
              </v-col>
            </v-row>
          </div>
        </v-col>

        <v-col cols="12" xl="5" md="4" class="d-md-block d-none">
          <div class="banner-illustration">
            <v-img
              src="/api/placeholder/500/300"
              alt="Teaching illustration"
              class="rounded-lg"
            />
          </div>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style lang="scss" scoped>
.mathilda-banner {
  background: #78C0E5; // Primary color from style guide
  
  .welcome-header {
    font-family: 'Museo Moderno', sans-serif;
    font-weight: 800;
    color: #FFFFFF;
  }

  .banner-text {
    font-family: 'Quicksand', sans-serif;
    font-weight: 500;
    color: #FFFFFF;
  }

  .stat-card {
    background: rgba(255, 255, 255, 0.15);
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    
    .text-h4 {
      font-family: 'Museo Moderno', sans-serif;
      font-weight: 700;
      color: #FFFFFF;
    }
    
    .text-body-2 {
      font-family: 'Quicksand', sans-serif;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.9);
    }
  }

  .action-buttons {
    gap: 1rem;
    
    .v-btn {
      font-family: 'Quicksand', sans-serif;
      font-weight: 700;
      font-size: 20px;
      letter-spacing: 0.5px;
      height: 56px;
      border-radius: 12px;
      text-transform: none;
      
      &.create-btn {
        background: #FFFFFF;
        color: #78C0E5;
        
        &:hover {
          background: #F1F1F2;
        }
      }
      
      &.profiles-btn {
        background: #EF8D61; // Secondary color
        color: #FFFFFF;
        
        &:hover {
          background: darken(#EF8D61, 5%);
        }
      }
      
      &.lessons-btn {
        background: #B7E6F2; // Accent 1
        color: #5C6970; // Neutral Dark
        
        &:hover {
          background: darken(#B7E6F2, 5%);
        }
      }
    }
  }
}

@media (max-width: 600px) {
  .mathilda-banner {
    .action-buttons {
      .v-col {
        padding: 4px 12px;
      }
      
      .v-btn {
        width: 100%;
      }
    }
  }

  .welcome-header {
    font-size: 28px !important;
  }
}
</style>