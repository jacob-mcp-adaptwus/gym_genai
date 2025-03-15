<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useIspValue } from '@/utils/useIspValue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
// assets
// import imageDemo1 from '@/assets/images/landing/feature-figma.png';
import imageDemo2 from '@/assets/images/landing/feature-components.png';
import imageDemo3 from '@/assets/images/landing/feature-documentation.png';

const relativeURL = ref<string | null>(null);
const { ispValue } = useIspValue();

onMounted(async () => {
  try {
    relativeURL.value = await import.meta.env.BASE_URL;
  } catch (error) {
    console.error('Error url not found:', error);
  }
});
</script>

<template>
  <div class="spacer pt-0">
    <v-container class="maxWidth py-0">
      <v-row class="justify-center">
        <v-col md="6" cols="12">
          <div class="text-center">
            <h2 class="text-h2 mb-sm-4 mb-2">Complete Combo</h2>
            <p class="text-h6 mb-0">
              Able Pro caters to the needs of both developers and designers, whether they are beginners or experts.
            </p>
          </div>
        </v-col>
        <v-col md="12" cols="12" class="pa-sm-3 pa-0"></v-col>
        <!-- <v-col md="4" sm="6" cols="12" data-aos="fade-up" data-aos-duration="800">
          <v-card variant="outlined" class="bg-surface overflow-hidden">
            <v-card-item>
              <h5 class="text-h5">Figma Design System</h5>
              <p class="mb-6 text-h6">Check the live preview of Able Pro Figma design file. Figma file included in all licenses.</p>
              <v-img cover height="250" class="rounded-md" :src="imageDemo1"></v-img>
              <v-btn
                color="secondary"
                size="large"
                class="mt-7"
                variant="tonal"
                rounded="md"
                target="_"
                href="https://www.figma.com/file/6XqmRhRmkr33w0EFD49acY/Able-Pro--v9.0-Figma-Preview?type=design&node-id=46-226114&mode=design&t=RPyhUJgBhofKcwRI-0"
              >
                <template v-slot:prepend>
                  <SvgSprite name="custom-link2" style="width: 20px; height: 20px" />
                </template>
                Reference
              </v-btn>
            </v-card-item>
          </v-card>
        </v-col> -->
        <v-col md="5" sm="6" cols="12" data-aos="fade-up" data-aos-duration="800">
          <v-card variant="outlined" class="bg-surface overflow-hidden h-100">
            <v-card-item>
              <h5 class="text-h5">Explore Components</h5>
              <p class="mb-6 text-h6">Access all components of Able Pro in one place to make your development work easier.</p>
              <v-img cover height="250" class="rounded-md" :src="imageDemo2"></v-img>
              <v-btn
                color="secondary"
                size="large"
                class="mt-7"
                variant="tonal"
                rounded="md"
                target="_"
                :href="ispValue ? `${relativeURL}components/buttons?isp=1` : `${relativeURL}components/buttons`"
              >
                <template v-slot:prepend>
                  <SvgSprite name="custom-link2" style="width: 20px; height: 20px" />
                </template>
                Reference
              </v-btn>
            </v-card-item>
          </v-card>
        </v-col>
        <v-col md="5" sm="6" cols="12" data-aos="fade-up" data-aos-duration="800">
          <v-card variant="outlined" class="bg-surface overflow-hidden h-100">
            <v-card-item class="pa-5 pb-7">
              <h5 class="text-h5">Documentation</h5>
              <p class="mb-6 text-h6">Find solutions and navigate through our helper guide with ease.</p>
              <v-img cover height="250" class="rounded-md" :src="imageDemo3"></v-img>
              <v-btn
                color="secondary"
                size="large"
                class="mt-7"
                variant="tonal"
                rounded="md"
                target="_"
                href="https://phoenixcoded.gitbook.io/able-pro"
              >
                <template v-slot:prepend>
                  <SvgSprite name="custom-link2" style="width: 20px; height: 20px" />
                </template>
                Reference
              </v-btn>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
