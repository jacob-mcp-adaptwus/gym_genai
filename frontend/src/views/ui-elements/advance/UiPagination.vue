<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Pagination' });
const subContent = ref({ content: 'The Pagination component enables the user to select a specific page from a range of pages.' });
const path = ref({ filepath: 'src/views/ui-elements/advance/pagination' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/paginations/' });

// pagination data
const pagination = ref(1);
const pagination2 = ref(1);
const pagination3 = ref(1);
const pagination4 = ref(1);
const pagination5 = ref(2);
const pagination6 = ref(1);
const pagination7 = ref(3);
const pagination8 = ref(6);
const pagination11 = ref(2);
const pagination12 = ref(3);
const pagination13 = ref(4);
const pagination14 = ref(2);
const pagination15 = ref(3);
const pagination16 = ref(6);
const pagination17 = ref(6);
const pagination18 = ref(6);
const pagination19 = ref(6);
const pagination20 = ref(6);
const pagination21 = ref(3);
const pagination22 = ref(2);
const pagination23 = ref(2);
const pagination24 = ref(3);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" lg="6">
          <v-row>
            <v-col cols="12">
              <UiParentCard title="Basic">
                <div>
                  <v-pagination density="compact" v-model="pagination" :length="6"></v-pagination>
                  <v-pagination density="compact" variant="flat" active-color="primary" v-model="pagination11" :length="6"></v-pagination>
                  <v-pagination
                    density="compact"
                    variant="outlined"
                    active-color="secondary"
                    v-model="pagination12"
                    :length="6"
                  ></v-pagination>
                  <v-pagination density="compact" disabled active-color="primary" v-model="pagination13" :length="6"> </v-pagination>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Size -->
            <v-col cols="12">
              <UiParentCard title="Size">
                <div class="text-center">
                  <v-pagination active-color="primary" density="compact" v-model="pagination6" :length="6"></v-pagination>
                  <v-pagination
                    active-color="primary"
                    variant="outlined"
                    density="comfortable"
                    v-model="pagination21"
                    :length="6"
                  ></v-pagination>
                  <v-pagination active-color="secondary" variant="flat" v-model="pagination22" :length="6"></v-pagination>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Ranges -->
            <v-col cols="12">
              <UiParentCard title="Ranges">
                <v-pagination density="compact" v-model="pagination4" :length="15"></v-pagination>
                <v-pagination density="compact" variant="flat" active-color="primary" v-model="pagination5" :length="15"></v-pagination>
                <v-pagination
                  density="compact"
                  variant="outlined"
                  active-color="secondary"
                  v-model="pagination7"
                  :length="15"
                ></v-pagination>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="12" lg="6">
          <v-row>
            <!-- variant -->
            <v-col cols="12">
              <UiParentCard title="Variants">
                <div class="text-center">
                  <v-pagination density="compact" v-model="pagination2" active-color="primary" :length="6"></v-pagination>
                  <v-pagination
                    density="compact"
                    variant="outlined"
                    active-color="primary"
                    v-model="pagination14"
                    :length="6"
                  ></v-pagination>
                  <v-pagination density="compact" variant="flat" active-color="primary" v-model="pagination15" :length="6"></v-pagination>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Rounded -->
            <v-col cols="12">
              <UiParentCard title="Circular">
                <div class="text-center">
                  <v-pagination rounded="circle" density="compact" v-model="pagination3" :length="6"></v-pagination>
                  <v-pagination
                    rounded="circle"
                    density="compact"
                    variant="outlined"
                    active-color="primary"
                    v-model="pagination23"
                    :length="6"
                  >
                  </v-pagination>
                  <v-pagination
                    rounded="circle"
                    density="compact"
                    variant="flat"
                    active-color="primary"
                    v-model="pagination24"
                    :length="6"
                  ></v-pagination>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Colors -->
            <v-col cols="12">
              <UiParentCard title="Colors">
                <div class="text-center">
                  <v-pagination density="compact" v-model="pagination8" :length="10"></v-pagination>
                  <v-pagination density="compact" variant="outlined" active-color="secondary" v-model="pagination16" :length="10">
                  </v-pagination>
                  <v-pagination density="compact" variant="flat" active-color="success" v-model="pagination17" :length="10"></v-pagination>
                  <v-pagination density="compact" variant="flat" active-color="warning" v-model="pagination18" :length="10"> </v-pagination>
                  <v-pagination density="compact" rounded="circle" active-color="info" v-model="pagination19" :length="10"> </v-pagination>
                  <v-pagination density="compact" rounded="circle" variant="flat" active-color="error" v-model="pagination20" :length="10">
                  </v-pagination>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
