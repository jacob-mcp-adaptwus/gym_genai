<script setup lang="ts">
import { ref } from 'vue';
// common components
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Chips' });
const subContent = ref({ content: 'Chips are compact elements that represent an input, attribute, or action.' });
const path = ref({ filepath: 'src/views/ui-elements/basic/chip' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/chips/' });

// buttons color data
const chipColor = ref(['primary', 'secondary', 'success', 'warning', 'info', 'error']);

// assets
import avtarImg from '@/assets/images/users/avatar-1.png';
import avtarImg1 from '@/assets/images/users/avatar-6.png';
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <!-- Basic -->
        <v-col cols="12" md="6">
          <UiParentCard title="Basic">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip rounded="lg"> Default </v-chip>

              <v-chip color="primary" variant="flat" rounded="lg"> Color </v-chip>

              <v-chip color="primary" variant="flat" disabled rounded="lg"> Disabled </v-chip>

              <v-chip color="primary" variant="flat" closable rounded="lg"> Deletable </v-chip>

              <v-chip link color="primary" variant="flat" rounded="lg">
                <v-avatar start rounded="lg" size="23">
                  <v-img :src="avtarImg" alt="user"></v-img>
                </v-avatar>
                Avatar
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Outlined Color -->
        <v-col cols="12" md="6">
          <UiParentCard title="Lighter">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip rounded="lg"> Default </v-chip>

              <v-chip color="primary" rounded="lg"> Color </v-chip>

              <v-chip color="primary" disabled rounded="lg"> Disabled </v-chip>

              <v-chip color="primary" closable rounded="lg"> Deletable </v-chip>

              <v-chip link color="primary" rounded="lg">
                <v-avatar start rounded="lg" size="23">
                  <v-img :src="avtarImg1" alt="user"></v-img>
                </v-avatar>
                Avatar
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Outlined -->
        <v-col cols="12" md="6">
          <UiParentCard title="Outlined">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip rounded="lg" variant="outlined"> Default </v-chip>

              <v-chip color="primary" variant="outlined" rounded="lg"> Color </v-chip>

              <v-chip color="primary" variant="outlined" disabled rounded="lg"> Disabled </v-chip>

              <v-chip color="primary" variant="outlined" closable rounded="lg"> Deletable </v-chip>

              <v-chip link color="primary" variant="outlined" rounded="lg">
                <v-avatar start rounded="lg" size="23">
                  <v-img :src="avtarImg1" alt="user"></v-img>
                </v-avatar>
                Avatar
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Combined Color -->
        <v-col cols="12" md="6">
          <UiParentCard title="Combined">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip rounded="lg" border="secondary solid thin opacity-50"> Default </v-chip>

              <v-chip color="primary" border="primary solid thin opacity-50" rounded="lg"> Color </v-chip>

              <v-chip color="primary" border="primary solid thin opacity-50" disabled rounded="lg"> Disabled </v-chip>

              <v-chip color="primary" border="primary solid thin opacity-50" closable rounded="lg"> Deletable </v-chip>

              <v-chip link border="primary solid thin opacity-50" color="primary" rounded="lg">
                <v-avatar start rounded="lg" size="23">
                  <v-img :src="avtarImg1" alt="user"></v-img>
                </v-avatar>
                Avatar
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Closable -->
        <v-col cols="12" md="6">
          <UiParentCard title="Deletable Icon">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip color="error" variant="flat" closable rounded="lg">Default</v-chip>
              <v-chip color="error" variant="flat" rounded="lg">
                Custom Icon
                <template v-slot:close>
                  <svg class="pc-icon ms-1">
                    <use xlink:href="/assets/svg/sprite.svg#custom-minus-square-outline"></use>
                  </svg>
                </template>
              </v-chip>
              <v-chip color="error" rounded="lg" variant="outlined">
                Custom Icon
                <template v-slot:close>
                  <svg class="pc-icon ms-1">
                    <use xlink:href="/assets/svg/sprite.svg#custom-trash-fill"></use>
                  </svg>
                </template>
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Label -->
        <v-col cols="12" md="6">
          <UiParentCard title="Avatar & Icon">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4 text-lightText">
              <v-chip rounded="lg">
                <template v-slot:prepend>
                  <svg class="pc-icon me-1" style="width: 15px; height: 15px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-circle-play-outline"></use>
                  </svg>
                </template>
                Play
              </v-chip>
              <v-chip link border="primary solid thin opacity-50" color="primary" rounded="lg">
                <v-avatar start rounded="lg" size="23">
                  <v-img :src="avtarImg1" alt="user"></v-img>
                </v-avatar>
                Avatar
              </v-chip>
              <v-chip rounded="lg" color="warning" variant="outlined">
                <template v-slot:prepend>
                  <svg class="pc-icon me-1" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-smile-fill"></use>
                  </svg>
                </template>
                Smile
              </v-chip>
              <v-chip rounded="lg" color="error" variant="flat">
                <template v-slot:prepend>
                  <svg class="pc-icon me-1" style="width: 18px; height: 18px">
                    <use xlink:href="/assets/svg/sprite.svg#custom-heart-fill"></use>
                  </svg>
                </template>
                Like
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Sizes -->
        <v-col cols="12" md="6">
          <UiParentCard title="Sizes">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip color="primary" size="x-small" variant="flat" rounded="lg"> x-small chip </v-chip>

              <v-chip color="primary" size="small" variant="flat" rounded="lg"> small chip </v-chip>

              <v-chip color="primary" variant="flat" rounded="lg"> Default </v-chip>

              <v-chip color="primary" size="large" variant="flat" rounded="lg"> large chip </v-chip>

              <v-chip color="primary" size="x-large" variant="flat" rounded="lg"> x-large chip </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <!-- Closable chip -->
        <v-col cols="12" md="6">
          <UiParentCard title="Lighter color">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip color="primary" rounded="lg" closable> Angular </v-chip>
              <v-chip color="secondary" rounded="lg" closable> Jquery </v-chip>
              <v-chip color="warning" rounded="lg" closable> Polymer </v-chip>
              <v-chip color="success" rounded="lg" closable> React </v-chip>
              <v-chip color="error" rounded="lg" closable> Vue.js </v-chip>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12">
          <UiParentCard title="Color">
            <div class="d-flex flex-column flex-sm-row flex-wrap align-center ga-4">
              <v-chip v-for="chip in chipColor" :key="chip" :color="chip" rounded="lg" variant="flat">
                {{ chip }}
              </v-chip>
            </div>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
