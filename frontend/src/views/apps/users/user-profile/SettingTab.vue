<script setup lang="ts">
import { shallowRef } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const items = shallowRef([
  {
    title: 'Order Confirmation',
    icon: 'custom-file-outline-2',
    content: 'You will be notified when customer order any product',
    value: true
  },
  {
    title: 'Setup Email Notification',
    icon: 'custom-mail-outline',
    content: 'Turn on email notification to get updates through email',
    value: false
  },
  {
    title: 'Update System Notification',
    icon: 'custom-mail-outline',
    content: 'You will be notified when customer order any product',
    value: true
  },
  {
    title: 'Language Change',
    icon: 'custom-translation-outlie',
    content: 'You will be notified when customer order any product',
    value: true
  }
]);
</script>

<template>
  <v-card class="bg-surface" variant="outlined" rounded="lg">
    <v-card-text>
      <h5 class="text-subtitle-1 mb-0">Settings</h5>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-item>
      <v-list class="border-0" lines="two" border aria-label="setting list" aria-busy="true">
        <v-list-item v-for="(item, index) in items" :key="index" class="py-6">
          <template v-slot:prepend>
            <SvgSprite :name="item.icon || ''" class="me-4 text-primary" style="width: 24px; height: 24px" />
          </template>
          <v-list-item-title class="text-h5">{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle class="text-body-2 text-lightText" style="opacity: 1">{{ item.content }}</v-list-item-subtitle>
          <template v-slot:append>
            <v-switch
              color="primary"
              density="compact"
              aria-label="switch"
              class="ms-3"
              :model-value="item.value"
              inset
              hide-details
            ></v-switch>
          </template>
        </v-list-item>
      </v-list>
      <div class="text-end mt-3">
        <v-btn variant="outlined" color="secondary" rounded="md">Cancel</v-btn>
        <v-btn variant="flat" color="primary" rounded="md" class="ms-3">Save</v-btn>
      </div>
    </v-card-item>
  </v-card>
</template>
