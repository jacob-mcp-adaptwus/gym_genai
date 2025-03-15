<script setup lang="ts">
import { ref } from 'vue';

import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useIspValue } from '@/utils/useIspValue';
import techData from '@/utils/techData';

import Logo from './LogoMain.vue';
import { useDisplay } from 'vuetify';

// types
import type { Technology } from '@/types/tech-types';

const { mdAndUp } = useDisplay();
const drawer = ref(false);
const isMenuOpen = ref(false);

const url = ref<string>(); // Define url as a ref

const { ispValue } = useIspValue();

if (ispValue) {
  url.value = 'https://1.envato.market/B0JAPW';
} else {
  url.value = 'https://1.envato.market/zNkqj6';
}

const getFinalUrl = (item: Technology) => {
  if (item.link !== '#!' && ispValue.value) {
    return `${item.link}?isp=1`;
  }
  return item.link;
};
</script>

<template>
  <v-app-bar elevation="0" flat height="74" class="border-bottom position-fixed" border="0">
    <v-container class="fill-height maxWidth">
      <div class="d-flex align-center ga-2 w-100">
        <div class="d-flex ga-1 align-center">
          <Logo />
          <v-chip rounded="lg" size="small" variant="outlined" color="secondary" class="px-1" style="height: 20px"> v1.0.0 </v-chip>
        </div>
        <!---/Search part -->
        <v-spacer />
        <!-- ---------------------------------------------- -->
        <!---right part -->
        <!-- ---------------------------------------------- -->
        <template v-if="mdAndUp">
          <v-btn variant="text" class="font-weight-medium" :to="ispValue ? '/dashboard/default?isp=1' : '/dashboard/default'" target="_">
            Login
          </v-btn>
          <!-- <v-btn
            icon
            variant="tonal"
            target="_"
            aria-label="github link"
            href="https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template"
          >
            <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
          </v-btn> -->
        </template>
        <template v-else>
          <v-btn variant="text" class="font-weight-medium" :to="ispValue ? '/dashboard/default?isp=1' : '/dashboard/default'" target="_">
            Login
          </v-btn>
          <!-- <v-btn variant="outlined" color="warning" class="font-weight-medium" to="/components/buttons" rounded="md">All Components</v-btn> -->
          <!-- <v-btn icon rounded="sm" variant="text" size="small" @click.stop="drawer = !drawer">
            <SvgSprite name="custom-menu-outline" style="width: 20px; height: 20px" />
          </v-btn> -->
        </template>
      </div>
    </v-container>
  </v-app-bar>

  <!-- <v-navigation-drawer v-model="drawer" temporary location="top" style="height: 310px" floating v-if="!mdAndUp">
    <v-list color="primary">
      <v-list-item :to="ispValue ? '/dashboard/default?isp=1' : '/dashboard/default'">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">Dashboard</v-list-item-title>
      </v-list-item>
      <v-list-item :to="ispValue ? '/components/buttons?isp=1' : '/components/buttons'">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">All Components</v-list-item-title>
      </v-list-item>
      <v-list-item href="https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template" target="_">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">Free version</v-list-item-title>
      </v-list-item>
      <v-list-item href="https://phoenixcoded.gitbook.io/able-pro" target="_">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">Documentation</v-list-item-title>
      </v-list-item>
      <v-list-item class="px-5">
        <v-list-item-title>
          <v-menu v-model="isMenuOpen" :close-on-content-click="false">
            <template #activator="{ props }">
              <v-btn
                variant="text"
                v-bind="props"
                :ripple="false"
                block
                class="preview-btn text-lightText text-h6"
                style="justify-content: flex-start; padding: 0"
              >
                <template #prepend>
                  <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
                </template>
                Live preview
                <SvgSprite
                  name="custom-chevron-down-2"
                  class="ms-1"
                  style="width: 15px; height: 15px; transition: 0.2s"
                  :style="{ transform: isMenuOpen ? 'rotate(-180deg)' : 'rotate(0deg)' }"
                />
              </v-btn>
            </template>
            <v-sheet rounded="md" width="170">
              <perfect-scrollbar style="min-height: 320px; height: 320px">
                <v-list class="py-0" aria-busy="true" aria-label="technology">
                  <v-list-item
                    v-for="(item, index) in techData"
                    :key="index"
                    class="py-sm-3 py-2 px-sm-4 px-3"
                    :href="getFinalUrl(item as Technology)"
                    :target="item.target"
                  >
                    <template #prepend>
                      <v-img
                        :src="item.image"
                        alt="technology"
                        style="width: 30px; height: 30px; min-width: 36px"
                        :style="item.name === 'Live Preview not available' ? 'filter: grayscale(1)' : ''"
                      />
                    </template>
                    {{ item.title }}
                  </v-list-item>
                </v-list>
              </perfect-scrollbar>
            </v-sheet>
          </v-menu>
        </v-list-item-title>
      </v-list-item>
      <v-list-item href="https://phoenixcoded.authordesk.app/" target="_">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">Support</v-list-item-title>
      </v-list-item>
      <v-list-item :href="url" target="_">
        <template v-slot:prepend>
          <SvgSprite name="custom-line" class="text-lightText" style="width: 20px; height: 20px" />
        </template>

        <v-list-item-title class="ms-3 text-lightText text-h6">Purchase Now</v-list-item-title>
        <template v-slot:append>
          <v-chip color="primary" variant="flat" size="small">v1.0</v-chip>
        </template>
      </v-list-item>
    </v-list>
  </v-navigation-drawer> -->
</template>

<style lang="scss">
.preview-btn {
  &:focus-visible {
    > .v-btn__overlay {
      opacity: 0;
    }
  }
  &.v-btn--active > .v-btn__overlay,
  &[aria-haspopup='menu'][aria-expanded='true'] > .v-btn__overlay {
    opacity: 0;
  }
  &:hover > .v-btn__overlay,
  &[aria-haspopup='menu'][aria-expanded='true']:hover > .v-btn__overlay {
    opacity: 0;
  }
}
</style>
