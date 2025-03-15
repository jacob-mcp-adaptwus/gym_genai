<script setup lang="ts">
import { ref } from 'vue';
// assets
import imageCard from '@/assets/images/component/card-media.png';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Card' });
const subContent = ref({ content: 'Cards contain content and actions about a single subject.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/cards' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/cards/' });

// tabs data
const tab = ref(null);
const tab1 = ref(null);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <v-row>
              <v-col cols="12" sm="6">
                <v-card class="card-shadow pa-5 h-100">
                  <h6 class="text-h6 pa-0 mb-0">Card Subtitle</h6>
                  <v-card-subtitle class="px-0">This is card description</v-card-subtitle>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card class="card-shadow">
                  <div class="card-header pa-5">
                    <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                  </div>
                  <v-divider></v-divider>
                  <div class="pa-5">
                    <h6 class="text-h6 pa-0 mb-0">Card Subtitle</h6>
                    <v-card-subtitle class="px-0">This is card description</v-card-subtitle>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="Outlined">
            <v-row>
              <v-col cols="12" sm="6">
                <v-card class="pa-5 h-100" variant="outlined">
                  <h6 class="text-h6 pa-0 mb-0">Card Subtitle</h6>
                  <v-card-subtitle class="px-0">This is card description</v-card-subtitle>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card variant="outlined">
                  <div class="card-header pa-5">
                    <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                  </div>
                  <v-divider></v-divider>
                  <div class="pa-5">
                    <h6 class="text-h6 pa-0 mb-0">Card Subtitle</h6>
                    <v-card-subtitle class="px-0">This is card description</v-card-subtitle>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="Actions">
            <v-row>
              <v-col cols="12">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="primary" variant="text">More</v-btn>
                    </div>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim.</p>
                  </v-card-item>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="secondary" aria-label="menu" variant="text" icon rounded="md" size="small">
                        <SvgSprite name="custom-more-outline" style="width: 16px; height: 16px" />
                      </v-btn>
                    </div>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper
                      ligula. Mauris purus sem.
                    </p>
                  </v-card-item>
                </v-card>
              </v-col>
              <v-col cols="12" sm="6">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="secondary" aria-label="menu" variant="text" icon rounded="md" size="small">
                        <SvgSprite name="custom-more-outline" style="width: 16px; height: 16px" />
                      </v-btn>
                    </div>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-actions class="pa-2">
                    <v-btn class="flex-grow-1" aria-label="setting" icon rounded>
                      <SvgSprite name="custom-setting-outline-2" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ms-0" aria-label="edit" icon rounded>
                      <SvgSprite name="custom-edit-outline" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ms-0" aria-label="menu" icon rounded>
                      <SvgSprite
                        name="custom-more-outline"
                        class="text-lightText"
                        style="width: 16px; height: 16px; transform: rotate(90deg)"
                      />
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <UiParentCard title="Complex Interaction">
            <v-row>
              <v-col cols="12">
                <v-card variant="outlined">
                  <v-tabs v-model="tab" color="primary">
                    <v-tab value="one">Article</v-tab>
                    <v-tab value="two">App</v-tab>
                    <v-tab value="three">Project</v-tab>
                  </v-tabs>
                  <v-divider></v-divider>
                  <v-card-text>
                    <v-window v-model="tab">
                      <v-window-item value="one">
                        <h5 class="text-h5 text-lightText">Article Content</h5>
                        <p>
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper
                          ligula. Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                        </p>
                        <p class="mb-0">Suspendisse sed lectus ac nunc rhoncus scelerisque.</p>
                      </v-window-item>

                      <v-window-item value="two">
                        <h5 class="text-h5 text-lightText">App Content</h5>
                        <p class="mb-0">
                          Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non
                          mattis. Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                        </p>
                      </v-window-item>

                      <v-window-item value="three">
                        <h5 class="text-h5 text-lightText">Project Content</h5>
                        <p class="mb-0">
                          Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu
                          ligula placerat cursus in nec est.
                        </p>
                      </v-window-item>
                    </v-window>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="primary" variant="text">More</v-btn>
                    </div>
                  </v-card-item>
                  <v-tabs v-model="tab1" color="primary">
                    <v-tab value="one">Article</v-tab>
                    <v-tab value="two">App</v-tab>
                    <v-tab value="three">Project</v-tab>
                  </v-tabs>
                  <v-divider></v-divider>
                  <v-card-text>
                    <v-window v-model="tab1">
                      <v-window-item value="one">
                        <h5 class="text-h5 text-lightText">Article Content</h5>
                        <p class="mb-0">
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu, semper
                          ligula. Mauris purus sem, sagittis eu mauris et, viverra lobortis urna.
                        </p>
                      </v-window-item>

                      <v-window-item value="two">
                        <h5 class="text-h5 text-lightText">App Content</h5>
                        <p class="mb-0">
                          Suspendisse sed lectus ac nunc rhoncus scelerisque. Integer vitae fringilla leo. Aliquam tincidunt et turpis non
                          mattis. Ut sed semper orci, sed facilisis mauris. Suspendisse blandit velit sit amet velit porta aliquet.
                        </p>
                      </v-window-item>

                      <v-window-item value="three">
                        <h5 class="text-h5 text-lightText">Project Content</h5>
                        <p class="mb-0">
                          Nam egestas sollicitudin nisl, sit amet aliquam risus pharetra ac. Donec ac lacinia orci. Phasellus ut enim eu
                          ligula placerat cursus in nec est.
                        </p>
                      </v-window-item>
                    </v-window>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <v-col cols="12" lg="9">
          <UiParentCard title="Media">
            <v-row>
              <v-col cols="12" md="4" sm="6">
                <v-card variant="outlined">
                  <v-img cover height="250" alt="card image" :src="imageCard"></v-img>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu.
                    </p>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-actions class="pa-2">
                    <v-btn class="flex-grow-1" aria-label="setting" icon rounded>
                      <SvgSprite name="custom-setting-outline-2" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ml-0" aria-label="edit" icon rounded>
                      <SvgSprite name="custom-edit-outline" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ml-0" aria-label="menu" icon rounded>
                      <SvgSprite
                        name="custom-more-outline"
                        class="text-lightText"
                        style="width: 16px; height: 16px; transform: rotate(90deg)"
                      />
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
              <v-col cols="12" md="4" sm="6">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="secondary" aria-label="menu" variant="text" icon rounded="md" size="small">
                        <SvgSprite name="custom-more-outline" style="width: 16px; height: 16px" />
                      </v-btn>
                    </div>
                  </v-card-item>
                  <v-img cover height="250" alt="card image" :src="imageCard"></v-img>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non libero dignissim, viverra augue eu,
                    </p>
                  </v-card-item>
                </v-card>
              </v-col>
              <v-col cols="12" md="4" sm="6">
                <v-card variant="outlined">
                  <v-card-item class="pa-5">
                    <div class="d-flex align-center justify-space-between">
                      <v-card-title class="text-h6 pa-0">Card Title</v-card-title>
                      <v-btn color="secondary" aria-label="menu" variant="text" icon rounded="md" size="small">
                        <SvgSprite name="custom-more-outline" style="width: 16px; height: 16px" />
                      </v-btn>
                    </div>
                  </v-card-item>
                  <v-img cover height="250" alt="card image" :src="imageCard"></v-img>
                  <v-card-item class="pa-5">
                    <v-card-subtitle class="text-h5 pb-3">Card Subtitle</v-card-subtitle>
                    <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                  </v-card-item>
                  <v-divider></v-divider>
                  <v-card-actions class="pa-2">
                    <v-btn class="flex-grow-1" aria-label="setting" icon rounded>
                      <SvgSprite name="custom-setting-outline-2" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ml-0" aria-label="edit" icon rounded>
                      <SvgSprite name="custom-edit-outline" class="text-lightText" style="width: 16px; height: 16px" />
                    </v-btn>
                    <v-divider vertical />
                    <v-btn class="flex-grow-1 ml-0" aria-label="menu" icon rounded>
                      <SvgSprite
                        name="custom-more-outline"
                        class="text-lightText"
                        style="width: 16px; height: 16px; transform: rotate(90deg)"
                      />
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
