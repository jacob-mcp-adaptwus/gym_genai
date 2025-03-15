<script setup lang="ts">
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useIspValue } from '@/utils/useIspValue';
import techData from '@/utils/techData';

// types
import type { Technology } from '@/types/tech-types';

const { ispValue } = useIspValue();

const getFinalUrl = (item: Technology) => {
  if (item.link !== '#!' && ispValue.value) {
    return `${item.link}?isp=1`;
  }
  return item.link;
};
</script>
<template>
  <!-- <div class="spacer">
    <v-container class="maxWidth py-0">
      <v-row class="justify-center mb-0">
        <v-col md="5" cols="12">
          <div class="text-center">
            <h2 class="text-h2 mb-sm-4 mb-2">Available Technologies</h2>
            <p class="text-h6 mb-0">Explore the Demos of Able Pro in multiple technologies.</p>
          </div>
        </v-col>
        <v-col md="12" cols="12" class="pa-sm-3 pa-0"></v-col>
        <v-col md="12" cols="12" class="pb-0">
          <v-row class="colSpacing justify-center">
            <v-col v-for="(tech, index) in techData" lg="4" md="6" sm="12" cols="12" :key="index">
              <v-card variant="outlined" class="bg-surface h-100">
                <v-card-item>
                  <v-badge v-if="tech.label" color="lighterror" text-color="error" :content="tech.label" offset-x="10" offset-y="5">
                    <v-img :src="tech.image" alt="technology" style="width: 70px" cover></v-img>
                  </v-badge>
                  <v-img v-else :src="tech.image" alt="technology" style="width: 70px" cover></v-img>
                  <h4 class="text-h4 mt-4 mb-4">{{ tech.title }}</h4>
                  <p class="text-h6 mb-4">{{ tech.description }}</p>
                  <v-btn
                    color="secondary"
                    size="large"
                    variant="tonal"
                    rounded="md"
                    :href="getFinalUrl(tech as Technology)"
                    :target="tech.target"
                  >
                    <template v-slot:prepend>
                      <SvgSprite name="custom-link2" style="width: 20px; height: 20px" />
                    </template>
                    Reference
                  </v-btn>
                  <v-btn
                    icon
                    v-if="tech.free"
                    color="containerBg"
                    aria-label="link"
                    variant="flat"
                    class="ms-2"
                    target="_blank"
                    href="https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template"
                  >
                    <SvgSprite name="custom-document-2" style="width: 20px; height: 20px" />
                  </v-btn>
                </v-card-item>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div> -->
</template>
<style lang="scss">
.colSpacing {
  > div {
    padding-inline: 20px;
    @media (max-width: 599px) {
      padding-inline: 10px;
    }
  }
}
</style>
