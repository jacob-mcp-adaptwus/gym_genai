<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// theme breadcrumb
const page = ref({ title: 'Multi Column' });
const breadcrumbs = ref([
  {
    title: 'Layouts',
    disabled: false,
    href: '#'
  },
  {
    title: 'Multi Column',
    disabled: true,
    href: '#'
  }
]);

const checkbox1 = ref(true);
const checkbox2 = ref(false);
const checkbox3 = ref(false);
const checkbox4 = ref(true);
const checkbox5 = ref(false);
const checkbox6 = ref(true);
const checkbox7 = ref(false);
const checkbox8 = ref(true);
const checkbox9 = ref(false);
const checkbox10 = ref(false);
</script>

<template>
  <!-- ----------------------------------------------------- -->
  <!-- Multi Column Forms -->
  <!-- ----------------------------------------------------- -->
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <!-- 2 Columns Form Layout -->
    <v-col cols="12">
      <UiParentCard title="2 Columns Form Layout">
        <v-row>
          <!-- column 1 -->
          <v-col cols="12" lg="6">
            <v-label class="mb-2">Name</v-label>
            <v-text-field
              hint="Please enter your full name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter full name"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" lg="6">
            <v-label class="mb-2">Email</v-label>
            <v-text-field
              hint="Please enter your Email"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter email"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
          <!-- column 3 -->
          <v-col cols="12" lg="6">
            <v-label class="mb-2">Password</v-label>
            <v-text-field
              hint="Please enter Password"
              persistent-hint
              variant="outlined"
              type="password"
              persistent-placeholder
              placeholder="Enter password"
              density="comfortable"
              color="primary"
            >
              <template v-slot:append-inner>
                <SvgSprite name="custom-lock-2" class="text-lightText" style="width: 24px; height: 24px" />
              </template>
            </v-text-field>
          </v-col>
          <!-- column 4 -->
          <v-col cols="12" lg="6">
            <v-label class="mb-2">Profile URL</v-label>
            <v-text-field
              hint="Please enter your Profile URL"
              persistent-hint
              variant="outlined"
              type="password"
              persistent-placeholder
              placeholder="Please enter your Profile URL"
              density="comfortable"
              color="primary"
            >
              <template v-slot:append-inner>
                <SvgSprite name="custom-link3" class="text-lightText" style="width: 24px; height: 24px" />
              </template>
            </v-text-field>
          </v-col>
          <!-- column 5 -->
          <v-col cols="12" lg="6">
            <v-label class="mb-2">Language</v-label>
            <div class="d-flex ga-4">
              <v-checkbox
                density="compact"
                v-model="checkbox1"
                hide-details
                color="primary"
                label="English"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox
                density="compact"
                v-model="checkbox2"
                hide-details
                color="primary"
                label="French"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox density="compact" v-model="checkbox3" hide-details color="primary" label="Dutch" class="flex-grow-0"></v-checkbox>
            </div>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
    <!-- 2 Columns Horizontal Form Layout -->
    <v-col cols="12">
      <UiParentCard title="2 Columns Horizontal Form Layout">
        <v-row>
          <!-- column 1 -->
          <v-col cols="12" sm="6">
            <!-- row 1 -->
            <v-row>
              <v-col cols="12" lg="4" md="3" class="pb-md-3 pb-0">
                <v-label class="mt-md-4">Name</v-label>
              </v-col>
              <v-col cols="12" lg="8" md="9">
                <v-text-field
                  hint="Please enter your full name"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter full name"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
            <!-- row 2 -->
            <v-row class="mt-3">
              <v-col cols="12" lg="4" md="3" class="pb-md-3 pb-0">
                <v-label class="mt-md-4">Password</v-label>
              </v-col>
              <v-col cols="12" lg="8" md="9">
                <v-text-field
                  hint="Please enter Password"
                  persistent-hint
                  variant="outlined"
                  type="password"
                  persistent-placeholder
                  placeholder="Enter password"
                  density="comfortable"
                  color="primary"
                >
                  <template v-slot:append-inner>
                    <SvgSprite name="custom-lock-2" class="text-lightText" style="width: 24px; height: 24px" />
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
            <!-- row 3 -->
            <v-row class="mt-3 align-center">
              <v-col cols="12" lg="4" md="3" class="pb-md-3 pb-0">
                <v-label>Language</v-label>
              </v-col>
              <v-col cols="12" lg="8" md="9">
                <div class="d-flex ga-4">
                  <v-checkbox
                    density="compact"
                    v-model="checkbox8"
                    hide-details
                    color="primary"
                    label="English"
                    class="flex-grow-0"
                  ></v-checkbox>
                  <v-checkbox
                    density="compact"
                    v-model="checkbox9"
                    hide-details
                    color="primary"
                    label="French"
                    class="flex-grow-0"
                  ></v-checkbox>
                  <v-checkbox
                    density="compact"
                    v-model="checkbox10"
                    hide-details
                    color="primary"
                    label="Dutch"
                    class="flex-grow-0"
                  ></v-checkbox>
                </div>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" sm="6">
            <!-- row 1 -->
            <v-row>
              <v-col cols="12" lg="4" md="3" class="pb-md-3 pb-0">
                <v-label class="mt-md-4">Email</v-label>
              </v-col>
              <v-col cols="12" lg="8" md="9">
                <v-text-field
                  hint="Please enter your Email"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter email"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
            <!-- row 2 -->
            <v-row class="mt-3">
              <v-col cols="12" lg="4" md="3" class="pb-md-3 pb-0">
                <v-label class="mt-md-4">Profile URL</v-label>
              </v-col>
              <v-col cols="12" lg="8" md="9">
                <v-text-field
                  hint="Please enter your Profile URL"
                  persistent-hint
                  variant="outlined"
                  type="password"
                  persistent-placeholder
                  placeholder="Please enter your Profile URL"
                  density="comfortable"
                  color="primary"
                >
                  <template v-slot:append-inner>
                    <SvgSprite name="custom-link3" class="text-lightText" style="width: 24px; height: 24px" />
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
    <!-- 3 Columns Form Layout -->
    <v-col cols="12">
      <UiParentCard title="3 Columns Form Layout">
        <v-row>
          <!-- column 1 -->
          <v-col cols="12" md="4" sm="6">
            <v-label class="mb-2">Name</v-label>

            <v-text-field
              hint="Please enter your full name"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter full name"
              density="comfortable"
              color="primary"
            ></v-text-field>
            <v-label class="mb-2 mt-5">Contact</v-label>

            <v-text-field
              hint="Please enter your contact"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter contact number"
              density="comfortable"
              color="primary"
            ></v-text-field>
            <v-label class="mb-2 mt-5">Address</v-label>

            <v-text-field
              hint="Please enter your address"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter your address"
              density="comfortable"
              color="primary"
            ></v-text-field>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" md="4" sm="6">
            <v-label class="mb-2">Email</v-label>

            <v-text-field
              hint="Please enter your Email"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter email"
              density="comfortable"
              color="primary"
            ></v-text-field>

            <v-label class="mb-2 mt-5">Profile URL</v-label>

            <v-text-field
              hint="Please enter your Profile URL"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter Profile URL"
              density="comfortable"
              color="primary"
            >
              <template v-slot:append-inner>
                <SvgSprite name="custom-link3" class="text-lightText" style="width: 24px; height: 24px" />
              </template>
            </v-text-field>

            <v-label class="mb-2 mt-5">User Type</v-label>
            <div class="d-flex ga-4">
              <v-checkbox
                density="compact"
                v-model="checkbox4"
                hide-details
                color="primary"
                label="Administrator"
                class="flex-grow-0"
              ></v-checkbox>
              <v-checkbox
                density="compact"
                v-model="checkbox5"
                hide-details
                color="primary"
                label="Author"
                class="flex-grow-0"
              ></v-checkbox>
            </div>
          </v-col>
          <!-- column 3 -->
          <v-col cols="12" md="4" sm="6">
            <v-label class="mb-2">Password</v-label>

            <v-text-field
              hint="Please enter Password"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter password"
              density="comfortable"
              color="primary"
            >
              <template v-slot:prepend-inner>
                <SvgSprite name="custom-lock-2" class="text-lightText" style="width: 24px; height: 24px" />
              </template>
            </v-text-field>
            <v-label class="mb-2 mt-5">Pincode</v-label>

            <v-text-field
              hint="Please enter your postcode"
              persistent-hint
              variant="outlined"
              persistent-placeholder
              placeholder="Enter your postcode"
              density="comfortable"
              color="primary"
            >
            </v-text-field>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
    <!-- 3 Columns Form Layout -->
    <v-col cols="12">
      <UiParentCard title="3 Columns Form Layout">
        <!-- Row 1 -->
        <v-row class="pb-6">
          <!-- column 1 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Name</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your full name"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter full name"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Email</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your Email"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter email"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 3 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Password</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter Password"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter password"
                  density="comfortable"
                  color="primary"
                >
                  <template v-slot:prepend-inner>
                    <SvgSprite name="custom-lock-2" class="text-lightText" style="width: 24px; height: 24px" />
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <!-- row 2 -->
        <v-row class="pt-6">
          <!-- column 1 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Contact</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your contact"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter contact number"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Profile URL</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your Profile URL"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter Profile URL"
                  density="comfortable"
                  color="primary"
                >
                  <template v-slot:append-inner>
                    <SvgSprite name="custom-link3" class="text-lightText" style="width: 24px; height: 24px" />
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 3 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center pb-6">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Pincode</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your postcode"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter your postcode"
                  density="comfortable"
                  color="primary"
                >
                </v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <!-- row 3 -->
        <v-row class="pt-6">
          <!-- column 1 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center pb-md-0 pb-6">
              <v-col cols="12" md="4" class="pb-0 pb-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">Address</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field
                  hint="Please enter your address"
                  persistent-hint
                  variant="outlined"
                  persistent-placeholder
                  placeholder="Enter your address"
                  density="comfortable"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <!-- column 2 -->
          <v-col cols="12" lg="4" md="6">
            <v-row class="d-flex align-center">
              <v-col cols="12" md="4" class="py-0 py-md-3">
                <v-label class="d-flex justify-start justify-md-end mb-0 mb-md-5">User Type</v-label>
              </v-col>
              <v-col cols="12" md="8">
                <div>
                  <v-checkbox
                    density="compact"
                    v-model="checkbox6"
                    hide-details
                    color="primary"
                    label="Administrator"
                    class="flex-grow-0"
                  ></v-checkbox>
                  <v-checkbox
                    density="compact"
                    v-model="checkbox7"
                    hide-details
                    color="primary"
                    label="Author"
                    class="flex-grow-0"
                  ></v-checkbox>
                </div>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
