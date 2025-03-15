<script setup lang="ts">
import { ref } from 'vue';
import { useDisplay } from 'vuetify';
import ChatListing from '@/components/apps/chats/ChatListing.vue';
import ChatDetail from '@/components/apps/chats/ChatDetail.vue';
import ChatProfile from '@/components/apps/chats/ChatProfile.vue';

const { mdAndUp } = useDisplay();
const toggleSide = ref(false);
const sDrawer = ref(false);
</script>
<template>
  <v-row class="mt-0">
    <v-col v-if="!toggleSide && mdAndUp" class="d-flex align-stretch chatSidebar pe-md-0">
      <v-card variant="outlined" class="bg-surface br-0" rounded="lg">
        <v-card-text class="pa-5">
          <h5 class="text-h5">
            Messages
            <v-chip color="secondary" size="x-small" variant="flat"> 9 </v-chip>
          </h5>
          <ChatListing />
          <ChatProfile />
        </v-card-text>
      </v-card>
    </v-col>
    <v-col class="d-flex align-stretch ps-md-0">
      <v-card variant="outlined" class="bg-surface bl-0" rounded="lg">
        <!---Toggle Button For mobile-->
        <v-btn icon @click="sDrawer = !sDrawer" variant="text" class="d-md-none d-sm-flex ms-4 mt-4">
          <Menu2Icon size="20" />
        </v-btn>
        <ChatDetail @s-Toggle="toggleSide = !toggleSide" />
      </v-card>
    </v-col>
  </v-row>

  <v-navigation-drawer temporary v-model="sDrawer" width="300" top v-if="!mdAndUp">
    <perfect-scrollbar style="height: calc(100vh - 60px)">
      <v-card-text class="pa-5">
        <h5 class="text-h5">
          Messages
          <v-chip color="secondary" size="x-small" variant="flat"> 9 </v-chip>
        </h5>
        <ChatListing />
        <ChatProfile />
      </v-card-text>
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
.chatSidebar {
  max-width: 319px;
  .v-list-item__prepend {
    > .v-avatar {
      ~ .v-list-item__spacer {
        width: 0;
      }
    }
  }
}
</style>
