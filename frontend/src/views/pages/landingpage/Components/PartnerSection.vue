<script setup lang="ts">
import { ref } from 'vue';
import { useDisplay } from 'vuetify';

// assets
import Partnet1 from '@/assets/images/landing/client-eagames.svg';
import Partnet2 from '@/assets/images/landing/client-vodafone.svg';
import Partnet3 from '@/assets/images/landing/client-crystal-1.svg';
import Partnet4 from '@/assets/images/landing/client-haswent-2.svg';
import Partnet5 from '@/assets/images/landing/client-haxter-3.svg';
import Partnet6 from '@/assets/images/landing/client-montecito-4.svg';
import Partnet7 from '@/assets/images/landing/client-slingshot.svg';
import Partnet8 from '@/assets/images/landing/client-totalstudio-5.svg';

const { lgAndUp } = useDisplay();

const partnerData = ref([Partnet1, Partnet2, Partnet3, Partnet4, Partnet5, Partnet6, Partnet7, Partnet8]);
</script>
<template>
  <div class="spacer">
    <v-container class="py-0">
      <v-row class="justify-center">
        <v-col cols="12">
          <div class="text-center">
            <h2 class="text-h2 mb-sm-4 mb-2">Trusted By</h2>
            <p class="text-h6 mb-0">From Startups to Fortune 500 companies using our Template for their product.</p>
          </div>
        </v-col>
        <v-col md="12" cols="12" class="pa-sm-3 pa-0"></v-col>
        <v-col cols="12">
          <v-row class="justify-center partner-box">
            <v-col
              md="3"
              sm="4"
              cols="6"
              v-for="(item, index) in partnerData"
              :style="lgAndUp ? ' flex: 1 0 18%;max-width: 18%' : ''"
              :key="index"
            >
              <v-img :src="item"></v-img>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<style lang="scss">
.partner-box {
  .v-img {
    filter: grayscale(1);
    opacity: 0.4;
    cursor: pointer;
    transition: 0.5s;
    &:hover {
      opacity: 1;
      transition: 0.5s;
    }
  }
}
</style>
