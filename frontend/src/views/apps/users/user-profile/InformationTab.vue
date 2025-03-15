<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

import Flag1 from '@/assets/images/flags/1.jpg';
import Flag2 from '@/assets/images/flags/2.jpg';
import Flag3 from '@/assets/images/flags/3.jpg';
import Flag4 from '@/assets/images/flags/4.jpg';
import Flag5 from '@/assets/images/flags/5.jpg';

const items = ref([
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
]);

const items1 = ref([
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  '10',
  '11',
  '12',
  '13',
  '14',
  '15',
  '16',
  '17',
  '18',
  '19',
  '20',
  '21',
  '22',
  '23',
  '24',
  '25',
  '26',
  '27',
  '28',
  '29',
  '30',
  '31'
]);

const items2 = ref([
  '1990',
  '1991',
  '1992',
  '1993',
  '1994',
  '1995',
  '1996',
  '1997',
  '1998',
  '1999',
  '2000',
  '2001',
  '2002',
  '2003',
  '2004',
  '2005',
  '2006',
  '2007',
  '2008',
  '2009',
  '2010',
  '2011',
  '2012',
  '2013',
  '2014',
  '2015',
  '2016',
  '2017',
  '2018',
  '2019',
  '2020',
  '2021',
  '2022',
  '2023'
]);

const items3 = ref(['+91', '1-671', '+36', '(255)', '+39', '1-876', '+7', '(254)', '(373)', '1-664', '+95', '(264)']);

const country = ref([
  { name: 'Anguilla', avatar: Flag1 },
  { name: 'Brazil', avatar: Flag2 },
  { name: 'Germany', avatar: Flag3 },
  { name: 'United Kingdom', avatar: Flag4 },
  { name: 'United States', avatar: Flag5 }
]);

const countryflag = ref(['United States']);
const isUpdating = ref(false);

const multi_value = ref([
  'Adobe XD',
  'Angular',
  'Corel Draw',
  'Figma',
  'HTML',
  'Illustrator',
  'Javascript',
  'Logo Design',
  'Material UI',
  'NodeJs',
  'npm',
  'Photoshop',
  'React',
  'Reduxjs & tooltit',
  'SASS'
]);
const items4 = ref([
  'Adobe XD',
  'After Effect',
  'Angular',
  'Animation',
  'ASP.net',
  'Bootstrap',
  'C#',
  'CC',
  'Corel Draw',
  'CSS',
  'DIV',
  'Dreamweaver',
  'Figma',
  'Graphics',
  'HTML',
  'Illustrator',
  'J2Ee',
  'Java',
  'Javascript',
  'Jquery',
  'Logo Design',
  'Material UI',
  'Motion',
  'MVC',
  'MySQL',
  'NodeJs',
  'npm',
  'Photoshop',
  'PHP',
  'React',
  'Redux',
  'Reduxjs & tooltit',
  'SASS',
  'SCSS',
  'SQL Server',
  'SVG',
  'UI/UX',
  'User interface designing',
  'Wordpress'
]);
</script>

<template>
  <v-card class="bg-surface" variant="outlined" rounded="lg">
    <v-card-text>
      <h5 class="text-subtitle-1 mb-0">Personal Information</h5>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-item>
      <v-row>
        <v-col cols="12" md="6">
          <v-label class="mb-2">First name</v-label>
          <v-text-field
            density="comfortable"
            single-line
            aria-label="firstname"
            variant="outlined"
            hide-details
            model-value="Stebin"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-label class="mb-2">Last name</v-label>
          <v-text-field
            density="comfortable"
            single-line
            aria-label="lastname"
            variant="outlined"
            hide-details
            model-value="Ben"
          ></v-text-field>
        </v-col>
        <v-col cols="12" xl="6" md="12">
          <v-label class="mb-2">Email Address</v-label>
          <v-text-field
            single-line
            density="comfortable"
            aria-label="email address"
            variant="outlined"
            hide-details
            type="email"
            model-value="stebin.ben@gmail.com"
          ></v-text-field>
        </v-col>
        <v-col cols="12" xl="6" md="12">
          <v-label class="mb-2">Date of Birth (+18)</v-label>
          <v-row>
            <v-col cols="6" sm="4">
              <v-autocomplete
                aria-label="autocomplete"
                modelValue="March"
                :items="items"
                color="primary"
                variant="outlined"
                hide-details
                single-line
                density="comfortable"
              ></v-autocomplete>
            </v-col>
            <v-col cols="6" sm="4">
              <v-autocomplete
                aria-label="autocomplete"
                modelValue="10"
                :items="items1"
                color="primary"
                variant="outlined"
                hide-details
                single-line
                density="comfortable"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" sm="4">
              <v-autocomplete
                aria-label="autocomplete"
                modelValue="1993"
                :items="items2"
                color="primary"
                variant="outlined"
                hide-details
                single-line
                density="comfortable"
              >
              </v-autocomplete>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" xl="6">
          <v-label class="mb-2">Phone Number</v-label>
          <v-row>
            <v-col cols="5" lg="3" md="5" sm="4">
              <v-autocomplete
                aria-label="autocomplete"
                modelValue="+91"
                :items="items3"
                color="primary"
                variant="outlined"
                hide-details
                single-line
                density="comfortable"
              ></v-autocomplete>
            </v-col>
            <v-col cols="7" lg="9" md="7" sm="8">
              <v-text-field
                single-line
                aria-label="phone number"
                variant="outlined"
                type="number"
                hide-details
                density="comfortable"
                model-value="9652364852"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-label class="mb-2">Designation</v-label>
          <v-text-field
            single-line
            density="comfortable"
            aria-label="designation"
            variant="outlined"
            hide-details
            model-value="Full Stack Developer"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-item>
    <v-card-item class="pa-0">
      <h5 class="text-h5 mb-0 pa-5 pb-4">Address</h5>
      <v-divider></v-divider>
      <v-row class="pa-5">
        <v-col cols="12" md="6">
          <v-label class="mb-2">Address 01</v-label>
          <v-textarea
            variant="outlined"
            density="comfortable"
            rows="3"
            hide-details
            aria-label="address"
            model-value="3801 Chalk Butte Rd, Cut Bank, MT 59427, United States"
          ></v-textarea>
        </v-col>
        <v-col cols="12" md="6">
          <v-label class="mb-2">Address 02</v-label>
          <v-textarea
            variant="outlined"
            density="comfortable"
            aria-label="address"
            rows="3"
            hide-details
            model-value="301 Chalk Butte Rd, Cut Bank, NY 96572, New York"
          ></v-textarea>
        </v-col>
        <v-col cols="12" md="6">
          <v-label class="mb-2">Country</v-label>
          <v-autocomplete
            v-model="countryflag"
            :disabled="isUpdating"
            :items="country"
            density="comfortable"
            variant="outlined"
            item-title="name"
            item-value="name"
            hide-details
            label="Select"
            single-line
            color="primary"
            clearable
            aria-label="autocomplete"
            clear-icon="$close"
          >
            <template v-slot:item="{ props, item }">
              <v-list-item v-bind="props" :title="item?.raw?.name">
                <template v-slot:prepend>
                  <v-avatar size="18" rounded="sm">
                    <img :src="item?.raw?.avatar" width="18" alt="flag" />
                  </v-avatar>
                </template>
              </v-list-item>
            </template>
          </v-autocomplete>
        </v-col>
        <v-col cols="12" md="6">
          <v-label class="mb-2">State</v-label>
          <v-text-field
            density="comfortable"
            single-line
            aria-label="state"
            variant="outlined"
            hide-details
            model-value="California"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-item>
    <v-card-item class="pa-0">
      <h5 class="text-h5 mb-0 pa-5 pb-4">Skills</h5>
      <v-divider></v-divider>
      <v-row class="pa-5">
        <v-col cols="12">
          <v-autocomplete
            aria-label="autocomplete"
            density="comfortable"
            v-model="multi_value"
            :items="items4"
            variant="outlined"
            class="skill-field"
            color="primary"
            label="Outlined"
            single-line
            multiple
            hide-details
            closable-chips
            role="combobox"
          >
            <template v-slot:chip>
              <v-chip
                label
                variant="tonal"
                color="lightText"
                size="large"
                rounded="lg"
                style="--v-chip-height: 38px"
                class="my-1 text-subtitle-1 text-dark font-weight-regular"
                border="lightText solid thin opacity-50"
              >
                <template v-slot:close>
                  <SvgSprite name="custom-close" style="width: 20px; height: 20px; transform: rotate(45deg)" />
                </template>
              </v-chip>
            </template>
          </v-autocomplete>
        </v-col>
      </v-row>
    </v-card-item>
    <v-card-item class="pa-0">
      <h5 class="text-h5 mb-0 pa-5 pb-4">Note</h5>
      <v-divider></v-divider>
      <v-row class="pa-5">
        <v-col cols="12">
          <v-textarea
            aria-label="note"
            variant="outlined"
            density="comfortable"
            hide-details
            single-line
            model-value="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
          ></v-textarea>
        </v-col>
        <v-col cols="12" class="text-end">
          <v-btn variant="outlined" color="secondary" rounded="md">Cancel</v-btn>
          <v-btn variant="flat" color="primary" rounded="md" class="ms-2">Save</v-btn>
        </v-col>
      </v-row>
    </v-card-item>
  </v-card>
</template>
<style lang="scss">
.skill-field {
  .v-autocomplete__selection {
    height: 2.2rem;
  }
}
</style>
