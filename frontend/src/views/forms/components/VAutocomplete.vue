<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// combo data
const items = ref([
  'The Dark Knight',
  'Control with Control',
  'Combo with Solo',
  'The Dark',
  'Fight Club',
  'demo@company.com',
  'Pulp Fiction'
]);
const items2 = ref([
  'The Dark Knight',
  'Control with Control',
  'Combo with Solo',
  'The Dark',
  'Fight Club',
  'demo@company.com',
  'Pulp Fiction'
]);
const items3 = ref(['The Dark Knight', 'Control with Control', 'City of god', 'The Dark', 'Fight Club', 'Aliens', 'Pulp Fiction']);
const items4 = ref(['The Dark Knight', 'Control with Control', 'City of god', 'The Dark', 'Fight Club', 'Aliens', 'Pulp Fiction']);
const srcs = {
  1: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
  2: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
  3: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
  4: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
  5: 'https://cdn.vuetifyjs.com/images/lists/5.jpg'
};

const people = ref([
  { name: 'Sandra Adams', group: 'Group 1', avatar: srcs[1] },
  { name: 'Ali Connors', group: 'Group 1', avatar: srcs[2] },
  { name: 'Trevor Hansen', group: 'Group 1', avatar: srcs[3] },
  { name: 'Tucker Smith', group: 'Group 1', avatar: srcs[2] },
  { name: 'Britta Holt', group: 'Group 2', avatar: srcs[4] },
  { name: 'Jane Smith ', group: 'Group 2', avatar: srcs[5] },
  { name: 'John Smith', group: 'Group 2', avatar: srcs[1] },
  { name: 'Sandra Williams', group: 'Group 2', avatar: srcs[3] }
]);

const value = ref(['The Dark Knight']);
const value2 = ref(['The Dark']);
const value4 = ref(['Pulp Fiction']);
const cap_value = ref(['demo@company.com']);
const multi_value = ref(['The Dark Knight', 'Fight Club']);
const friends = ref(['Sandra Adams', 'Britta Holt']);
const isUpdating = ref(false);

// component content
const page = ref({ title: 'Autocomplete' });
const subContent = ref({ content: 'The autocomplete is a normal text input enhanced by a panel of suggested options.' });
const path = ref({ filepath: 'src/views/forms/components/autocomplete' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/autocompletes/' });
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Combo Box -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <v-row>
              <v-col lg="6" cols="12">
                <v-autocomplete
                  aria-label="autocomplete"
                  v-model="value"
                  :items="items"
                  color="primary"
                  variant="outlined"
                  hide-details
                  rounded="sm"
                  single-line
                  density="default"
                ></v-autocomplete>
              </v-col>
              <v-col lg="6" cols="12">
                <v-autocomplete
                  aria-label="autocomplete"
                  v-model="cap_value"
                  :items="items"
                  color="primary"
                  label="Email Address"
                  variant="outlined"
                  single-line
                  hide-details
                ></v-autocomplete>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <!-- With Caption -->
        <!-- Combo with Multiple Options -->
        <v-col cols="12" md="6">
          <UiParentCard title="Multiple Tags">
            <v-autocomplete
              aria-label="autocomplete"
              v-model="multi_value"
              :items="items2"
              variant="outlined"
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
                  color="primary"
                  rounded="lg"
                  size="large"
                  class="my-1 py-4 d-flex text-subtitle-1 font-weight-regular"
                  border="primary solid thin opacity-50"
                ></v-chip>
              </template>
            </v-autocomplete>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="With image">
            <v-autocomplete
              aria-label="autocomplete"
              v-model="friends"
              :disabled="isUpdating"
              :items="people"
              chips
              variant="outlined"
              closable-chips
              item-title="name"
              item-value="name"
              hide-details
              label="Select"
              single-line
              multiple
            >
              <template v-slot:chip="{ props, item }">
                <v-chip v-bind="props" class="py-4" :prepend-avatar="item.raw.avatar" :text="item.raw.name"></v-chip>
              </template>

              <template v-slot:item="{ props, item }">
                <v-list-item
                  v-bind="props"
                  :prepend-avatar="item?.raw?.avatar"
                  :title="item?.raw?.name"
                  :subtitle="item?.raw?.group"
                ></v-list-item>
              </template>
            </v-autocomplete>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="With close">
            <v-autocomplete
              clearable
              aria-label="autocomplete"
              clear-icon="$close"
              variant="outlined"
              label="Autocomplete"
              single-line
              color="primary"
              :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
              hide-details
            ></v-autocomplete>
          </UiParentCard>
        </v-col>
        <v-col>
          <UiParentCard title="Density">
            <v-row>
              <v-col md="6" cols="12">
                <v-autocomplete
                  aria-label="autocomplete"
                  v-model="value2"
                  :items="items3"
                  color="primary"
                  variant="outlined"
                  single-line
                  hide-details
                  density="default"
                ></v-autocomplete>
              </v-col>
              <v-col md="6" cols="12">
                <v-autocomplete
                  aria-label="autocomplete"
                  v-model="value4"
                  :items="items4"
                  color="primary"
                  variant="outlined"
                  single-line
                  hide-details
                  density="compact"
                ></v-autocomplete>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
