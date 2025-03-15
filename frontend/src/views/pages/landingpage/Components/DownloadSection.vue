<script setup lang="ts">
import { useIspValue } from '@/utils/useIspValue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import { useDisplay } from 'vuetify';
const { smAndUp } = useDisplay();

const { ispValue } = useIspValue();
</script>
<template>
  <div class="spacer">
    <v-container class="maxWidth">
      <v-row class="align-center">
        <v-col md="6" cols="12">
          <h2 class="text-h2 text-uppercase"><span class="text-primary">Try </span>Before Buy</h2>
          <p class="text-body-1 mb-0">Download the Free MIT Able Pro Dashboard Template before make your purchase decision.</p>
        </v-col>
        <v-col md="6" cols="12" class="ps-md-12 text-md-end">
          <v-btn
            color="secondary"
            variant="outlined"
            :size="smAndUp ? 'large' : 'default'"
            rounded="md"
            target="_"
            :href="ispValue ? 'https://ableproadmin.com/vue?isp=1' : 'https://ableproadmin.com/vue'"
            >Check Out Pro Version</v-btn
          >
          <v-btn
            color="primary"
            variant="flat"
            :size="smAndUp ? 'large' : 'default'"
            class="ms-3"
            rounded="md"
            target="_"
            href="https://github.com/phoenixcoded/able-pro-free-admin-dashboard-template"
          >
            <template v-slot:prepend>
              <SvgSprite name="custom-link2" style="width: 20px; height: 20px" />
            </template>
            Free (Soon)
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
