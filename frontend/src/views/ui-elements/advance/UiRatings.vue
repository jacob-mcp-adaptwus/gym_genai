<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Rating' });
const subContent = ref({
  content: "Ratings provide insight regarding others' opinions and experiences, and can allow the user to submit a rating of their own."
});
const path = ref({ filepath: 'src/views/ui-elements/advance/ratings' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/ratings/' });

// rating data
const rating = ref(3);
const rating2 = ref(2);
const rating3 = ref(5);
const rating4 = ref(2);
const rating5 = ref(2);
const rating6 = ref(3);
const rating7 = ref(3.5);
const rating9 = ref(4);
const rating10 = ref(4);
const rating11 = ref(3);
const rating12 = ref(3.5);

const rating8 = ref(4.5);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" md="6">
          <v-row>
            <v-col cols="12">
              <UiParentCard title="Basic">
                <v-row class="align-center mb-2 mx-0 mt-0">
                  <v-col sm="3" cols="12" class="pa-0">
                    <h6 class="text-h6 mb-0">Controlled</h6>
                  </v-col>
                  <v-col sm="9" cols="12" class="pa-0">
                    <v-rating v-model="rating" color="inputBorder" active-color="warning" density="compact"></v-rating>
                  </v-col>
                </v-row>
                <v-row class="align-center mb-2 mx-0 mt-0">
                  <v-col sm="3" cols="12" class="pa-0">
                    <h6 class="text-h6 mb-0">Read only</h6>
                  </v-col>
                  <v-col sm="9" cols="12" class="pa-0">
                    <v-rating v-model="rating4" readonly color="inputBorder" active-color="warning" density="compact"></v-rating>
                  </v-col>
                </v-row>
                <v-row class="align-center mx-0 my-0">
                  <v-col sm="3" cols="12" class="pa-0">
                    <h6 class="text-h6 mb-0">Clearable</h6>
                  </v-col>
                  <v-col sm="9" cols="12" class="pa-0">
                    <v-rating v-model="rating3" clearable color="inputBorder" active-color="warning" density="compact"></v-rating>
                  </v-col>
                </v-row>
              </UiParentCard>
            </v-col>
            <!-- Hover -->
            <v-col cols="12">
              <UiParentCard title="Hover">
                <div>
                  <v-rating v-model="rating5" color="warning" hover></v-rating>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Label -->
            <v-col cols="12">
              <UiParentCard title="Label">
                <div>
                  <v-rating
                    v-model="rating6"
                    class="ma-2"
                    :item-labels="['sad', '', '', '', 'happy']"
                    item-label-position="top"
                    color="warning"
                    hover
                  ></v-rating>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Size -->
            <v-col cols="12">
              <UiParentCard title="Size">
                <div>
                  <v-rating
                    class="d-block"
                    v-model="rating2"
                    color="inputBorder"
                    active-color="warning"
                    value="3"
                    size="x-small"
                  ></v-rating>

                  <v-rating class="d-block" v-model="rating9" color="inputBorder" active-color="warning" value="3" size="small"></v-rating>

                  <v-rating class="d-block" v-model="rating10" color="inputBorder" active-color="warning" value="3" size="large"></v-rating>

                  <v-rating
                    class="d-block"
                    v-model="rating11"
                    color="inputBorder"
                    active-color="warning"
                    value="3"
                    size="x-large"
                  ></v-rating>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Icons -->
            <v-col cols="12">
              <UiParentCard title="Customization">
                <div>
                  <v-rating class="d-block" v-model="rating8" color="error" hover>
                    <template v-slot:item="props">
                      <svg :class="'pc-icon ' + (props.isFilled ? 'text-warning me-1' : 'text-lightText me-1')">
                        <use xlink:href="/assets/svg/sprite.svg#custom-smile-outline"></use>
                      </svg>
                    </template>
                  </v-rating>

                  <v-rating
                    class="d-block mt-3"
                    v-model="rating7"
                    color="error"
                    empty-icon="$heartOutline"
                    full-icon="$heart"
                    half-icon="$heartHalf"
                    half-increments
                    hover
                  >
                    <template v-slot:item="props">
                      <svg v-if="props.isFilled" class="pc-icon text-error me-1">
                        <use xlink:href="/assets/svg/sprite.svg#custom-heart-fill"></use>
                      </svg>
                      <svg v-else class="pc-icon text-lightText me-1">
                        <use xlink:href="/assets/svg/sprite.svg#custom-heart-outline"></use>
                      </svg>
                    </template>
                  </v-rating>
                </div>
              </UiParentCard>
            </v-col>
            <v-col cols="12">
              <UiParentCard title="Half increments">
                <div>
                  <v-rating v-model="rating12" hover half-increments color="inputBorder" active-color="warning"></v-rating>
                  <pre class="mb-0 ms-2">{{ rating12 }}</pre>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
