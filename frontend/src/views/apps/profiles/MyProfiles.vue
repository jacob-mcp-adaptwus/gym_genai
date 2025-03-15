<script setup lang="ts">
import { ref, onMounted, computed, watch, onBeforeUnmount } from 'vue';
import { useProfileStore } from '@/stores/profiles';
import { Trash2, Edit, AlertCircle, Search, UserPlus } from 'lucide-vue-next';
import type { Profile, CreateProfileRequest, UpdateProfileRequest } from '@/services/profileService';

const profileStore = useProfileStore();
const isLoading = computed(() => profileStore.isLoading);

// State management
const selectedProfile = ref<Profile | null>(null);
const searchQuery = ref('');
const deleteDialog = ref(false);
const profileToDelete = ref<Profile | null>(null);
const editDialog = ref(false);
const createDialog = ref(false);
const hasUnsavedChanges = ref(false);
const saveSnackbar = ref(false);
const saveSnackbarText = ref('');
const saveSnackbarColor = ref('success');

// Form state
const formProfile = ref<CreateProfileRequest & UpdateProfileRequest>({
  profileName: '',
  demographics: '',
  generalBackground: '',
  mathAbility: '',
  engagement: '',
  specialConsiderations: '',
  active: true
});

// Computed properties
const filteredProfiles = computed(() => {
  const profiles = profileStore.getSortedProfiles;
  
  if (!searchQuery.value) {
    return profiles;
  }
  
  const query = searchQuery.value.toLowerCase();
  return profiles.filter(profile => 
    profile.profileName.toLowerCase().includes(query) ||
    profile.demographics.toLowerCase().includes(query) ||
    profile.generalBackground.toLowerCase().includes(query) ||
    profile.mathAbility.toLowerCase().includes(query)
  );
});

// Initialize data
onMounted(async () => {
  try {
    await profileStore.fetchProfiles();
  } catch (err) {
    console.error('Error in MyProfiles mounted:', err);
    showError(err instanceof Error ? err.message : 'Failed to fetch profiles');
  }
});

// Watch for changes in the profile store
watch(() => profileStore.getSortedProfiles, (newProfiles) => {
  console.log('Profiles updated:', newProfiles);
}, { immediate: true });

const handleSelectProfile = (profile: Profile) => {
  selectedProfile.value = profile;
  formProfile.value = { ...profile };
};

const handleEditClick = (profile: Profile) => {
  formProfile.value = { ...profile };
  editDialog.value = true;
};

const handleCreateClick = () => {
  formProfile.value = {
    profileName: '',
    demographics: '',
    generalBackground: '',
    mathAbility: '',
    engagement: '',
    specialConsiderations: '',
    active: true
  };
  createDialog.value = true;
};

const handleDeleteClick = (profile: Profile) => {
  profileToDelete.value = profile;
  deleteDialog.value = true;
};

const confirmDelete = async () => {
  const profileToDeleteValue = profileToDelete.value;
  if (!profileToDeleteValue) return;
  
  try {
    await profileStore.deleteProfile(profileToDeleteValue.profileName);
    deleteDialog.value = false;
    
    if (selectedProfile.value?.profileName === profileToDeleteValue.profileName) {
      selectedProfile.value = null;
    }
    
    profileToDelete.value = null;
    showSuccess('Profile deleted successfully');
  } catch (err) {
    showError(err instanceof Error ? err.message : 'Failed to delete profile');
  }
};

const handleSaveProfile = async (isCreate: boolean = false) => {
  try {
    if (isCreate) {
      await profileStore.createProfile(formProfile.value);
      createDialog.value = false;
      showSuccess('Profile created successfully');
    } else {
      if (!selectedProfile.value) return;
      
      await profileStore.updateProfile(
        selectedProfile.value.profileName,
        formProfile.value
      );
      editDialog.value = false;
      showSuccess('Profile updated successfully');
    }
  } catch (err) {
    showError(err instanceof Error ? err.message : 'Failed to save profile');
  }
};

const showSuccess = (message: string) => {
  saveSnackbarText.value = message;
  saveSnackbarColor.value = 'success';
  saveSnackbar.value = true;
};

const showError = (message: string) => {
  saveSnackbarText.value = message;
  saveSnackbarColor.value = 'error';
  saveSnackbar.value = true;
};

const handleCloseSnackbar = () => {
  saveSnackbar.value = false;
  profileStore.clearSaveStatus();
};

// Format date helper
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  });
};

// Cleanup function
onBeforeUnmount(() => {
  profileStore.clearError();
  profileStore.clearSaveStatus();
});
</script>
<template>
  <v-container fluid>
    <v-row>
      <!-- Left Column: Profile List -->
      <v-col cols="12" md="4">
        <v-card elevation="1">
          <v-card-title class="d-flex align-center py-4 px-4">
            Student Profiles
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              prepend-icon="+"
              size="small"
              @click="handleCreateClick"
            >
              New Profile
            </v-btn>
          </v-card-title>

          <v-card-text>
            <!-- Search Bar -->
            <v-text-field
              v-model="searchQuery"
              label="Search profiles"
              variant="outlined"
              density="comfortable"
              hide-details
              class="mb-4"
            >
              <template v-slot:prepend-inner>
                <Search class="text-medium-emphasis" :size="20" />
              </template>
            </v-text-field>

            <!-- Profiles List -->
            <v-list v-if="filteredProfiles.length > 0" lines="two">
              <v-list-item
                v-for="profile in filteredProfiles"
                :key="profile.profileName"
                :active="selectedProfile?.profileName === profile.profileName"
                @click="handleSelectProfile(profile)"
                class="mb-2 rounded profile-item"
              >
                <template v-slot:prepend>
                  <v-avatar
                    :color="profile.active ? 'primary' : 'grey'"
                    size="40"
                  >
                    {{ profile.profileName[0].toUpperCase() }}
                  </v-avatar>
                </template>

                <v-list-item-title class="text-subtitle-1 font-weight-medium mb-1">
                  {{ profile.profileName }}
                  <v-chip
                    v-if="!profile.active"
                    size="x-small"
                    color="grey"
                    class="ml-2"
                  >
                    Inactive
                  </v-chip>
                </v-list-item-title>

                <v-list-item-subtitle class="text-wrap">
                  {{ profile.demographics }}
                </v-list-item-subtitle>

                <template v-slot:append>
                  <v-btn
                    variant="text"
                    color="primary"
                    size="small"
                    class="mr-1"
                    @click.stop="handleEditClick(profile)"
                  >
                    <Edit :size="20" />
                  </v-btn>
                  <v-btn
                    variant="text"
                    color="error"
                    size="small"
                    @click.stop="handleDeleteClick(profile)"
                  >
                    <Trash2 :size="20" />
                  </v-btn>
                </template>
              </v-list-item>
            </v-list>

            <!-- Empty State -->
            <div 
              v-else-if="!isLoading" 
              class="text-center empty-state pa-4"
            >
              <UserPlus
                :size="64"
                class="mb-4 text-primary"
              />
              <h3 class="text-h5 mb-2">No profiles found</h3>
              <p class="text-medium-emphasis">
                {{ searchQuery ? 'Try different search terms' : 'Create your first student profile' }}
              </p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Right Column: Profile Details -->
      <v-col cols="12" md="8">
        <v-card v-if="selectedProfile" elevation="1">
          <v-card-title class="py-4 px-4">
            {{ selectedProfile.profileName }}
            <v-chip
              :color="selectedProfile.active ? 'success' : 'grey'"
              size="small"
              class="ml-2"
            >
              {{ selectedProfile.active ? 'Active' : 'Inactive' }}
            </v-chip>
          </v-card-title>

          <v-card-text>
            <v-row>
              <v-col cols="12" md="6">
                <h3 class="text-h6 mb-2">Demographics</h3>
                <v-card variant="outlined" class="mb-4 pa-4">
                  <p class="text-body-1">{{ selectedProfile.demographics }}</p>
                </v-card>

                <h3 class="text-h6 mb-2">General Background</h3>
                <v-card variant="outlined" class="mb-4 pa-4">
                  <p class="text-body-1">{{ selectedProfile.generalBackground }}</p>
                </v-card>
              </v-col>

              <v-col cols="12" md="6">
                <h3 class="text-h6 mb-2">Math Ability</h3>
                <v-card variant="outlined" class="mb-4 pa-4">
                  <p class="text-body-1">{{ selectedProfile.mathAbility }}</p>
                </v-card>

                <h3 class="text-h6 mb-2">Engagement Level</h3>
                <v-card variant="outlined" class="mb-4 pa-4">
                  <p class="text-body-1">{{ selectedProfile.engagement }}</p>
                </v-card>

                <h3 class="text-h6 mb-2">Special Considerations</h3>
                <v-card variant="outlined" class="mb-4 pa-4">
                  <p class="text-body-1">{{ selectedProfile.specialConsiderations }}</p>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>

          <v-card-actions class="pa-4">
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              prepend-icon="edit"
              @click="handleEditClick(selectedProfile)"
            >
              Edit Profile
            </v-btn>
          </v-card-actions>
        </v-card>

        <!-- Empty State -->
        <v-card v-else elevation="1" class="d-flex align-center justify-center" min-height="400">
          <div class="text-center">
            <UserPlus
              :size="64"
              class="mb-4 text-primary"
            />
            <h3 class="text-h5 mb-2">No Profile Selected</h3>
            <p class="text-medium-emphasis">
              Select a profile from the list to view details
            </p>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <!-- Create Profile Dialog -->
    <v-dialog v-model="createDialog" max-width="800">
      <v-card>
        <v-card-title class="text-h5 pa-4">
          Create New Profile
        </v-card-title>

        <v-card-text class="pa-4">
          <v-form @submit.prevent="handleSaveProfile(true)">
            <v-text-field
              v-model="formProfile.profileName"
              label="Profile Name"
              required
              variant="outlined"
              class="mb-4"
            ></v-text-field>

            <v-textarea
              v-model="formProfile.demographics"
              label="Demographics"
              required
              variant="outlined"
              class="mb-4"
              hint="Age, grade level, language preferences, etc."
            ></v-textarea>

            <v-textarea
              v-model="formProfile.generalBackground"
              label="General Background"
              required
              variant="outlined"
              class="mb-4"
              hint="Student's learning history and general academic background"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.mathAbility"
              label="Math Ability"
              required
              variant="outlined"
              class="mb-4"
              hint="Current math skills and areas for improvement"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.engagement"
              label="Engagement Level"
              required
              variant="outlined"
              class="mb-4"
              hint="How the student engages with learning materials"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.specialConsiderations"
              label="Special Considerations"
              required
              variant="outlined"
              class="mb-4"
              hint="Any special needs, accommodations, or learning preferences"
            ></v-textarea>
          </v-form>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn
            color="grey-darken-1"
            variant="text"
            @click="createDialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            @click="handleSaveProfile(true)"
          >
            Create Profile
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Edit Profile Dialog -->
    <v-dialog v-model="editDialog" max-width="800">
      <v-card>
        <v-card-title class="text-h5 pa-4">
          Edit Profile
        </v-card-title>

        <v-card-text class="pa-4">
          <v-form @submit.prevent="handleSaveProfile(false)">
            <v-text-field
              v-model="formProfile.profileName"
              label="Profile Name"
              required
              variant="outlined"
              disabled
              class="mb-4"
            ></v-text-field>

            <v-textarea
              v-model="formProfile.demographics"
              label="Demographics"
              required
              variant="outlined"
              class="mb-4"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.generalBackground"
              label="General Background"
              required
              variant="outlined"
              class="mb-4"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.mathAbility"
              label="Math Ability"
              required
              variant="outlined"
              class="mb-4"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.engagement"
              label="Engagement Level"
              required
              variant="outlined"
              class="mb-4"
            ></v-textarea>

            <v-textarea
              v-model="formProfile.specialConsiderations"
              label="Special Considerations"
              required
              variant="outlined"
              class="mb-4"
            ></v-textarea>

            <v-switch
              v-model="formProfile.active"
              label="Active Profile"
              color="primary"
              hide-details
            ></v-switch>
          </v-form>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn
            color="grey-darken-1"
            variant="text"
            @click="editDialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            @click="handleSaveProfile(false)"
          >
            Save Changes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Delete Confirmation Dialog -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title class="text-h5 pa-4">
          Delete Profile
        </v-card-title>

        <v-card-text class="pa-4">
          Are you sure you want to delete "{{ profileToDelete?.profileName }}"? 
          This action cannot be undone.
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn
            color="grey-darken-1"
            variant="text"
            @click="deleteDialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="error"
            @click="confirmDelete"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Snackbar -->
    <v-snackbar
      v-model="saveSnackbar"
      :color="saveSnackbarColor"
      :timeout="3000"
      location="top"
    >
      {{ saveSnackbarText }}

      <template v-slot:actions>
        <v-btn
          color="white"
          variant="text"
          @click="handleCloseSnackbar"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>
<style lang="scss" scoped>
.v-container {
  max-width: 1600px;
  margin: 0 auto;
  padding-bottom: 64px;
}

// Card base styles
.v-card {
  transition: all 0.3s ease;
  border-radius: 8px;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}

// List item styles
.v-list {
  .profile-item {
    margin-bottom: 8px;
    transition: all 0.2s ease;
    border: 1px solid transparent;
    
    &:hover {
      background-color: rgba(var(--v-theme-primary), 0.05);
      transform: translateX(4px);
    }
    
    &--active {
      background-color: rgba(var(--v-theme-primary), 0.1);
      border-color: rgba(var(--v-theme-primary), 0.2);
      
      &:hover {
        background-color: rgba(var(--v-theme-primary), 0.15);
      }
    }
    
    .v-list-item-title {
      font-weight: 500;
      line-height: 1.4;
    }
    
    .v-list-item-subtitle {
      line-height: 1.6;
      margin-top: 4px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }
}

// Avatar styles
.v-avatar {
  border: 2px solid rgba(var(--v-theme-on-surface), 0.1);
  font-weight: 600;
  text-transform: uppercase;
}

// Search field styles
.v-text-field {
  :deep(.v-field__input) {
    padding: 8px 16px;
  }
  
  :deep(.v-field__outline) {
    border-radius: 8px;
  }
  
  &:focus-within {
    :deep(.v-field__outline) {
      border-color: rgb(var(--v-theme-primary));
    }
  }
}

// Form textarea styles
.v-textarea {
  :deep(.v-field__input) {
    min-height: 120px;
    line-height: 1.6;
  }
}

// Section cards
.v-card[variant="outlined"] {
  background-color: rgba(var(--v-theme-surface), 0.5);
  transition: all 0.2s ease;
  
  &:hover {
    background-color: rgba(var(--v-theme-surface), 0.8);
  }

  .text-body-1 {
    line-height: 1.6;
    white-space: pre-line;
  }
}

// Empty state styles
.empty-state {
  padding: 32px;
  text-align: center;
  
  .lucide {
    opacity: 0.7;
    margin-bottom: 16px;
  }
  
  .text-h5 {
    font-weight: 600;
    color: rgb(var(--v-theme-primary));
  }
  
  .text-medium-emphasis {
    max-width: 300px;
    margin: 0 auto;
    line-height: 1.6;
  }
}

// Dialog styles
.v-dialog {
  .v-card {
    border-radius: 12px;
    
    .v-card-title {
      font-weight: 600;
    }
  }
}

// Button hover effects
.v-btn {
  &:has(> .lucide) {
    opacity: 0.7;
    transition: all 0.2s ease;
    
    &:hover {
      opacity: 1;
      transform: scale(1.1);
    }
  }
}

// Animation classes
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

// Custom scrollbar
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: rgba(var(--v-theme-primary), 0.2);
  border-radius: 3px;
  
  &:hover {
    background-color: rgba(var(--v-theme-primary), 0.4);
  }
}

// Responsive styles
@media (max-width: 960px) {
  .v-container {
    padding: 12px;
  }
  
  .profile-item {
    margin-bottom: 4px;
    
    &:hover {
      transform: none;
    }
  }
  
  .v-avatar {
    width: 36px !important;
    height: 36px !important;
  }

  .v-card-text {
    padding: 12px !important;
  }

  .empty-state {
    padding: 24px;
  }
  
  .v-dialog {
    margin: 12px;
    
    .v-card {
      max-height: calc(100vh - 24px);
      overflow-y: auto;
    }
  }
}

// Print styles
@media print {
  .v-dialog,
  .v-snackbar,
  .v-btn:not(.v-btn--active) {
    display: none !important;
  }
}
</style>