<script setup lang="ts">
import { shallowRef } from 'vue';

// assets
import Avatar1 from '@/assets/images/users/avatar-6.png';
import Avatar2 from '@/assets/images/users/avatar-1.png';
import Avatar3 from '@/assets/images/users/avatar-2.png';
import Avatar4 from '@/assets/images/users/avatar-3.png';
import Avatar5 from '@/assets/images/users/avatar-4.png';
import Avatar6 from '@/assets/images/users/avatar-5.png';
import Avatar7 from '@/assets/images/users/avatar-7.png';
import Avatar8 from '@/assets/images/users/avatar-8.png';

const marqueeArray = shallowRef([
  { image: Avatar1, text: '“Amazing template for fast develop.💎“', name: 'devbar', designation: 'Customizability' },
  {
    image: Avatar2,
    text: '“Code quality is amazing. Design is astonishing. very easy to customize..😍“',
    name: 'shahabblouch',
    designation: 'Code Quality'
  },
  {
    image: Avatar3,
    text: '“This has been one of my favorite admin dashboards to use. 😍“',
    name: 'htmhell',
    designation: 'Design Quality'
  },
  {
    image: Avatar4,
    text: '“Excellent support, if we need any modification, they are doing immediately“',
    name: 'hemchandkodali',
    designation: 'Customer Support'
  },
  {
    image: Avatar5,
    text: '“For developers like me, this is the total package! 😍 “',
    name: 'sumaranjum',
    designation: 'Feature Availability'
  },
  {
    image: Avatar6,
    text: '“I love the looks of Able Pro 7.0. I really like the colors you guys have chosen for this theme. It looks really nice.. 💎“',
    name: 'ritelogic',
    designation: 'Other'
  },
  {
    image: Avatar7,
    text: '“The author is very nice and solved my problem inmediately 😍 “',
    name: 'richitela',
    designation: 'Customer Support'
  },
  {
    image: Avatar8,
    text: '“Perfect for my need. Elegant look n feel with blazing fast code. 💎“',
    name: 'Genstiade',
    designation: 'Feature Availability'
  }
]);
</script>
<template>
  <v-container class="py-0" fluid style="max-width: 100%">
    <v-row class="justify-center">
      <v-col lg="6" md="8" cols="12">
        <div class="text-center">
          <h2 class="text-h2 mt-0 mb-sm-4 mb-2">They <span class="text-primary">love </span> Able Pro, Now your turn 😍</h2>
          <p class="text-h6 mb-0">
            We take pride in our Dashboard development, which has been consistently rated 4.6/5 by our satisfied customers. It brings us joy
            to share the positive feedback we have received from our loyal clients.
          </p>
        </div>
      </v-col>
      <v-col md="12" cols="12" class="pa-sm-3 pa-0"></v-col>
      <v-col cols="12">
        <div class="mx-n3">
          <Vue3Marquee :pause-on-hover="true" :clone="true" :duration="50">
            <v-card v-for="(item, index) in marqueeArray" :key="index" variant="outlined" class="bg-surface mx-3 my-2 text-h2">
              <v-card-item>
                <div class="d-flex align-center">
                  <v-avatar size="52" variant="flat" color="lightprimary">
                    <img :src="item.image" width="52" alt="Julia" />
                  </v-avatar>
                  <div class="ms-3">
                    <p class="text-body-1 mb-0">{{ item.text }}</p>
                    <p class="text-body-1 mb-0">
                      <small class="me-2">{{ item.name }}- </small>
                      <span>{{ item.designation }}</span>
                    </p>
                  </div>
                </div>
              </v-card-item>
            </v-card>
          </Vue3Marquee>
        </div>
        <div class="mt-4 mx-n3">
          <Vue3Marquee :pause-on-hover="true" :clone="true" :duration="50" :direction="'reverse'">
            <v-card v-for="(item, index) in marqueeArray" :key="index" variant="outlined" class="bg-surface mx-3 my-2 text-h2">
              <v-card-item>
                <div class="d-flex align-center">
                  <v-avatar size="52" variant="flat" color="lightprimary">
                    <img :src="item.image" width="52" alt="Julia" />
                  </v-avatar>
                  <div class="ms-3">
                    <p class="text-body-1 mb-0">{{ item.text }}</p>
                    <p class="text-body-1 mb-0">
                      <small class="me-1">{{ item.name }} -</small>
                      <span>{{ item.designation }}</span>
                    </p>
                  </div>
                </div>
              </v-card-item>
            </v-card>
          </Vue3Marquee>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<style lang="scss">
.vue3-marquee {
  > .marquee {
    .v-card {
      width: 420px;
      @media (max-width: 959px) {
        width: 320px;
      }
    }
  }
}
</style>
