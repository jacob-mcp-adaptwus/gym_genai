<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useUserCardStore } from '@/stores/apps/UserCard';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

const store = useUserCardStore();

onMounted(() => {
  store.fetchCards();
});

type Card = {
  name: string;
  avatar: string;
  role: string;
  about: string;
  email: string;
  contact: number;
  location: string;
  // Add other properties as needed
};
const cards = computed<Card[]>(() => {
  return store.cards;
});
// theme breadcrumb
const page = ref({ title: 'Style 01' });
const breadcrumbs = ref([
  {
    title: 'Users',
    disabled: false,
    href: '#'
  },
  {
    title: 'Cards',
    disabled: false,
    href: '#'
  },
  {
    title: 'Style 01',
    disabled: true,
    href: '#'
  }
]);
// dropdown data
const actionDD = ref([{ title: 'Edit' }, { title: 'Delete' }]);

const page1 = ref(1);
const rows = ref([{ title: '10 Rows' }, { title: '20 Rows' }, { title: '30 Rows' }]);
const searchValue = ref('');

const filteredCards = computed<Card[]>(() => {
  return cards.value.filter((card) => {
    return card.name.toLowerCase().includes(searchValue.value.toLowerCase());
  });
});
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row class="justify-content-end">
    <v-col cols="12">
      <UiParentCard title="Cards">
        <template v-slot:action>
          <v-row class="justify-end">
            <v-col cols="12" md="3" sm="5">
              <v-text-field
                color="primary"
                hide-details
                width="200"
                class="mt-sm-0 mt-2 w-100"
                single-line
                density="comfortable"
                variant="outlined"
                persistent-placeholder
                placeholder="Search"
                v-model="searchValue"
              >
                <template v-slot:prepend-inner>
                  <SvgSprite name="custom-search" class="text-lightText" style="width: 16px; height: 16px" />
                </template>
              </v-text-field>
            </v-col>
          </v-row>
        </template>

        <v-row>
          <v-col cols="12" md="4" xl="3" sm="6" v-for="(card, i) in filteredCards" :key="i">
            <v-card variant="outlined" rounded="lg" class="card-hover-border bg-containerBg">
              <v-card-text>
                <div class="d-flex align-start">
                  <img :src="card.avatar" :alt="card.avatar" width="72" class="rounded-md" />
                  <div class="ms-auto">
                    <v-menu rounded="md">
                      <template v-slot:activator="{ props }">
                        <v-btn size="x-small" aria-label="menu" v-bind="props" variant="text">
                          <SvgSprite name="custom-more-outline" style="width: 16px; height: 16px" />
                        </v-btn>
                      </template>
                      <v-list elevation="24" aria-label="menu" aria-busy="true" rounded="md" density="compact" class="py-0">
                        <v-list-item v-for="(item, index) in actionDD" :key="index" :value="index" color="secondary">
                          <v-list-item-title class="text-h6">{{ item.title }}</v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </v-menu>
                  </div>
                </div>
                <div class="mb-4 mt-5">
                  <h4 class="text-md-h4 text-h5 mb-0">{{ card.name }}</h4>
                  <span class="text-subtitle-2 text-disabled font-weight-medium">{{ card.role }}</span>

                  <p class="text-subtitle-2 mt-4 mb-4">
                    {{ card.about }}
                  </p>

                  <span class="text-subtitle-2 text-disabled font-weight-medium">Email</span>
                  <p class="text-subtitle-2 font-weight-medium">
                    {{ card.email }}
                  </p>
                  <v-row class="mt-3">
                    <v-col cols="6">
                      <span class="text-subtitle-2 text-disabled font-weight-medium">Phone</span>
                      <p class="text-subtitle-2 font-weight-medium">
                        {{ card.contact }}
                      </p>
                    </v-col>
                    <v-col cols="6">
                      <span class="text-subtitle-2 text-disabled font-weight-medium">Location</span>
                      <p class="text-subtitle-2 font-weight-medium">
                        {{ card.location }}
                      </p>
                    </v-col>
                  </v-row>
                </div>
                <div class="d-flex ga-4 flex-wrap mt-5">
                  <v-btn variant="outlined" color="primary" rounded="md" class="flex-fill">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-message-outline" style="width: 16px; height: 16px" />
                    </template>
                    Message
                  </v-btn>
                  <v-btn variant="outlined" color="error" rounded="md" class="flex-fill">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-slash-outline" style="width: 16px; height: 16px" />
                    </template>
                    Block
                  </v-btn>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row class="justify-space-between mt-5">
          <v-col cols="12" lg="5" class="text-left">
            <v-pagination density="compact" class="left-pagination" v-model="page1" active-color="primary" :length="6"> </v-pagination>
          </v-col>
          <v-col cols="12" lg="5" class="text-end">
            <v-menu transition="scale-transition">
              <template v-slot:activator="{ props }">
                <v-btn color="inherit" rounded="md" variant="text" v-bind="props">
                  10 Rows
                  <template v-slot:append>
                    <SvgSprite name="custom-chevron-outline" style="width: 16px; height: 16px; transform: rotate(90deg)" />
                  </template>
                </v-btn>
              </template>

              <v-list>
                <v-list-item v-for="(row, i) in rows" :key="i" :value="i">
                  <v-list-item-title>{{ row.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-col>
        </v-row>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
<style>
.left-pagination .v-pagination__list {
  justify-content: start;
}
</style>
