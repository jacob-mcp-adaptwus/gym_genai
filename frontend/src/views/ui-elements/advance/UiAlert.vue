<script setup lang="ts">
import { ref } from 'vue';
// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// component content
const page = ref({ title: 'Alert' });
const subContent = ref({
  content: "An alert displays a short, important message in a way that attracts the user's attention without interrupting the user's task."
});
const path = ref({ filepath: 'src/views/ui-elements/advance/alert' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/alerts/' });
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Basic -->
            <v-col cols="12">
              <UiParentCard title="Basic">
                <v-alert color="primary" variant="tonal" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-alert-fill" style="width: 20px; height: 20px" />
                  </template>
                  Primary Text
                </v-alert>
                <v-alert color="secondary" variant="tonal" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-database-outline" style="width: 20px; height: 20px" />
                  </template>
                  Secondary Text
                </v-alert>
                <v-alert color="success" variant="tonal" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-check-square-fill" style="width: 20px; height: 20px" />
                  </template>
                  Success Text
                </v-alert>
                <v-alert color="warning" variant="tonal" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-warning-fill" style="width: 20px; height: 20px" />
                  </template>
                  Warning Text
                </v-alert>
                <v-alert color="info" variant="tonal" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-circle-info-fill" style="width: 20px; height: 20px" />
                  </template>
                  Info Text
                </v-alert>
                <v-alert color="error" variant="tonal" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-bug-fill" style="width: 20px; height: 20px" />
                  </template>
                  Error Text
                </v-alert>
              </UiParentCard>
            </v-col>
            <!-- With Action -->
            <v-col cols="12">
              <UiParentCard title="Actions">
                <v-alert
                  type="success"
                  variant="tonal"
                  density="compact"
                  class="mb-4 border-solid border-success border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                  closable
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-checkbox-marked-circle-outline" style="width: 20px; height: 20px" />
                  </template>
                  <div>Success Text</div>
                </v-alert>
                <v-alert
                  type="warning"
                  variant="tonal"
                  density="compact"
                  class="mb-4 border-solid border-warning border-thin border-opacity-25"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-warning-outline" style="width: 20px; height: 20px" />
                  </template>
                  <div>Warning Text</div>
                  <template v-slot:append>
                    <v-btn variant="text" rounded="md" color="warning">Undo</v-btn>
                  </template>
                </v-alert>
                <v-alert
                  color="primary"
                  variant="tonal"
                  density="compact"
                  class="mb-4 border-solid border-primary border-thin border-opacity-25"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-alert-outline" style="width: 20px; height: 20px" />
                  </template>
                  <div>Primary Text</div>
                  <template v-slot:append>
                    <v-btn variant="flat" rounded="md" color="primary" size="small">Continue</v-btn>
                  </template>
                </v-alert>
              </UiParentCard>
            </v-col>
            <!-- Fill alert -->
            <v-col cols="12">
              <UiParentCard title="Filled">
                <v-alert color="primary" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-alert-fill" style="width: 20px; height: 20px" />
                  </template>
                  Primary Text
                </v-alert>
                <v-alert color="secondary" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-database-outline" style="width: 20px; height: 20px" />
                  </template>
                  Secondary Text
                </v-alert>
                <v-alert color="success" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-check-square-fill" style="width: 20px; height: 20px" />
                  </template>
                  Success Text
                </v-alert>
                <v-alert color="warning" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-warning-fill" style="width: 20px; height: 20px" />
                  </template>
                  Warning Text
                </v-alert>
                <v-alert color="info" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-circle-info-fill" style="width: 20px; height: 20px" />
                  </template>
                  Info Text
                </v-alert>
                <v-alert color="error" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-bug-fill" style="width: 20px; height: 20px" />
                  </template>
                  Error Text
                </v-alert>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="12" md="6">
          <v-row>
            <!-- Description -->
            <v-col cols="12">
              <UiParentCard title="Description">
                <v-alert
                  color="primary"
                  variant="tonal"
                  class="mb-4 border-solid border-primary border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-alert-fill" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Primary text</h6>
                  <div>This is an primary text</div>
                </v-alert>
                <v-alert
                  color="secondary"
                  variant="tonal"
                  class="mb-4 border-solid border-secondary border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-database-outline" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Secondary text</h6>
                  <div>This is an secondary text</div>
                </v-alert>
                <v-alert
                  color="success"
                  variant="tonal"
                  class="mb-4 border-solid border-success border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-check-square-fill" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Success text</h6>
                  <div>This is an success text</div>
                </v-alert>
                <v-alert
                  color="warning"
                  variant="tonal"
                  class="mb-4 border-solid border-warning border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-warning-fill" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Warning text</h6>
                  <div>This is an warning text</div>
                </v-alert>
                <v-alert
                  color="info"
                  variant="tonal"
                  class="mb-4 border-solid border-info border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-circle-info-fill" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Info text</h6>
                  <div>This is an info text</div>
                </v-alert>
                <v-alert
                  color="error"
                  variant="tonal"
                  class="border-solid border-error border-thin border-opacity-25"
                  icon="false"
                  rounded="md"
                >
                  <template v-slot:prepend>
                    <SvgSprite name="custom-bug-fill" class="mt-1" style="width: 20px; height: 20px" />
                  </template>
                  <h6 class="text-h6 text-capitalize mb-1">Error text</h6>
                  <div>This is an error text</div>
                </v-alert>
              </UiParentCard>
            </v-col>
            <!-- Outlined -->
            <v-col cols="12">
              <UiParentCard title="Outlined">
                <v-alert color="primary" variant="outlined" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-alert-outline" style="width: 20px; height: 20px" />
                  </template>
                  Primary Text
                </v-alert>
                <v-alert color="secondary" variant="outlined" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-database-outline" style="width: 20px; height: 20px" />
                  </template>
                  Secondary Text
                </v-alert>
                <v-alert color="success" variant="outlined" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-square-check-outline" style="width: 20px; height: 20px" />
                  </template>
                  Success Text
                </v-alert>
                <v-alert color="warning" variant="outlined" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-warning-outline" style="width: 20px; height: 20px" />
                  </template>
                  Warning Text
                </v-alert>
                <v-alert color="info" variant="outlined" class="mb-4" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-info-circle-outline" style="width: 20px; height: 20px" />
                  </template>
                  Info Text
                </v-alert>
                <v-alert color="error" variant="outlined" icon="false" rounded="md">
                  <template v-slot:prepend>
                    <SvgSprite name="custom-bug-outline" style="width: 20px; height: 20px" />
                  </template>
                  Error Text
                </v-alert>
              </UiParentCard>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
