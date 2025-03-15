<script setup lang="ts">
import { ref } from 'vue';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Buttons' });
const subContent = ref({ content: 'Buttons allow users to take actions, and make choices, with a single tap.' });
const path = ref({ filepath: 'src/views/forms/components/buttons' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/buttons' });

// buttons color data
const btnsColor = ref(['primary', 'secondary', 'info', 'success', 'warning', 'error']);
const btnsColor1 = ref([
  {
    name: 'primary',
    color: 'darkprimary'
  },
  {
    name: 'secondary',
    color: 'darksecondary'
  },
  {
    name: 'info',
    color: 'darkinfo'
  },
  {
    name: 'success',
    color: 'darksuccess'
  },
  {
    name: 'warning',
    color: 'darkwarning'
  },
  {
    name: 'error',
    color: 'darkerror'
  }
]);

// buttons size data
const btnsSize = ref(['x-small', 'small', 'large', 'x-large']);

// buttons data
const btnsContent = ref(['one', 'two', 'three']);

const loading = ref(false);

function load() {
  loading.value = true;
  setTimeout(() => {
    loading.value = false;
  }, 3000);
}
</script>

// ===============================|| Ui Buttons ||=============================== //
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Base Buttons -->
        <v-col cols="12" md="6">
          <v-row>
            <v-col cols="12">
              <UiParentCard title="Basic Button">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn v-for="btn in btnsColor" rounded="md" :key="btn" :color="btn">
                    {{ btn }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Outlined Buttons -->
            <v-col cols="12">
              <UiParentCard title="Outlined Button">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn v-for="btn in btnsColor" rounded="md" :key="btn" :color="btn" variant="outlined">
                    {{ btn }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Dashed Buttons -->
            <v-col cols="12">
              <UiParentCard title="Dashed Button">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn
                    v-for="btn in btnsColor"
                    rounded="md"
                    :key="btn"
                    :color="btn"
                    :border="`${btn} dashed thin opacity-100`"
                    variant="tonal"
                  >
                    {{ btn }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Flat Buttons -->
            <v-col cols="12">
              <UiParentCard title="Flat Button">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn v-for="btn in btnsColor" :key="btn" :color="btn" variant="flat" rounded="md">
                    {{ btn }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Text Buttons -->
            <v-col cols="12">
              <UiParentCard title="Text Button">
                <div class="d-flex flex-wrap ga-4 my-2 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn v-for="btn in btnsColor" rounded="md" :key="btn" :color="btn" variant="text">
                    {{ btn }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Shadow Button -->
            <v-col cols="12">
              <UiParentCard title="Shadow Button">
                <div class="d-flex flex-wrap ga-4 align-center flex-column flex-sm-row fill-height">
                  <v-btn
                    variant="flat"
                    v-for="btn in btnsColor1"
                    rounded="md"
                    :key="btn.name"
                    :color="btn.color"
                    :class="`${btn.name}-shadow`"
                  >
                    {{ btn.name }}
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- With Icons -->
            <v-col cols="12">
              <UiParentCard title="With Icons">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn flat color="primary" rounded="md">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-home-outline" style="width: 18px; height: 18px" />
                    </template>
                    Home
                  </v-btn>
                  <v-btn flat color="secondary" rounded="md">
                    Profile
                    <template v-slot:append>
                      <SvgSprite name="custom-smile-fill" style="width: 18px; height: 18px" />
                    </template>
                  </v-btn>
                  <v-btn flat color="info" rounded="md" variant="outlined">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-navigation-outline" style="width: 18px; height: 18px" />
                    </template>
                    Address
                  </v-btn>
                  <v-btn flat color="success" rounded="md" variant="outlined">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-circle-plus-outline" style="width: 18px; height: 18px" />
                    </template>
                    Add
                  </v-btn>
                  <v-btn flat color="warning" rounded="md" variant="outlined">
                    Send
                    <template v-slot:append>
                      <SvgSprite name="custom-send-outline" style="width: 18px; height: 18px" />
                    </template>
                  </v-btn>
                  <v-btn flat color="error" rounded="md" variant="text">
                    Cancel
                    <template v-slot:append>
                      <SvgSprite name="custom-close" style="width: 18px; height: 18px; transform: rotate(45deg)" />
                    </template>
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Sizes -->
            <v-col cols="12">
              <UiParentCard title="Button size">
                <div class="d-flex flex-wrap ga-4 align-start flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn v-for="btn in btnsSize" rounded="md" :key="btn" :size="btn" color="primary"> {{ btn }} </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Disabled -->
            <v-col cols="12">
              <UiParentCard title="Disabled Button">
                <div class="d-flex flex-wrap ga-4 align-start flex-wrap flex-row fill-height">
                  <v-btn text="Default" rounded="md" variant="text" disabled></v-btn>
                  <v-btn text="Cotained" rounded="md" variant="tonal" disabled></v-btn>
                  <v-btn text="Outlined" rounded="md" variant="outlined" disabled></v-btn>
                  <v-btn text="Dashed" rounded="md" variant="tonal" border="secondary dashed thin opacity-100" disabled></v-btn>
                  <v-btn icon variant="tonal" aria-label="button" rounded="md" disabled>
                    <SvgSprite name="custom-home-outline" style="width: 20px; height: 20px" />
                  </v-btn>
                  <v-btn icon variant="outlined" aria-label="button" rounded="md" disabled>
                    <SvgSprite name="custom-circle-plus-outline" style="width: 20px; height: 20px" />
                  </v-btn>
                  <v-btn icon border="secondary dashed thin opacity-100" aria-label="button" rounded="md" variant="tonal" disabled>
                    <SvgSprite name="custom-send-outline" style="width: 20px; height: 20px" />
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Block level -->
            <v-col cols="12">
              <UiParentCard title="Block level">
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-btn color="primary" rounded="md" block>Primary</v-btn>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-btn color="secondary" rounded="md" variant="outlined" block>Secondary</v-btn>
                  </v-col>
                </v-row>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Button group -->
            <v-col cols="12">
              <UiParentCard title="Button group">
                <div class="d-flex flex-column ga-4">
                  <v-btn-group divided variant="flat" color="primary" density="compact">
                    <v-btn v-for="btn in btnsContent" :key="btn">{{ btn }}</v-btn>
                  </v-btn-group>
                  <v-btn-group divided variant="outlined" color="primary" density="compact">
                    <v-btn v-for="btn in btnsContent" :key="btn">{{ btn }}</v-btn>
                  </v-btn-group>
                  <v-btn-group divided color="primary" variant="text" density="compact">
                    <v-btn v-for="btn in btnsContent" :key="btn">{{ btn }}</v-btn>
                  </v-btn-group>
                  <v-btn-group divided variant="outlined" color="warning" density="compact">
                    <v-btn v-for="btn in btnsContent" :key="btn">{{ btn }}</v-btn>
                  </v-btn-group>
                </div>
              </UiParentCard>
            </v-col>
            <v-col cols="12">
              <UiParentCard title="Fab">
                <div class="d-flex ga-4 flex-wrap">
                  <v-btn icon size="large" aria-label="button" variant="elevated" color="primary" class="primary-shadow">
                    <SvgSprite name="custom-plus" style="width: 20px; height: 20px" />
                  </v-btn>
                  <v-btn icon size="large" aria-label="button" variant="elevated" color="info" class="info-shadow">
                    <SvgSprite name="custom-edit-outline" style="width: 20px; height: 20px" />
                  </v-btn>
                  <v-btn icon size="large" aria-label="button" variant="elevated" disabled>
                    <SvgSprite name="custom-mic-off" style="width: 20px; height: 20px" />
                  </v-btn>
                  <v-btn size="large" variant="elevated" rounded="pill" color="error" class="error-shadow">Extended</v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <v-col cols="12">
              <h5 class="text-h5 mb-5">Extended Button</h5>
              <!-- Icon button -->
              <UiParentCard title="Icon Button">
                <v-row>
                  <v-col cols="12">
                    <div class="d-flex flex-wrap ga-4">
                      <v-btn color="primary" aria-label="button" variant="flat" icon rounded="md">
                        <SvgSprite name="custom-home-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="secondary" aria-label="button" variant="flat" icon rounded="md">
                        <SvgSprite name="custom-smile-fill" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="info" aria-label="button" icon rounded="md" variant="outlined">
                        <SvgSprite name="custom-navigation-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="success" aria-label="button" icon rounded="md" variant="outlined">
                        <SvgSprite name="custom-circle-plus-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="warning" aria-label="button" icon rounded="md" variant="tonal" border="warning dashed thin opacity-100">
                        <SvgSprite name="custom-send-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="error" aria-label="button" icon rounded="md" variant="text">
                        <SvgSprite name="custom-close" style="width: 20px; height: 20px; transform: rotate(45deg)" />
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="12">
                    <div class="d-flex flex-wrap ga-4">
                      <v-btn color="primary" aria-label="button" icon>
                        <SvgSprite name="custom-home-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="secondary" aria-label="button" icon>
                        <SvgSprite name="custom-smile-fill" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="info" aria-label="button" icon variant="outlined">
                        <SvgSprite name="custom-navigation-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="success" aria-label="button" icon variant="outlined">
                        <SvgSprite name="custom-circle-plus-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="warning" aria-label="button" icon variant="tonal" border="warning dashed thin opacity-100">
                        <SvgSprite name="custom-send-outline" style="width: 20px; height: 20px" />
                      </v-btn>
                      <v-btn color="error" aria-label="button" icon variant="text">
                        <SvgSprite name="custom-close" style="width: 20px; height: 20px; transform: rotate(45deg)" />
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </UiParentCard>
            </v-col>
            <!-- Loading button -->
            <v-col cols="12">
              <UiParentCard title="Loading Button">
                <div class="d-flex flex-wrap ga-4">
                  <v-btn :loading="loading" rounded="md" color="primary" @click="load">
                    <template v-slot:prepend>
                      <SvgSprite name="custom-home-outline" style="width: 18px; height: 18px" />
                    </template>
                    Home
                  </v-btn>
                  <v-btn color="secondary" variant="outlined" rounded="md">
                    Edit
                    <v-progress-circular size="16" indeterminate color="secondary" aria-label="progressbar" class="ms-2">
                    </v-progress-circular>
                  </v-btn>
                  <v-btn color="info" rounded="md" variant="tonal" text="Loading..." border="info dashed thin opacity-100"></v-btn>
                  <v-btn color="success" variant="flat" icon rounded="md">
                    <v-progress-circular size="16" indeterminate aria-label="progressbar"> </v-progress-circular>
                  </v-btn>
                  <v-btn color="warning" icon variant="tonal" border="warning dashed thin opacity-100">
                    <v-progress-circular size="16" indeterminate aria-label="progressbar"> </v-progress-circular>
                  </v-btn>
                  <v-btn color="error" icon variant="text">
                    <v-progress-circular size="16" indeterminate aria-label="progressbar"> </v-progress-circular>
                  </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Ripple button -->
            <v-col cols="12">
              <UiParentCard title="Ripple">
                <div class="d-flex flex-wrap ga-4">
                  <v-btn color="primary" rounded="md"> With Ripple </v-btn>
                  <v-btn color="primary" rounded="md" :ripple="false"> Without Ripple </v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Density button -->
            <v-col cols="12">
              <UiParentCard title="Density">
                <div class="d-flex flex-wrap align-center ga-4">
                  <v-btn density="compact" rounded="md" color="primary">Compact Button</v-btn>
                  <v-btn density="comfortable" rounded="md" color="primary">Comfortable Button</v-btn>
                  <v-btn density="default" rounded="md" color="primary">Default Button</v-btn>
                </div>
              </UiParentCard>
            </v-col>
            <!-- Rounded -->
            <v-col cols="12">
              <UiParentCard title="Rounded">
                <div class="d-flex ga-4 align-center flex-column flex-wrap flex-sm-row fill-height">
                  <v-btn rounded="0" color="primary">Rounded 0</v-btn>
                  <v-btn rounded="xs" color="secondary">Rounded xs</v-btn>
                  <v-btn rounded="sm" color="success">Rounded sm</v-btn>
                  <v-btn color="info">Rounded sm</v-btn>
                  <v-btn rounded="lg" color="warning">Rounded lg</v-btn>
                  <v-btn rounded="xl" color="error">Rounded xl</v-btn>
                </div>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
