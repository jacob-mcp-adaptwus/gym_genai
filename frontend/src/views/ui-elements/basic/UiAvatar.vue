<script setup lang="ts">
import { ref } from 'vue';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Avatar' });
const subContent = ref({ content: 'Avatars are found throughout vuetify design with uses in everything from tables to dialog menus.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/avatar' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/avatars/' });
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Basic Avatar -->
            <v-col cols="12">
              <UiParentCard title="Basic">
                <div>
                  <v-avatar variant="tonal" color="primary">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Image Avatar -->
            <v-col cols="12">
              <UiParentCard title="Vector">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar size="40" variant="flat" color="lightprimary">
                    <img src="@/assets/images/users/vector-1.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="40" variant="flat" color="lightprimary">
                    <img src="@/assets/images/users/vector-2.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="40" variant="flat" color="lightprimary">
                    <img src="@/assets/images/users/vector-3.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="40" variant="flat" color="lightprimary">
                    <img src="@/assets/images/users/vector-4.png" width="40" alt="Julia" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Variant Avatar -->
            <v-col cols="12">
              <UiParentCard title="Variants">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar size="40" color="lightprimary" class="text-primary" variant="flat">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" class="text-primary" rounded="md">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="primary" variant="flat" rounded="0">
                    <SvgSprite name="custom-user-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="lightprimary" class="text-primary" variant="flat"> U </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" class="text-primary" rounded="md"> U </v-avatar>
                  <v-avatar size="40" color="primary" variant="flat" rounded="0"> U </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Icon Avatar -->
            <v-col cols="12">
              <UiParentCard title="Icon">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar size="32" color="primary">
                    <SvgSprite name="custom-user-fill" style="width: 18px; height: 18px" />
                  </v-avatar>
                  <v-avatar size="32" variant="flat" color="success">
                    <SvgSprite name="custom-mail-fill" style="width: 18px; height: 18px" />
                  </v-avatar>
                  <v-avatar size="32" variant="flat" color="error">
                    <SvgSprite name="custom-setting-fill" style="width: 18px; height: 18px" />
                  </v-avatar>
                  <v-avatar size="32" color="primary" variant="tonal">
                    <SvgSprite name="custom-plus" style="width: 18px; height: 18px" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- With badge Avatar -->
            <v-col cols="12">
              <UiParentCard title="With Badge">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-badge color="error" content="4">
                    <img src="@/assets/images/users/avatar-6.png" class="rounded-circle" width="40" alt="Julia" />
                  </v-badge>
                  <v-badge color="error" dot offset-x="3">
                    <v-avatar color="secondary" variant="flat" rounded="circle">
                      <SvgSprite name="custom-user-outline" style="width: 18px; height: 18px" />
                    </v-avatar>
                  </v-badge>
                  <v-badge color="error" dot offset-x="3">
                    <img src="@/assets/images/users/avatar-2.png" class="rounded-circle" width="40" alt="Julia" />
                  </v-badge>
                  <v-badge color="error" dot offset-x="3">
                    <v-avatar color="primary" variant="outlined" rounded="circle"> U </v-avatar>
                  </v-badge>
                  <v-badge color="error" dot offset-x="3">
                    <v-avatar color="lightprimary" rounded="circle">
                      <img src="@/assets/images/users/vector-2.png" class="rounded-circle" width="40" alt="Julia" />
                    </v-avatar>
                  </v-badge>
                  <v-badge color="success" dot offset-x="-3" offset-y="-3">
                    <img src="@/assets/images/users/avatar-1.png" class="rounded-md" width="40" alt="Julia" />
                  </v-badge>
                  <v-badge color="transparent pa-0" bordered location="bottom end" offset-x="3" offset-y="3">
                    <img src="@/assets/images/users/avatar-1.png" class="rounded-circle" width="40" alt="Julia" />
                    <template v-slot:badge>
                      <img src="@/assets/images/users/avatar-1.png" width="16" class="rounded-circle" alt="Julia" />
                    </template>
                  </v-badge>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Image Avatar -->
            <v-col cols="12">
              <UiParentCard title="Image">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar color="lightprimary" variant="flat" rounded="circle">
                    <img src="@/assets/images/users/avatar-1.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar variant="flat" rounded="circle">
                    <img src="@/assets/images/users/avatar-2.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar variant="flat" rounded="circle">
                    <img src="@/assets/images/users/avatar-3.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar variant="flat" rounded="circle">
                    <img src="@/assets/images/users/avatar-4.png" width="40" alt="Julia" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Fallbacks Avatar -->
            <v-col cols="12">
              <UiParentCard title="Colors">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar color="primary" variant="flat">
                    <SvgSprite name="custom-user-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar color="secondary" variant="flat">
                    <SvgSprite name="custom-database-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar color="success" variant="flat">
                    <SvgSprite name="custom-circle-check-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar color="warning" variant="flat">
                    <SvgSprite name="custom-warning-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar color="info" variant="flat">
                    <SvgSprite name="custom-info-circle-outline" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar color="error" variant="flat">
                    <SvgSprite name="custom-trash" style="width: 20px; height: 20px" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Letter Avatar -->
            <v-col cols="12">
              <UiParentCard title="Letter">
                <div class="d-flex align-center ga-2">
                  <v-avatar size="32" color="lightprimary" class="text-primary" variant="flat"> U </v-avatar>
                  <v-avatar size="32" color="lighterror" class="text-error" variant="flat"> UI </v-avatar>
                  <v-avatar size="32" color="error" variant="flat"> A </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Outline Avatar -->
            <v-col cols="12">
              <UiParentCard title="Outlined">
                <div class="d-flex align-center ga-2 flex-wrap">
                  <v-avatar size="40" color="primary" variant="outlined">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" class="text-primary" rounded="md">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" rounded="0">
                    <SvgSprite name="custom-user-fill" style="width: 20px; height: 20px" />
                  </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined"> U </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" rounded="md"> U </v-avatar>
                  <v-avatar size="40" color="primary" variant="outlined" rounded="0"> U </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <v-col cols="12">
              <UiParentCard title="Avatar Group">
                <h6 class="text-subtitle-1 mb-4">Default</h6>
                <div class="d-flex align-center justify-end flex-wrap flex-row-reverse mb-4">
                  <v-avatar size="42" variant="flat" color="info" class="ms-n2"> +3 </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface" class="ms-n2">
                    <img src="@/assets/images/users/avatar-7.png" width="42" alt="vector" />
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface" class="ms-n2">
                    <img src="@/assets/images/users/avatar-6.png" width="42" alt="vector" />
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface">
                    <img src="@/assets/images/users/avatar-5.png" width="42" alt="vector" />
                  </v-avatar>
                </div>
                <v-divider></v-divider>
                <h6 class="text-subtitle-1 my-4">On Hover</h6>
                <div class="d-flex align-center justify-end flex-wrap flex-row-reverse">
                  <v-avatar size="42" variant="flat" color="primary" class="ms-n2 cursor-pointer">
                    +6
                    <v-tooltip activator="parent" location="top" aria-label="tooltip">
                      <div class="d-flex align-center justify-center flex-wrap flex-row-reverse">
                        <v-avatar size="40" variant="outlined" color="surface" class="ms-n2">
                          <img src="@/assets/images/users/avatar-9.png" width="40" alt="vector" />
                        </v-avatar>
                        <v-avatar size="40" variant="outlined" color="surface" class="ms-n2">
                          <img src="@/assets/images/users/avatar-8.png" width="40" alt="vector" />
                        </v-avatar>
                        <v-avatar size="40" variant="outlined" color="surface" class="ms-n2">
                          <img src="@/assets/images/users/avatar-7.png" width="40" alt="vector" />
                        </v-avatar>
                        <v-avatar size="40" variant="outlined" color="surface" class="ms-n2">
                          <img src="@/assets/images/users/avatar-6.png" width="40" alt="vector" />
                        </v-avatar>
                        <v-avatar size="40" variant="outlined" color="surface">
                          <img src="@/assets/images/users/avatar-5.png" width="40" alt="vector" />
                        </v-avatar>
                      </div>
                    </v-tooltip>
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface" class="ms-n2">
                    <img src="@/assets/images/users/avatar-4.png" width="42" alt="vector" />
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface" class="ms-n2">
                    <img src="@/assets/images/users/avatar-3.png" width="42" alt="vector" />
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface" class="ms-n2">
                    <img src="@/assets/images/users/avatar-2.png" width="42" alt="vector" />
                  </v-avatar>
                  <v-avatar size="42" variant="outlined" color="surface">
                    <img src="@/assets/images/users/avatar-1.png" width="42" alt="vector" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Size Avatar -->
            <v-col cols="12">
              <UiParentCard title="Size Avatar">
                <div class="d-flex align-center flex-wrap ga-2">
                  <v-avatar size="25" color="primary" variant="tonal">
                    <img src="@/assets/images/users/avatar-1.png" width="25" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="40" color="secondary" variant="tonal">
                    <img src="@/assets/images/users/avatar-2.png" width="40" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="50" color="success" variant="tonal">
                    <img src="@/assets/images/users/avatar-3.png" width="50" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="52" color="info" variant="tonal">
                    <img src="@/assets/images/users/avatar-4.png" width="52" alt="Julia" />
                  </v-avatar>
                  <v-avatar size="64" color="warning" variant="tonal">
                    <img src="@/assets/images/users/avatar-5.png" width="64" alt="Julia" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Fallbacks Avatar -->
            <v-col cols="12">
              <UiParentCard title="Fallbacks">
                <div class="d-flex align-center ga-2">
                  <v-avatar size="40" color="error" variant="flat"> B </v-avatar>
                  <v-avatar size="40" color="error" class="text-error" variant="outlined"> R </v-avatar>
                  <v-avatar size="40" color="error" variant="tonal">
                    <SvgSprite name="custom-user-bold" style="width: 18px; height: 18px" />
                  </v-avatar>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
