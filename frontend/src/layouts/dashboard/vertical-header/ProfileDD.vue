<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useCustomizerStore } from '../../../stores/customizer';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const tab = ref(null);
const authStore = useAuthStore();
const customizer = useCustomizerStore();

const { cognitoUser } = useAuthStore();

// Computed properties for user information
const userFullName = computed(() => {
  if (cognitoUser?.profile) {
    const { given_name, family_name } = cognitoUser.profile;
    return `${given_name} ${family_name}`;
  }
  return 'User';
});

const userEmail = computed(() => {
  return cognitoUser?.profile?.email || 'No email available';
});

const handleNavigation = (route: string) => {
  router.push(route);
};

const profiledata1 = ref([
  {
    title: 'Lesson Planner',
    icon: 'custom-edit',
    route: '/lessons/planner'
  },
  {
    title: 'My Lessons',
    icon: 'custom-history',
    route: '/lessons/mylesson'
  },
  {
    title: 'My Profiles',
    icon: 'custom-user',
    route: '/profiles/myprofiles'
  }
]);

const profiledata2 = ref([
  {
    title: 'Support',
    icon: 'custom-support'
  }
]);
</script>

<template>
  <!-- Profile Dropdown -->
  <div>
    <div class="d-flex align-center pa-5">
      <v-avatar size="40" class="me-2">
        <img src="@/assets/images/users/mathtilda.png" width="40" alt="profile" />
      </v-avatar>
      <div>
        <h6 class="text-subtitle-1 mb-0">{{ userFullName }}</h6>
        <p class="text-caption text-lightText mb-0">{{ userEmail }}</p>
      </div>
      <div class="ms-auto">
        <v-btn 
          variant="text" 
          aria-label="logout" 
          color="error" 
          rounded="sm" 
          icon 
          size="large" 
          @click="authStore.logout()"
        >
          <SvgSprite name="custom-logout-1" />
        </v-btn>
      </div>
    </div>
    
    <v-tabs v-model="tab" color="primary" grow>
      <v-tab value="111">
        <div class="v-icon--start">
          <SvgSprite 
            name="custom-user-outline" 
            style="width: 18px; height: 18px" 
          />
        </div>
        Profile
      </v-tab>
      <v-tab value="222">
        <div class="v-icon--start">
          <SvgSprite 
            name="custom-setting-outline-1" 
            style="width: 18px; height: 18px" 
          />
        </div>
        Setting
      </v-tab>
    </v-tabs>

    <v-divider></v-divider>

    <perfect-scrollbar style="height: calc(100vh - 300px); max-height: 240px">
      <v-window v-model="tab">
        <!-- Profile Tab -->
        <v-window-item value="111">
          <v-list class="px-2" aria-label="profile list">
            <v-list-item
              v-for="(item, index) in profiledata1"
              :key="index"
              color="primary"
              :base-color="customizer.actTheme === 'dark' ? 'lightText' : 'secondary'"
              rounded="md"
              :value="item.title"
              @click="handleNavigation(item.route)"
              class="mb-1"
            >
              <template v-slot:prepend>
                <div class="me-4">
                  <SvgSprite :name="item.icon || ''" style="width: 18px; height: 18px" />
                </div>
              </template>
              <v-list-item-title class="text-subtitle-1">{{ item.title }}</v-list-item-title>
            </v-list-item>

            <v-list-item
              @click="authStore.logout()"
              color="primary"
              :base-color="customizer.actTheme === 'dark' ? 'lightText' : 'secondary'"
              rounded="md"
            >
              <template v-slot:prepend>
                <div class="me-4">
                  <SvgSprite name="custom-logout-1" style="width: 18px; height: 18px" />
                </div>
              </template>
              <v-list-item-title class="text-subtitle-1">Logout</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-window-item>

        <!-- Settings Tab -->
        <v-window-item value="222">
          <v-list class="px-2" aria-label="profile list">
            <v-list-item
              v-for="(item, index) in profiledata2"
              :key="index"
              color="primary"
              :base-color="customizer.actTheme === 'dark' ? 'lightText' : 'secondary'"
              rounded="md"
              :value="item.title"
            >
              <template v-slot:prepend>
                <div class="me-4">
                  <SvgSprite :name="item.icon || ''" style="width: 18px; height: 18px" />
                </div>
              </template>
              <v-list-item-title class="text-subtitle-1">{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-window-item>
      </v-window>
    </perfect-scrollbar>
  </div>
</template>