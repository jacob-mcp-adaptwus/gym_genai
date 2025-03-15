<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Accordion' });
const subContent = ref({ content: 'Lists are continuous, vertical indexes of text or images.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/expansion-panel' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/expansion-panels/' });

const panel = ref([0, 1]);
const panel1 = ref([0]);
const panel2 = ref([0]);
const multiple = ref([0, 1]);
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <v-expansion-panels v-model="panel1">
              <v-expansion-panel v-for="i in 3" :key="i" elevation="0">
                <v-expansion-panel-title color="containerBg"> Accordion 0{{ i }} </v-expansion-panel-title>
                <v-expansion-panel-text>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                  eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                  lobortis eget.
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
        <!-- Disabled -->
        <v-col cols="12" md="6">
          <UiParentCard title="Disabled">
            <v-expansion-panels disabled>
              <v-expansion-panel v-for="i in 3" :key="i" elevation="0">
                <v-expansion-panel-title> Accordion 0{{ i }} </v-expansion-panel-title>
                <v-expansion-panel-text>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                  eget.
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
        <!-- Default Expand -->
        <v-col cols="12" md="6">
          <UiParentCard title="Default Expand">
            <v-expansion-panels v-model="panel">
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 01</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 02</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 03</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
        <!-- Multiple Expand -->
        <v-col cols="12" md="6">
          <UiParentCard title="Multiple Expand">
            <v-expansion-panels v-model="multiple" multiple>
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 01</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 02</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 03</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>

        <!-- Inset -->
        <v-col cols="12" md="6">
          <UiParentCard title="Inset">
            <v-expansion-panels variant="inset">
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 01</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 02</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 03</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
        <!-- Popout -->
        <v-col cols="12" md="6">
          <UiParentCard title="Popout">
            <v-expansion-panels variant="popout">
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 01</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 02</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>

              <v-expansion-panel elevation="0">
                <v-expansion-panel-title color="containerBg">Accordion 03</v-expansion-panel-title>
                <v-expansion-panel-text> Some content </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
        <!-- Customized Icon -->
        <v-col cols="12" md="6">
          <UiParentCard title="Customized Icon">
            <v-expansion-panels v-model="panel2">
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title class="text-primary font-weight-semibold">
                  <SvgSprite name="custom-smile-outline" class="me-2" style="width: 18px; height: 18px" />
                  Accordion 01
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                  <h5 class="mb-2 mt-3 text-h5">Lorem ipsum dolor sit amet,</h5>
                  <p class="pt-3">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                    eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                    lobortis eget.
                  </p>
                  <p class="pt-3">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                    eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                    lobortis eget.
                  </p>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title class="text-error font-weight-semibold">
                  <SvgSprite name="custom-user-outline" class="me-2" style="width: 18px; height: 18px" />
                  Accordion 02
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                    eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                    lobortis eget.
                  </p>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title class="text-secondary font-weight-semibold">
                  <SvgSprite name="custom-clock-outline" class="me-2" style="width: 18px; height: 18px" />
                  Accordion 03
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                    eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                    lobortis eget.
                  </p>
                </v-expansion-panel-text>
              </v-expansion-panel>
              <v-expansion-panel elevation="0">
                <v-expansion-panel-title class="text-info font-weight-semibold">
                  <SvgSprite name="custom-picture-outline" class="me-2" style="width: 18px; height: 18px" />
                  Accordion 03
                </v-expansion-panel-title>
                <v-expansion-panel-text>
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis
                    eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo
                    lobortis eget.
                  </p>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
