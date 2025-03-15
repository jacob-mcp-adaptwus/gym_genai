<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import Banner from '../../../../components/apps/socialprofile/BannerSection.vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import { useGalleryStore } from '@/stores/apps/gallery';
import UiParentCard from '@/components/shared/UiParentCard.vue';

const store = useGalleryStore();

onMounted(() => {
  store.fetchGallery();
});

type GalleryItem = {
  title: string;
  image: string;
  dateTime: string;
  // Add other properties as needed
};
const getPhotos = computed<GalleryItem[]>(() => {
  return store.gallery;
});

const searchValue = ref('');
// dropdown data
const actionDD = ref([
  { title: 'Remove Tag' },
  { title: 'Download' },
  { title: 'Make Profile Picture' },
  { title: 'Make Cover Photo' },
  { title: 'Find support or Report Photo' }
]);
const page = ref({ title: 'Social Profile' });

const filteredCards = computed<GalleryItem[]>(() => {
  return getPhotos.value.filter((card) => {
    return card.title.toLowerCase().includes(searchValue.value.toLowerCase());
  });
});

const breadcrumbs = ref([
  {
    title: 'Users',
    disabled: false,
    href: '/'
  },
  {
    title: 'Social Profile',
    disabled: true,
    href: '#'
  }
]);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12">
      <Banner />
    </v-col>
  </v-row>
  <v-row class="justify-content-end mt-5">
    <v-col cols="12">
      <UiParentCard title="Gallery">
        <template v-slot:action>
          <v-row class="justify-end">
            <v-col cols="12" md="5" sm="7">
              <div class="d-sm-flex align-center ga-4 mt-4 mt-sm-0">
                <v-text-field
                  color="primary"
                  hide-details
                  width="200"
                  variant="outlined"
                  density="comfortable"
                  persistent-placeholder
                  placeholder="Search"
                  v-model="searchValue"
                >
                  <template v-slot:prepend-inner>
                    <SvgSprite name="custom-search" class="text-lightText" style="width: 18px; height: 18px" />
                  </template>
                </v-text-field>
                <v-btn color="secondary" rounded="md" size="large" variant="flat" class="mt-4 mt-sm-0">Add Photos</v-btn>
              </div>
            </v-col>
          </v-row>
        </template>

        <v-row>
          <v-col cols="12" lg="3" md="4" sm="6" v-for="(card, i) in filteredCards" :key="i">
            <v-card variant="outlined" rounded="lg" class="card-hover-border bg-containerBg overflow-hidden">
              <img :src="card.image" alt="gallery" class="w-100" />
              <v-card-text class="pa-3">
                <div class="d-flex align-center ga-2">
                  <div style="min-width: 140px">
                    <h4 class="text-subtitle-1 mb-1">{{ card.title }}</h4>
                    <small class="opacity-50 d-block text-truncate d-flex align-center ga-2">
                      <SvgSprite name="custom-calendar-outline" class="text-lightText" style="width: 16px; height: 16px" />
                      {{ card.dateTime }}
                    </small>
                  </div>
                  <div class="ms-auto">
                    <v-menu rounded="md">
                      <template v-slot:activator="{ props }">
                        <v-btn size="x-small" aria-label="menu" color="secondary" v-bind="props" icon rounded="md" variant="text">
                          <SvgSprite name="custom-more-outline" class="text-lightText" style="width: 16px; height: 16px" />
                        </v-btn>
                      </template>
                      <v-list elevation="24" aria-label="menu" aria-busy="true" density="compact" rounded="md" class="py-0">
                        <v-list-item v-for="(item, index) in actionDD" :key="index" :value="index" color="secondary">
                          <v-list-item-title class="text-h6">{{ item.title }}</v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </v-menu>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
