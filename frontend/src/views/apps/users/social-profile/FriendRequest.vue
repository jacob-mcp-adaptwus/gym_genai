<script setup lang="ts">
import { ref, onMounted, computed, shallowRef } from 'vue';
import Banner from '../../../../components/apps/socialprofile/BannerSection.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import { useFrinedsStore } from '@/stores/apps/friends';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

const store = useFrinedsStore();

onMounted(() => {
  store.fetchFrineds();
});

type FriendItem = {
  avatar: string;
  name: string;
  mutual: number;
  // Add other properties as needed
};
const getfriends = computed<FriendItem[]>(() => {
  return store.friends;
});

const searchValue = ref('');
// dropdown data
const actionDD = shallowRef([
  { title: 'Favorite', icon: 'custom-heart-outline' },
  { title: 'Edit Friend List', icon: 'custom-multi-users' },
  { title: 'UnFriend', icon: 'custom-trash' }
]);
const page = ref({ title: 'Social Profile' });

const filteredCards = computed<FriendItem[]>(() => {
  return getfriends.value.filter((card) => {
    return card.name.toLowerCase().includes(searchValue.value.toLowerCase());
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
      <UiParentCard title="Friend Request">
        <template v-slot:action>
          <v-row class="justify-end">
            <v-col cols="12" md="3" sm="5">
              <v-text-field
                color="primary"
                hide-details
                width="200"
                variant="outlined"
                density="comfortable"
                persistent-placeholder
                placeholder="Search"
                v-model="searchValue"
                class="mt-sm-0 mt-2 w-100"
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 18px; height: 18px" />
                </template>
              </v-text-field>
            </v-col>
          </v-row>
        </template>

        <v-row>
          <v-col cols="12" xl="3" md="4" sm="6" v-for="(card, i) in filteredCards" :key="i">
            <v-card variant="outlined" rounded="lg" class="card-hover-border bg-containerBg friend-card">
              <v-card-text>
                <div class="d-flex align-center ga-4">
                  <img :src="card.avatar" :alt="card.avatar" width="40" class="rounded-md" />
                  <div class="w-50">
                    <h4 class="text-subttitle-1 text-truncate mb-0">{{ card.name }}</h4>
                    <small class="opacity-50 d-block text-truncate d-flex align-center ga-2 w-50">
                      <span class="text-truncate w-100">{{ card.mutual }} mutual friends</span>
                    </small>
                  </div>
                  <div class="ms-auto">
                    <v-menu rounded="md">
                      <template v-slot:activator="{ props }">
                        <v-btn size="x-small" aria-label="menu" rounded="md" v-bind="props" variant="text">
                          <SvgSprite name="custom-more-outline" class="text-lightText" style="width: 16px; height: 16px" />
                        </v-btn>
                      </template>
                      <v-list elevation="24" rounded="md" aria-label="menu" aria-busy="true" density="compact" class="py-0">
                        <v-list-item v-for="(item, index) in actionDD" :key="index" :value="index" color="secondary">
                          <template v-slot:prepend>
                            <SvgSprite :name="item.icon || ''" class="v-icon--start opacity-50" style="width: 16px; height: 16px" />
                          </template>
                          <v-list-item-title class="text-h6">{{ item.title }}</v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </v-menu>
                  </div>
                </div>
                <v-row class="mt-2">
                  <v-col cols="6">
                    <v-btn variant="outlined" color="primary" block rounded="md"> Confirm </v-btn>
                  </v-col>
                  <v-col cols="6">
                    <v-btn variant="outlined" color="error" block rounded="md"> Delete </v-btn>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
<style lang="scss">
.friend-card {
  .text-truncate {
    white-space: unset !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
}
</style>
