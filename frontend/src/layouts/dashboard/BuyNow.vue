<script setup lang="ts">
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useIspValue } from '@/utils/useIspValue';
import { useDisplay } from 'vuetify';

const { xs } = useDisplay();

const { ispValue } = useIspValue();
</script>

<template>
  <!-- <v-btn
    v-if="!xs"
    color="error"
    :href="ispValue ? 'https://1.envato.market/B0JAPW' : 'https://1.envato.market/zNkqj6'"
    target="_"
    variant="flat"
    size="large"
    class="floting-button"
    rounded="pill"
  >
    <template v-slot:prepend>
      <SvgSprite name="custom-shopping-cart" />
    </template>
    Buy now
    <v-tooltip activator="parent" aria-label="tooltip" content-class="smallTooltip" location="top">Buy now</v-tooltip>
  </v-btn> -->
  <!-- <v-btn
    v-if="xs"
    color="error"
    :href="ispValue ? 'https://1.envato.market/B0JAPW' : 'https://1.envato.market/zNkqj6'"
    target="_"
    variant="flat"
    size="large"
    class="floting-button"
    icon
  >
    <SvgSprite name="custom-shopping-cart" />
  </v-btn> -->
</template>

<style lang="scss" scoped>
.floting-button {
  position: fixed;
  bottom: 50px;
  right: 30px;
  opacity: 1;
  transition: all 0.5s ease;
  animation: pulse 2s infinite;
  z-index: 1030;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(var(--v-theme-error), 0.3);
  }

  70% {
    box-shadow: 0 0 0 20px rgba(var(--v-theme-error), 0);
  }

  100% {
    box-shadow: 0 0 0 0 rgba(var(--v-theme-error), 0);
  }
}
</style>
