<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Breadcrumbs' });
const subContent = ref({ content: 'Breadcrumbs allow users to make selections from a range of values.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/breadcrumb' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/breadcrumbs/' });

// breadcrumb data
const items = ref([
  {
    title: 'Home',
    disabled: false,
    href: '/'
  },
  {
    title: 'Kanban',
    disabled: true,
    href: ''
  }
]);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <v-toolbar rounded="md" color="containerBg" dark prominent :border="true">
              <v-breadcrumbs :items="items" class="mb-0 pa-6"></v-breadcrumbs>
            </v-toolbar>
          </UiParentCard>
        </v-col>
        <!-- Custom Separator -->
        <v-col cols="12" md="6">
          <UiParentCard title="Custom Separator">
            <v-toolbar rounded="md" color="containerBg" dark prominent :border="true">
              <v-breadcrumbs :items="items" class="mb-0 pa-6">
                <template v-slot:divider>
                  <div class="d-flex align-center">
                    <SvgSprite name="custom-line" style="width: 14px; height: 14px" />
                  </div>
                </template>
              </v-breadcrumbs>
            </v-toolbar>
          </UiParentCard>
        </v-col>
        <!-- With Title -->
        <v-col cols="12" md="6">
          <UiParentCard title="With Title">
            <v-toolbar rounded="md" color="containerBg" class="breadcrumb-with-title" dark prominent :border="true">
              <div>
                <v-toolbar-title class="ms-6 mb-n2 text-h2 font-weight-bold">Kanban</v-toolbar-title>
                <v-breadcrumbs :items="items" class="pb-0 mb-0 pa-6 pt-3">
                  <template v-slot:divider>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-outline" style="width: 13px; height: 13px" />
                    </div>
                  </template>
                </v-breadcrumbs>
              </div>
            </v-toolbar>
          </UiParentCard>
        </v-col>
        <!-- Title Bottom -->
        <v-col cols="12" md="6">
          <UiParentCard title="Title Bottom">
            <v-toolbar rounded="md" color="containerBg" class="breadcrumb-with-title" dark prominent :border="true">
              <div>
                <v-breadcrumbs :items="items" class="pt-0 pb-3 pa-6">
                  <template v-slot:divider>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-outline" style="width: 13px; height: 13px" />
                    </div>
                  </template>
                </v-breadcrumbs>
                <v-toolbar-title class="ms-6 mt-n4 text-h2 font-weight-bold">Kanban</v-toolbar-title>
              </div>
            </v-toolbar>
          </UiParentCard>
        </v-col>
        <!-- With Icons -->
        <v-col cols="12">
          <UiParentCard title="With Icons">
            <v-toolbar rounded="md" color="containerBg" class="breadcrumb-with-title" dark prominent :border="true">
              <div>
                <v-toolbar-title class="ms-6 mb-n4 text-h2 font-weight-bold">Kanban</v-toolbar-title>
                <v-breadcrumbs :items="items" class="pb-0 mb-0 pa-6">
                  <template v-slot:divider>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-outline" style="width: 13px; height: 13px" />
                    </div>
                  </template>
                  <template v-slot:prepend>
                    <SvgSprite name="custom-home-outline" class="me-1 text-lightText" style="width: 16px; height: 16px" />
                  </template>
                </v-breadcrumbs>
              </div>
            </v-toolbar>
          </UiParentCard>
        </v-col>
        <!-- with Divider -->
        <v-col cols="12" md="6">
          <UiParentCard title="No Card with Divider">
            <v-toolbar rounded="md" class="pb-4 breadcrumb-height" color="transparent" dark prominent>
              <div>
                <v-toolbar-title class="mb-n2 text-h2 font-weight-bold">Kanban</v-toolbar-title>
                <v-breadcrumbs :items="items" class="pb-0 mb-0 ps-0">
                  <template v-slot:divider>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-outline" style="width: 13px; height: 13px" />
                    </div>
                  </template>
                </v-breadcrumbs>
              </div>
            </v-toolbar>
            <v-divider></v-divider>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="No Card with Divider">
            <v-toolbar rounded="md" class="breadcrumb-height" color="transparent" dark prominent>
              <div>
                <v-toolbar-title class="mb-n2 text-h2 font-weight-bold">Kanban</v-toolbar-title>
                <v-breadcrumbs :items="items" class="pb-0 mb-0 ps-0">
                  <template v-slot:divider>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-outline" style="width: 13px; height: 13px" />
                    </div>
                  </template>
                </v-breadcrumbs>
              </div>
            </v-toolbar>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
