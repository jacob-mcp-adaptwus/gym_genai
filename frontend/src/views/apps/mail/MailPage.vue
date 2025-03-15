<script setup lang="ts">
import { ref } from 'vue';
import { useDisplay } from 'vuetify';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import MailSidebar from '@/components/apps/mail/MailSidebar.vue';
import MailListing from '@/components/apps/mail/MailListing.vue';

const page = ref({ title: 'Mail Page' });
const { lgAndUp } = useDisplay();
const breadcrumbs = ref([
  {
    title: 'Applications',
    disabled: false,
    href: '#'
  },
  {
    title: 'Mail',
    disabled: true,
    href: '#'
  }
]);
const toggleSide = ref(false);
const sDrawer = ref(false);
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>

  <v-row>
    <v-col v-if="!toggleSide && lgAndUp" class="d-flex align-stretch mailSidebar pe-md-0">
      <v-card variant="outlined" class="bg-surface br-0" rounded="lg">
        <perfect-scrollbar style="height: calc(100vh - 60px)">
          <v-card-text class="pa-5">
            <MailSidebar />
          </v-card-text>
        </perfect-scrollbar>
      </v-card>
    </v-col>
    <v-col class="d-flex align-stretch ps-md-0">
      <v-card variant="outlined" class="bg-surface overflow-hidden bl-0" rounded="lg">
        <!---Toggle Button For mobile-->
        <v-btn icon @click="sDrawer = !sDrawer" aria-label="menu" variant="text" rounded="md" class="d-lg-none d-md-flex d-sm-flex">
          <SvgSprite name="custom-menu-outline" style="width: 18px; height: 18px" />
        </v-btn>

        <div>
          <MailListing @s-Toggle="toggleSide = !toggleSide" />
        </div>
      </v-card>
    </v-col>
  </v-row>

  <v-navigation-drawer temporary v-model="sDrawer" width="300" top v-if="!lgAndUp">
    <perfect-scrollbar style="height: calc(100vh - 100px)">
      <v-card-text class="pa-5"> <MailSidebar /> </v-card-text>
    </perfect-scrollbar>
  </v-navigation-drawer>
</template>
<style lang="scss">
.br-0 {
  @media (min-width: 960px) {
    border-right: none;
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important;
    [dir='rtl'] & {
      border-left: none;
      border-right: 1px solid rgb(var(--v-theme-borderLight));
      border-top-right-radius: 8px !important;
      border-bottom-right-radius: 8px !important;
      border-top-left-radius: 0 !important;
      border-bottom-left-radius: 0 !important;
    }
  }
}
.bl-0 {
  @media (min-width: 960px) {
    border-top-left-radius: 0 !important;
    border-bottom-left-radius: 0 !important;
    [dir='rtl'] & {
      border-top-left-radius: 8px !important;
      border-bottom-left-radius: 8px !important;
      border-top-right-radius: 0 !important;
      border-bottom-right-radius: 0 !important;
    }
  }
}

.custom-main {
  margin: 0;
}
.mailSidebar {
  max-width: 350px;
}
</style>
