<script setup lang="ts">
import SvgSprite from '@/components/shared/SvgSprite.vue';
</script>
<template>
  <v-card variant="flat" class="recievable-card" rounded="lg">
    <v-card-item>
      <div class="d-flex align-end">
        <div class="d-flex">
          <v-avatar size="40" variant="tonal" color="surface" style="--v-activated-opacity: 0.05" rounded="md">
            <SvgSprite name="custom-user-right-outline" style="width: 20px; height: 20px" />
          </v-avatar>
          <div class="text-surface ms-2">
            <p class="text-h6 mb-0">
              Total Recievables
              <SvgSprite name="custom-info-circle-outline" style="width: 16px; height: 16px" />
            </p>
            <div class="d-flex align-center">
              <p class="text-caption mb-0">Current</p>
              <p class="text-h6 ms-2 mb-0">109.1k</p>
            </div>
          </div>
        </div>
        <div class="d-flex text-surface ms-auto align-center">
          <p class="text-caption mb-0">Overdue</p>
          <p class="text-h6 ms-2 mb-0">62k</p>
        </div>
      </div>
      <h4 class="text-h4 text-surface mt-3 mb-0">$43,078</h4>
      <div class="d-flex align-center">
        <v-progress-linear
          aria-label="progressbar"
          color="warning"
          model-value="90"
          bg-opacity="0.9"
          bg-color="lightwarning"
          height="6"
          rounded
        ></v-progress-linear>
        <span class="text-caption text-surface ms-2 d-block">90%</span>
      </div>
    </v-card-item>
  </v-card>
</template>
<style lang="scss">
.recievable-card {
  background: var(--v-gradient);
}
</style>
