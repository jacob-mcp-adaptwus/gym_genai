<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiTitleCard from '@/components/shared/UiTitleCard.vue';

// component content
const page = ref({ title: 'Tabs' });
const subContent = ref({ content: 'Tabs make it easy to explore and switch between different views.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/tabs' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/tabs/' });

// tabs data
const tab = ref(null);
const tab2 = ref(0);
const tab3 = ref(null);
const tab5 = ref(null);
const tab7 = ref(null);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" md="6">
          <UiTitleCard title="Basic" class-name="pt-5">
            <v-tabs v-model="tab" color="primary">
              <v-tab value="one" class="font-weight-medium">
                Tab1
                <v-chip color="primary" class="ms-2 font-weight-medium" rounded="lg" size="small"> 99 </v-chip>
              </v-tab>
              <v-tab value="two" class="font-weight-medium">
                Tab2
                <v-chip color="lightText" class="ms-2 font-weight-medium" rounded="lg" size="small"> 9 </v-chip>
              </v-tab>
              <v-tab value="three" class="font-weight-medium">Tab3</v-tab>
            </v-tabs>
            <v-divider></v-divider>
            <v-card-text class="border-0 px-0 pb-0">
              <v-window v-model="tab">
                <v-window-item value="one">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper ligula.
                  Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                </v-window-item>

                <v-window-item value="two">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="three">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>
              </v-window>
            </v-card-text>
          </UiTitleCard>
        </v-col>
        <!-- With Icons -->
        <v-col cols="12" md="6">
          <UiTitleCard title="Color Tab with Disabled Tab + Scrollable Tabs" class-name="pt-5">
            <v-tabs v-model="tab2" color="primary">
              <v-tab value="1" class="font-weight-medium">
                Tab1
                <v-chip color="primary" class="ms-2 font-weight-medium" rounded="lg" size="small"> 99 </v-chip>
              </v-tab>
              <v-tab value="2" class="font-weight-medium" disabled>
                Tab2
                <v-chip color="lightText" class="ms-2 font-weight-medium" rounded="lg" size="small"> 99 </v-chip>
              </v-tab>
              <v-tab value="3" class="font-weight-medium">
                Tab3
                <v-chip color="lightText" class="ms-2 font-weight-medium" rounded="lg" size="small"> 9 </v-chip>
              </v-tab>
              <v-tab value="4" class="font-weight-medium">Tab4</v-tab>
              <v-tab value="5" class="font-weight-medium">Tab5</v-tab>
              <v-tab value="6" class="font-weight-medium">Tab6</v-tab>
              <v-tab value="7" class="font-weight-medium">Tab7</v-tab>
              <v-tab value="8" class="font-weight-medium">Tab8</v-tab>
              <v-tab value="9" class="font-weight-medium">Tab9</v-tab>
            </v-tabs>
            <v-divider></v-divider>
            <v-card-text class="border-0 px-0 pb-0">
              <v-window v-model="tab2">
                <v-window-item value="1">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper ligula.
                  Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                </v-window-item>

                <v-window-item value="2">
                  Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute,
                  non cupidatat skateboard dolor brunch.
                </v-window-item>

                <v-window-item value="3">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="4">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>

                <v-window-item value="5">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper ligula.
                  Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                </v-window-item>

                <v-window-item value="6">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="7">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>

                <v-window-item value="8">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="9">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>
              </v-window>
            </v-card-text>
          </UiTitleCard>
        </v-col>
        <!-- Icons -->
        <v-col cols="12" md="6">
          <UiTitleCard title="Icon tabs" class-name="pt-5">
            <v-tabs v-model="tab3" color="primary">
              <v-tab value="111">
                <SvgSprite name="custom-user-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Profile
              </v-tab>
              <v-tab value="222">
                <SvgSprite name="custom-page-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Followers
              </v-tab>
              <v-tab value="444">
                <SvgSprite name="custom-multi-users" class="v-icon--start" style="width: 18px; height: 18px" /> Friends
              </v-tab>
              <v-tab value="666">
                <SvgSprite name="custom-picture-outline" class="v-icon--start" style="width: 18px; height: 18px" /> Gallery
              </v-tab>
            </v-tabs>
            <v-divider></v-divider>
            <v-card-text class="border-0 px-0 pb-0">
              <v-window v-model="tab3">
                <v-window-item value="111">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper ligula.
                  Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                </v-window-item>

                <v-window-item value="222">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="444">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>

                <v-window-item value="666">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>
              </v-window>
            </v-card-text>
          </UiTitleCard>
        </v-col>

        <!-- Center -->
        <v-col cols="12" md="6">
          <UiTitleCard title="Centered Tabs" class-name="pt-5">
            <v-tabs v-model="tab5" align-tabs="center" color="primary">
              <v-tab value="11111" class="font-weight-medium">
                Tab1
                <v-chip color="primary" class="ms-2 font-weight-medium" rounded="lg" size="small"> 99 </v-chip>
              </v-tab>
              <v-tab value="22222" class="font-weight-medium">
                Tab2
                <v-chip color="lightText" class="ms-2 font-weight-medium" rounded="lg" size="small"> 9 </v-chip>
              </v-tab>
              <v-tab value="44444" class="font-weight-medium">Tab3</v-tab>
            </v-tabs>
            <v-divider></v-divider>
            <v-card-text class="border-0 px-0 pb-0">
              <v-window v-model="tab5">
                <v-window-item value="11111">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper ligula.
                  Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                </v-window-item>

                <v-window-item value="22222">
                  Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non mattis.
                  Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                </v-window-item>

                <v-window-item value="44444">
                  Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu ligula
                  placerat cursus in nec est.
                </v-window-item>
              </v-window>
            </v-card-text>
          </UiTitleCard>
        </v-col>

        <!-- Vertical Tabs -->
        <v-col cols="12" lg="6" md="8">
          <UiTitleCard title="Vertical Tabs" class-name="pt-5">
            <v-row class="d-flex flex-row">
              <v-col cols="12" sm="3">
                <v-tabs
                  v-model="tab7"
                  class="vertical-tab-height"
                  direction="vertical"
                  color="primary"
                  prev-icon="$chevronUp"
                  next-icon="$chevronDown"
                >
                  <v-tab value="option-1" rounded="md" class="justify-center"> Tab 1 </v-tab>
                  <v-tab value="option-2" rounded="md" class="justify-center"> Tab 2 </v-tab>
                  <v-tab value="option-3" rounded="md" class="justify-center"> Tab 3 </v-tab>
                  <v-tab value="option-4" rounded="md" class="justify-center"> Tab 4 </v-tab>
                  <v-tab value="option-5" rounded="md" class="justify-center"> Tab 5 </v-tab>
                  <v-tab value="option-6" rounded="md" class="justify-center"> Tab 6 </v-tab>
                  <v-tab value="option-7" rounded="md" class="justify-center"> Tab 7 </v-tab>
                </v-tabs>
              </v-col>
              <v-col cols="12" sm="9">
                <v-window v-model="tab7">
                  <v-window-item value="option-1">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit. In est quam, mattis non dui sed, pretium dignissim elit.
                          Nam auctor augue et magna rutrum dictum. Nulla facilisi. Sed consectetur libero vitae sem ultrices fermentum.
                          Donec ac tortor ullamcorper, posuere est congue, pharetra velit. Nullam vehicula elit elementum pellentesque
                          elementum. Duis consectetur sapien purus, et scelerisque erat fringilla quis.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-2">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Vestibulum felis felis, venenatis non eleifend nec, eleifend gravida enim. In tristique nunc ut dui sodales
                          dapibus. Aenean consequat eros sed erat sagittis lobortis. Proin turpis leo, pulvinar ac eros feugiat, feugiat
                          varius odio. Nullam quam massa, tempus ac egestas ac, dapibus sed nisl. Vivamus vehicula cursus magna vitae
                          pretium. Nunc dictum elit at felis malesuada, id sollicitudin leo elementum.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-3">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Curabitur vitae condimentum magna. In posuere rhoncus dolor sit amet mattis. Suspendisse ligula enim, varius at
                          consequat aliquam, pharetra ac velit. Morbi a augue vel leo suscipit convallis. Proin semper pretium dolor, ac
                          pharetra diam gravida non. Etiam velit orci, elementum et viverra ornare, vestibulum accumsan dui. Suspendisse
                          sagittis tristique metus non interdum. Nullam mollis sagittis dolor.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-4">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Quisque posuere luctus turpis vel aliquam. Maecenas consequat tempus nisl, ac ultrices lacus laoreet dignissim.
                          Donec pretium quis turpis sed rutrum. Etiam fermentum ipsum vel urna scelerisque vulputate. Phasellus nulla dui,
                          bibendum id ligula et, eleifend efficitur orci. Integer vel purus nec lectus porta interdum. Aliquam finibus
                          lectus id odio dictum, in facilisis quam hendrerit. Ut vitae tellus enim.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-5">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Vestibulum ullamcorper sem ac velit dictum ultricies. Vestibulum orci dolor, laoreet vehicula eleifend et,
                          pharetra eget nulla. Vivamus arcu nisl, tincidunt et turpis semper, ultrices porta neque. Nam vestibulum, sapien
                          sit amet malesuada dignissim, justo nisi dictum nisl, non maximus quam risus vitae nisi. Fusce vitae nisl
                          ultrices, hendrerit libero non, pellentesque ipsum.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-6">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Vestibulum felis felis, venenatis non eleifend nec, eleifend gravida enim. In tristique nunc ut dui sodales
                          dapibus. Aenean consequat eros sed erat sagittis lobortis. Proin turpis leo, pulvinar ac eros feugiat, feugiat
                          varius odio. Nullam quam massa, tempus ac egestas ac, dapibus sed nisl. Vivamus vehicula cursus magna vitae
                          pretium. Nunc dictum elit at felis malesuada, id sollicitudin leo elementum.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                  <v-window-item value="option-7">
                    <v-card variant="text">
                      <v-card-text class="border-0 pa-0">
                        <p class="mb-0">
                          Vestibulum ullamcorper sem ac velit dictum ultricies. Vestibulum orci dolor, laoreet vehicula eleifend et,
                          pharetra eget nulla. Vivamus arcu nisl, tincidunt et turpis semper, ultrices porta neque. Nam vestibulum, sapien
                          sit amet malesuada dignissim, justo nisi dictum nisl, non maximus quam risus vitae nisi. Fusce vitae nisl
                          ultrices, hendrerit libero non, pellentesque ipsum.
                        </p>
                      </v-card-text>
                    </v-card>
                  </v-window-item>
                </v-window>
              </v-col>
            </v-row>
          </UiTitleCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
