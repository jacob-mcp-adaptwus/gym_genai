<script setup lang="ts">
import { shallowRef } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const items = shallowRef([
  { text: 'anshan.dh81@gmail.com', icon: 'custom-mail-outline', color: 'dark' },
  { text: '(+1-876) 8654 239 581', icon: 'custom-phone-outline-1', color: 'dark' },
  { text: 'New York', icon: 'custom-goal-outline', color: 'dark' },
  { text: 'https://anshan.dh.url', icon: 'custom-link1', color: 'primary link-hover' }
]);

const details = shallowRef([
  {
    title: 'Full Name',
    subtext: 'Anshan Handgun'
  },
  {
    title: 'Father Name',
    subtext: 'Mr. Deepen Handgun'
  },
  {
    title: 'Phone',
    subtext: '(+1-876) 8654 239 581'
  },
  {
    title: 'Country',
    subtext: 'New York'
  },
  {
    title: 'Email',
    subtext: 'anshan.dh81@gmail.com'
  },
  {
    title: 'Zip Code',
    subtext: '956 754'
  },
  {
    title: 'Address',
    subtext: 'Street 110-B Kalians Bag, Dewan, M.P. New York'
  }
]);

const edus = shallowRef([
  {
    title: 'Master Degree (Year)',
    subtext: '2014-2017'
  },
  {
    title: 'Institute',
    subtext: '-'
  },
  {
    title: 'Bachelor (Year)',
    subtext: '2011-2013'
  },
  {
    title: 'Institute',
    subtext: 'Imperial College London'
  },
  {
    title: 'School (Year)',
    subtext: '2009-2011'
  },
  {
    title: 'Institute',
    subtext: 'School of London, England'
  }
]);

const emps = shallowRef([
  {
    year: 'Senior UI/UX designer (Year)',
    post: '2019-Current',
    title: 'Job Responsibility',
    subtext: 'Perform task related to project manager with the 100+ team under my observation. Team management is key role in this company.'
  },
  {
    year: 'Trainee cum Project Manager (Year)',
    post: '2017-2019',
    title: 'Job Responsibility',
    subtext: 'Team management is key role in this company.'
  }
]);

const skills = shallowRef([
  {
    color: 'primary',
    title: 'Junior',
    value: 30
  },
  {
    color: 'primary',
    title: 'UX Researcher',
    value: 80
  },
  {
    color: 'primary',
    title: 'Wordpress',
    value: 90
  },
  {
    color: 'primary',
    title: 'HTML',
    value: 30
  },
  {
    color: 'primary',
    title: 'Graphic Design',
    value: 95
  },
  {
    color: 'primary',
    title: 'Code style',
    value: 75
  }
]);
</script>

<template>
  <v-row>
    <v-col cols="12" xl="3" md="4">
      <v-card variant="flat" class="overflow-hidden" rounded="lg">
        <v-card variant="outlined" class="overflow-hidden" rounded="lg">
          <v-card-text>
            <div class="text-center pb-4">
              <div class="text-end">
                <v-chip color="primary" size="small" class="mt-2" variant="flat">Pro</v-chip>
              </div>
              <v-avatar size="64" color="lightprimary">
                <img src="@/assets/images/users/vector-1.png" alt="John Doe" width="64" class="v-avatar" />
              </v-avatar>
              <h5 class="text-h5 mt-4 mb-1">Anshan H.</h5>
              <span class="text-h6 text-lightText">Project Manager</span>
            </div>
            <v-divider></v-divider>
            <div class="my-4 d-flex align-center ga-2">
              <div class="text-center w-100">
                <h5 class="text-h5 mb-1">86</h5>
                <span class="text-h6 text-lightText">Post </span>
              </div>
              <v-divider vertical></v-divider>
              <div class="text-center w-100">
                <h5 class="text-h5 mb-1">40</h5>
                <span class="text-h6 text-lightText">Project </span>
              </div>
              <v-divider vertical></v-divider>
              <div class="text-center w-100">
                <h5 class="text-h5 mb-1">4.5K</h5>
                <span class="text-h6 text-lightText">Members </span>
              </div>
            </div>
            <v-divider></v-divider>
            <v-list density="compact" class="pb-0" aria-label="user details" aria-busy="true">
              <template v-for="(item, i) in items" :key="i">
                <v-list-item color="primary" class="py-0 px-0">
                  <template v-slot:prepend>
                    <SvgSprite :name="item.icon || ''" class="text-lightText me-2" style="width: 18px; height: 18px" />
                  </template>

                  <v-list-item-title :class="`text-h6 text-end text-${item.color}`">
                    {{ item.text }}
                  </v-list-item-title>
                </v-list-item>
              </template>
            </v-list>
          </v-card-text>
        </v-card>
      </v-card>
      <v-card variant="outlined" class="mt-6 overflow-hidden" rounded="lg">
        <v-card-text>
          <h5 class="text-subtitle-1 mb-0">Skills</h5>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-item>
          <v-list class="py-0" density="compact" aria-label="skills" aria-busy="true">
            <v-list-item class="pa-0" v-for="(skill, i) in skills" :key="i">
              <div class="d-flex justify-space-between">
                <h5 class="text-h6 mb-0 text-lightText">{{ skill.title }}</h5>
                <div class="flex-1-1">
                  <div class="d-flex align-center justify-end">
                    <v-progress-linear
                      aria-label="progressbar"
                      :bg-color="skill.color"
                      height="6"
                      bg-opacity="0.4"
                      rounded
                      :model-value="skill.value"
                      :color="skill.color"
                      style="min-width: 64px; width: 64px"
                    >
                    </v-progress-linear>
                    <span class="text-caption ms-2 text-lightText">{{ skill.value }}%</span>
                  </div>
                </div>
              </div>
            </v-list-item>
          </v-list>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="12" xl="9" md="8">
      <v-card variant="flat" rounded="lg">
        <v-card variant="outlined" class="overflow-hidden" rounded="lg">
          <v-list aria-label="about list" aria-busy="true">
            <v-list-item>
              <template v-slot:title>
                <h5 class="text-subtitle-1 mb-0">About Me</h5>
              </template>
            </v-list-item>
          </v-list>
          <v-divider></v-divider>
          <v-card-text>
            <p class="text-lightText mb-0">
              Hello,I’m Anshan Handgun Creative Graphic Designer & User Experience Designer based in Website, I create digital Products a
              more Beautiful and usable place. Morbid accusant ipsum. Nam nec tellus at.
            </p>
          </v-card-text>
        </v-card>
      </v-card>

      <v-card variant="outlined" class="mt-6" rounded="lg">
        <div class="px-5 py-6">
          <h5 class="text-subtitle-1 mb-0">Personal Details</h5>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <v-row class="py-2 mx-0 details-content">
            <v-col sm="6" cols="12" class="px-0 pb-0" v-for="(detail, i) in details" :key="i">
              <p class="text-h6 text-lightText mb-1">{{ detail.title }}</p>
              <p class="text-h6 mb-2">{{ detail.subtext }}</p>
              <v-divider></v-divider>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>

      <v-card variant="flat" class="mt-6" rounded="lg">
        <v-card variant="outlined" rounded="lg">
          <div class="px-5 py-6">
            <h5 class="text-subtitle-1 mb-0">Education</h5>
          </div>
          <v-divider></v-divider>
          <v-card-text>
            <v-row class="py-2 mx-0 education-content">
              <v-col sm="6" cols="12" class="px-0 pb-0" v-for="(edu, i) in edus" :key="i">
                <p class="text-h6 text-lightText mb-1">{{ edu.title }}</p>
                <p class="text-h6 mb-2">{{ edu.subtext }}</p>
                <v-divider></v-divider>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>

        <v-card variant="flat" class="mt-6" rounded="lg">
          <v-card variant="outlined" rounded="lg">
            <div class="px-5 py-6">
              <h5 class="text-subtitle-1 mb-0">Employment</h5>
            </div>
            <v-divider></v-divider>
            <v-card-text class="employment-content">
              <v-row class="pt-3" v-for="(emp, i) in emps" :key="i">
                <v-col md="4">
                  <h4 class="text-h6 text-lightText mb-0">{{ emp.year }}</h4>
                  <span class="text-h6">{{ emp.post }}</span>
                </v-col>
                <v-col md="8">
                  <h4 class="text-h6 text-lightText mb-0">{{ emp.title }}</h4>
                  <span class="text-h6">{{ emp.subtext }}</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.link-hover {
  cursor: pointer;
}
.details-content {
  > div {
    &:last-child {
      .v-divider {
        display: none;
      }
    }
  }
}
.education-content {
  > div {
    &:nth-last-child(-n + 2) {
      .v-divider {
        @media (min-width: 600px) {
          display: none;
        }
      }
    }
    &:last-child {
      .v-divider {
        display: none;
      }
    }
  }
}
.employment-content {
  .v-row:not(:last-child) {
    border-bottom: 1px solid rgb(var(--v-theme-borderLight));
  }
}
</style>
