<script setup lang="ts"></script>

<template>
  <v-row>
    <v-col cols="12" md="8">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="px-5 py-6">
            <h5 class="text-subtitle-1 mb-0">Change Password</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col cols="12">
                <v-label class="mb-2">Current password</v-label>
                <v-text-field
                  type="text"
                  single-line
                  placeholder="Enter Current password"
                  density="comfortable"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-label class="mb-2">New Password</v-label>
                <v-text-field
                  type="email"
                  single-line
                  placeholder="Enter New Password"
                  density="comfortable"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-label class="mb-2">Re-enter New Password</v-label>
                <v-text-field
                  type="text"
                  single-line
                  placeholder="Enter Confirm Password"
                  density="comfortable"
                  color="primary"
                  variant="outlined"
                  hide-details
                ></v-text-field>
              </v-col>
            </v-row>
            <v-btn color="primary" rounded="md" variant="flat" class="mt-5">Change Password</v-btn>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
    <v-col cols="12" md="4">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-6">
            <h5 class="text-subtitle-1 mb-0">Delete Account</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <p class="text-lightText">
              To deactivate your account, first delete its resources. If you are the only owner of any teams, either assign another owner or
              deactivate the team.
            </p>

            <v-btn color="error" rounded="md" variant="outlined" class="mt-4">Deactivate Account</v-btn>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
