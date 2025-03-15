<script setup>
import { ref } from 'vue';

import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

import DialogsActivator from '@/components/forms/plugins/dialogs/DialogsActivator.vue';
import DialogsModel from '@/components/forms/plugins/dialogs/DialogsModel.vue';
import DialogsFullscreen from '@/components/forms/plugins/dialogs/DialogsFullscreen.vue';
import DialogsTransitions from '@/components/forms/plugins/dialogs/DialogsTransitions.vue';
import DialogsPersistent from '@/components/forms/plugins/dialogs/DialogsPersistent.vue';
import DialogsScrollable from '@/components/forms/plugins/dialogs/DialogsScrollable.vue';
import DialogsForm from '@/components/forms/plugins/dialogs/DialogsForm.vue';
import DialogsNested from '@/components/forms/plugins/dialogs/DialogsNested.vue';

// component content
const page = ref({ title: 'Dialog' });
const subContent = ref({
  content: 'Dialogs inform users about a task and can contain critical information, require decisions, or involve multiple tasks.'
});
const path = ref({ filepath: 'src/views/forms/plugins/modal' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/dialogs/' });
</script>
<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12" md="12">
      <v-row>
        <v-col cols="12" sm="12" md="6">
          <UiParentCard title="Activator">
            <DialogsActivator />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6">
          <UiParentCard title="V-model">
            <DialogsModel />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Fullscreen">
            <DialogsFullscreen />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Transitions">
            <DialogsTransitions />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Persistent">
            <DialogsPersistent />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Scrollable">
            <DialogsScrollable />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Form">
            <DialogsForm />
          </UiParentCard>
        </v-col>
        <v-col cols="12" sm="12" md="6" class="d-flex align-items-stretch">
          <UiParentCard title="Nested Dialog">
            <DialogsNested />
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
