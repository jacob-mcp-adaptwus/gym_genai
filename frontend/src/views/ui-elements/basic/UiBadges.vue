<script setup lang="ts">
import { ref } from 'vue';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Badge' });
const subContent = ref({ content: 'Badge generates a small badge to the top-right of its child(ren).' });
const path = ref({ filepath: 'src/views/ui-elements/basic/badge' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/badges/' });
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <div class="d-flex align-center flex-row ga-6">
              <v-badge color="primary" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="secondary" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="success" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="warning" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="info" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="error" content="4" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Light Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Light">
            <div class="d-flex align-center flex-row ga-6">
              <v-badge color="lightprimary" content="4" text-color="primary" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightsecondary" content="4" text-color="secondary" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightsuccess" content="4" text-color="success" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightwarning" content="4" text-color="warning" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightinfo" content="4" text-color="info" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lighterror" content="4" text-color="error" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Maximum Value Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Maximum Value">
            <div class="d-flex align-center flex-row ga-6">
              <v-badge color="primary" content="99" offset-x="-2" offset-y="-3">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="secondary" content="99+" offset-x="2" offset-y="-3">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightprimary" content="999+" text-color="primary" class="me-2" offset-x="2" offset-y="-3">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="lightsecondary" content="99" text-color="secondary" offset-x="2" offset-y="-3">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="error" content="99" offset-x="2" offset-y="-3">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Dot Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Dot Badges">
            <div class="d-flex align-center flex-wrap ga-6">
              <v-badge color="primary" dot offset-x="-4" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="secondary" dot offset-x="-4" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="success" dot offset-x="-4" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="warning" dot offset-x="-4" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="info" dot offset-x="-4" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="error" dot offset-x="-4" offset-y="-5"> Typography </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Customized Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Customized Badges">
            <div class="d-flex align-center ga-6">
              <v-badge color="error" size="large" content="2">
                <SvgSprite name="custom-shopping-cart" />
              </v-badge>
              <v-badge color="primary" inline content="2">
                <SvgSprite name="custom-shopping-cart" />
              </v-badge>
              <v-badge color="secondary" bordered content="2">
                <SvgSprite name="custom-shopping-cart" />
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Alignment Badges -->
        <v-col cols="12" md="6">
          <UiParentCard title="Alignment">
            <div class="d-flex align-center flex-row ga-6">
              <v-badge color="primary" location="top end" content="9" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="primary" location="top end" dot offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="primary" location="bottom end" content="9" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="primary" location="top start" content="9" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
              <v-badge color="primary" location="bottom start" content="99" offset-x="-5" offset-y="-5">
                <SvgSprite name="custom-mail-outline" />
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="Overlap">
            <div class="d-flex align-center ga-2 flex-wrap">
              <v-badge color="primary" location="top end" dot offset-x="0" offset-y="0">
                <v-avatar color="primary" variant="tonal" rounded="circle">
                  <SvgSprite name="custom-user-fill" />
                </v-avatar>
              </v-badge>
              <v-badge color="primary" location="top end" dot offset-x="-2" offset-y="-2">
                <v-avatar color="primary" variant="flat" rounded="md">
                  <SvgSprite name="custom-user-outline" />
                </v-avatar>
              </v-badge>
              <v-badge color="primary" location="top end" dot offset-x="-3" offset-y="-3">
                <v-avatar color="primary" variant="outlined" rounded="0">
                  <SvgSprite name="custom-user-fill" />
                </v-avatar>
              </v-badge>
              <v-badge color="primary" location="top end" dot offset-x="2" offset-y="2">
                <v-avatar color="primary" variant="outlined" rounded="circle">
                  <SvgSprite name="custom-user-fill" />
                </v-avatar>
              </v-badge>
            </div>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
