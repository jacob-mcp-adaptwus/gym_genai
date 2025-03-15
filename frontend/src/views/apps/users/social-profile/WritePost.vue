<script setup lang="ts">
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
</script>
<template>
  <v-card variant="outlined" class="bg-surface pa-5" elevation="0" rounded="lg">
    <v-textarea
      variant="outlined"
      single-line
      color="primary"
      density="comfortable"
      name="input-7-4"
      placeholder="Whats on your mind, Larry ?"
      rows="4"
    ></v-textarea>
    <div class="d-flex">
      <v-btn color="secondary" variant="text" rounded="md">
        <template v-slot:prepend>
          <SvgSprite name="custom-paper-clip-2" style="width: 16px; height: 16px" />
        </template>
        Gallery
      </v-btn>
      <v-btn color="secondary" variant="flat" rounded="md" class="ms-auto">
        <template v-slot:prepend>
          <SvgSprite name="custom-copy" style="width: 16px; height: 16px" />
        </template>
        Post
      </v-btn>
    </div>
  </v-card>
</template>
