<script setup lang="ts">
import { ref, shallowRef } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const cpassword = ref('');
const npassword = ref('');
const conpassword = ref('');
const show1 = ref(false);
const show2 = ref(false);
const show3 = ref(false);

const items = shallowRef([
  {
    title: 'At least 8 characters'
  },
  {
    title: 'At least 1 lower letter (a-z)'
  },
  {
    title: 'At least 1 uppercase letter (A-Z)'
  },
  {
    title: 'At least 1 number (0-9)'
  },
  {
    title: 'At least 1 special characters'
  }
]);
</script>

<template>
  <v-row>
    <v-col cols="12">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="pa-5">
            <h5 class="text-subtitle-1 mb-0">Change Password</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col cols="12" md="6">
                <v-row>
                  <v-col cols="12">
                    <v-label class="mb-2">Old Password</v-label>
                    <v-text-field
                      color="primary"
                      single-line
                      placeholder="Enter Old Password"
                      variant="outlined"
                      density="comfortable"
                      :type="show1 ? 'text' : 'password'"
                      hide-details
                      v-model="cpassword"
                    >
                      <template v-slot:append-inner>
                        <SvgSprite
                          name="custom-eye-invisible"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show1 == false"
                          @click="show1 = !show1"
                        />
                        <SvgSprite
                          name="custom-eye"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show1 == true"
                          @click="show1 = !show1"
                        />
                      </template>
                    </v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-label class="mb-2">New Password</v-label>
                    <v-text-field
                      color="primary"
                      single-line
                      placeholder="Enter New Password"
                      density="comfortable"
                      variant="outlined"
                      :type="show2 ? 'text' : 'password'"
                      hide-details
                      v-model="npassword"
                    >
                      <template v-slot:append-inner>
                        <SvgSprite
                          name="custom-eye-invisible"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show2 == false"
                          @click="show2 = !show2"
                        />
                        <SvgSprite
                          name="custom-eye"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show2 == true"
                          @click="show2 = !show2"
                        />
                      </template>
                    </v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-label class="mb-2">Confirm Password</v-label>
                    <v-text-field
                      color="primary"
                      single-line
                      placeholder="Enter Confirm Password"
                      density="comfortable"
                      variant="outlined"
                      :type="show3 ? 'text' : 'password'"
                      hide-details
                      v-model="conpassword"
                    >
                      <template v-slot:append-inner>
                        <SvgSprite
                          name="custom-eye-invisible"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show3 == false"
                          @click="show3 = !show3"
                        />
                        <SvgSprite
                          name="custom-eye"
                          class="text-secondary"
                          style="width: 20px; height: 20px"
                          v-if="show3 == true"
                          @click="show3 = !show3"
                        />
                      </template>
                    </v-text-field>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" md="6">
                <h5 class="text-h5">New Password must contain:</h5>
                <v-list aria-label="content" aria-busy="true">
                  <v-list-item v-for="(item, index) in items" :key="index" border>
                    <template v-slot:prepend>
                      <SvgSprite name="custom-line" class="me-2" style="width: 24px; height: 24px" />
                    </template>
                    <h6 class="text-h6 mb-0">{{ item.title }}</h6>
                  </v-list-item>
                </v-list>
              </v-col>
            </v-row>
            <div class="text-end mt-4">
              <v-btn color="secondary" rounded="md" variant="outlined" class="me-2">Cancel</v-btn>
              <v-btn color="primary" rounded="md" variant="flat">Update profile</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
