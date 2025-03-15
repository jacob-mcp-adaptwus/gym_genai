<script setup lang="ts">
import { shallowRef } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import CardHeader from '@/components/shared/CardHeader.vue';

const notifications = shallowRef([
  {
    icon: 'custom-document-2',
    color: 'success',
    title: 'Johnny sent you an invoice billed',
    time: '2 August',
    link: '$1,000.'
  },
  {
    icon: 'custom-document-text-outline',
    color: 'primary',
    title: 'Sent an invoice to Aida Bugg amount of',
    time: '7 hours ago',
    link: '$200.'
  },
  {
    icon: 'custom-setup-outline',
    color: 'error',
    title: 'There was a failure to your setup',
    time: '7 hours ago'
  },
  {
    color: 'primary',
    title: 'Cristina danny invited to you join Meeting',
    time: '7 hours ago'
  },
  {
    color: 'primary',
    title: 'Cristina danny invited to you join Meeting',
    time: '7 hours ago'
  }
]);
</script>

<template>
  <CardHeader title="Notification" class="overflow-hidden">
    <template v-slot:header>
      <v-btn variant="text" aria-label="menu" color="secondary" icon rounded="md" size="small">
        <SvgSprite name="custom-more-outline" style="width: 20px; height: 20px" />
      </v-btn>
    </template>
    <v-list class="py-2" lines="two" aria-label="user list" aria-busy="true">
      <v-list-item v-for="(item, i) in notifications" :key="i" rounded="md" class="px-6">
        <template v-slot:prepend>
          <div class="me-3">
            <v-avatar size="40" class="py-2" :color="item.color" variant="tonal">
              <SvgSprite v-if="item.icon" :name="item.icon || ''" style="width: 20px; height: 20px" />
              <span v-else class="text-h5 font-weight-regular">C</span>
            </v-avatar>
          </div>
        </template>
        <div class="d-inline-flex align-center justify-space-between w-100">
          <h6 class="text-subtitle-1 mb-0">
            {{ item.title }}
            <router-link to="/widget/data" class="text-primary link-hover" v-if="item.link">{{ item.link }}</router-link>
          </h6>
          <span class="text-caption d-flex align-center">
            <SvgSprite name="custom-link1" class="ms-1 text-lightText" style="width: 18px; height: 18px" />
          </span>
        </div>

        <p class="text-caption text-lightText mb-0">{{ item.time }}</p>
      </v-list-item>
    </v-list>
    <v-card-item class="pt-0">
      <v-btn variant="outlined" color="secondary" rounded="md" block>View all</v-btn>
    </v-card-item>
  </CardHeader>
</template>
