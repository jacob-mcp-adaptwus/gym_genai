<script setup lang="ts">
import { ref, shallowRef } from 'vue';

// common components
import SvgSprite from '@/components/shared/SvgSprite.vue';
import ComponentTitle from '@/components/shared/ComponentTitle.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// define consts
const caption_email1 = ref('demo@company.com');
const caption_email2 = ref('demo@company.com');
const caption_email3 = ref('demo@company.com');
const validate_email1 = ref('demo.sd');
const validate_email2 = ref('demo.sd');
const multiline2 = ref('Default Value');
const select_sm = ref<string>('Small');
const full_text = ref('Default');
const some_imp1 = ref('Default');
const some_imp2 = ref('Default');
const some_imp3 = ref('Default');

// rules for email textfield
const rules = ref({
  required: (value: string) => !!value || 'Required.',
  counter: (value: string) => value.length <= 20 || 'Max 20 characters',
  email: (value: string) => {
    const pattern =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return pattern.test(value) || 'Invalid e-mail.';
  }
});

//  data of select
const items = ref(['None', 'demo@company.com', 'Judiya@company.com', 'taju_diya@company.com']);

// confirm edit text
const model = shallowRef('Egg plant');

// component content
const page = ref({ title: 'Textfield' });
const subContent = ref({ content: 'Text fields let users enter and edit text.' });
const path = ref({ filepath: 'src/views/forms/components/textfield' });
const link = ref({ filelink: 'https://vuetifyjs.com/en/components/text-fields/' });
</script>

<template>
  <ComponentTitle :title="page.title" :subContent="subContent.content" :path="path.filepath" :link="link.filelink"></ComponentTitle>
  <v-row>
    <v-col cols="12">
      <v-row>
        <v-col cols="12" md="6">
          <!-- variant -->
          <UiParentCard title="Variant">
            <div>
              <v-text-field label="Outlined" color="primary" variant="outlined"></v-text-field>

              <v-text-field label="Filled" density="comfortable" color="primary" variant="filled" rounded="false"></v-text-field>

              <v-text-field label="Underlined" color="primary" variant="underlined"></v-text-field>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- general -->
          <UiParentCard title="General">
            <div>
              <v-text-field color="primary" persistent-placeholder placeholder="Email Address" variant="outlined"></v-text-field>

              <v-text-field
                color="primary"
                persistent-placeholder
                placeholder="Email Address"
                value="demo@company.com"
                variant="outlined"
              ></v-text-field>

              <v-text-field
                color="primary"
                persistent-placeholder
                placeholder="demo@company.com"
                variant="outlined"
                disabled
              ></v-text-field>
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- with caption -->
          <UiParentCard title="With Caption">
            <v-text-field color="primary" aria-label="email address" v-model="caption_email1" label="Email Address" variant="outlined">
              <template v-slot:prepend-inner>
                <SvgSprite name="custom-mail-outline" style="width: 20px; height: 20px" />
              </template>
            </v-text-field>
            <v-text-field
              color="primary"
              aria-label="email address"
              v-model="caption_email2"
              label="Email Address"
              variant="outlined"
            ></v-text-field>
            <v-text-field color="primary" aria-label="email address" v-model="caption_email3" label="Email Address" variant="outlined">
              <template v-slot:append-inner>
                <SvgSprite name="custom-mail-outline" style="width: 20px; height: 20px" />
              </template>
            </v-text-field>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- with validation -->
          <UiParentCard title="With Validation">
            <v-text-field
              color="error"
              class="mb-4"
              aria-label="email address"
              v-model="validate_email1"
              :rules="[rules.required, rules.email]"
              label="Email Address"
              variant="outlined"
              error
            >
              <template v-slot:prepend-inner>
                <SvgSprite name="custom-mail-outline" style="width: 20px; height: 20px" />
              </template>
            </v-text-field>
            <v-text-field
              color="error"
              class="mb-4"
              aria-label="email address"
              error
              v-model="validate_email2"
              :rules="[rules.required, rules.email]"
              label="Email Address"
              variant="outlined"
            >
            </v-text-field>
            <v-text-field color="error" aria-label="email address" label="Email Address" variant="outlined"> </v-text-field>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- With Icon & Adornments -->
          <UiParentCard title="With Icon & Adornments">
            <v-text-field variant="outlined" color="primary" persistent-placeholder placeholder="Email address">
              <template v-slot:prepend-inner>
                <SvgSprite name="custom-mail-outline" style="width: 20px; height: 20px" />
              </template>
            </v-text-field>
            <v-text-field variant="outlined" color="primary" persistent-placeholder placeholder="Email address">
              <template v-slot:prepend-inner>
                <SvgSprite name="custom-lock-outline" style="width: 20px; height: 20px" />
              </template>
              <template v-slot:append-inner>
                <SvgSprite name="custom-eye" style="width: 20px; height: 20px" />
              </template>
            </v-text-field>
            <v-text-field persistent-placeholder placeholder="John Deo" color="primary" variant="outlined">
              <template v-slot:prepend-inner>
                <span class="v-card-subtitle px-0">Mr</span>
                <v-divider class="ms-3" inset vertical></v-divider>
              </template>
            </v-text-field>
            <v-text-field persistent-placeholder placeholder="Password" color="primary" variant="outlined">
              <template v-slot:append-inner>
                <v-divider class="me-3" inset vertical></v-divider>
                <span class="v-card-subtitle px-0">.com</span>
              </template>
            </v-text-field>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- Multiline -->
          <UiParentCard title="Multiline">
            <v-textarea
              filled
              auto-grow
              label="Multiline Placeholder"
              rows="1"
              single-line
              row-height="20"
              color="primary"
              variant="outlined"
            ></v-textarea>
            <v-textarea
              filled
              auto-grow
              aria-label="multiline"
              label="Multiline Placeholder"
              variant="outlined"
              rows="4"
              single-line
              color="primary"
              v-model="multiline2"
            ></v-textarea>
            <v-textarea
              clearable
              clear-icon="$closeCircle"
              variant="outlined"
              placeholder="Multiline Clearable"
              rows="1"
              row-height="20"
              single-line
              value="This is clearable text."
              color="primary"
            ></v-textarea>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- Select -->
          <UiParentCard title="Select">
            <v-select
              :items="items"
              color="primary"
              role="link"
              single-line
              label="Email Address"
              variant="outlined"
              density="comfortable"
            ></v-select>
            <v-select
              role="link"
              :items="items"
              color="primary"
              single-line
              label="Email Address"
              variant="outlined"
              density="compact"
              v-model="select_sm"
              outlined
            ></v-select>
          </UiParentCard>
        </v-col>
        <v-col cols="12" md="6">
          <!-- size -->
          <UiParentCard title="Size">
            <v-text-field variant="outlined" color="primary" single-line label="Default"> </v-text-field>
            <v-text-field variant="outlined" color="primary" density="compact"> </v-text-field>
          </UiParentCard>
        </v-col>
        <v-col cols="12">
          <!-- Layout -->
          <UiParentCard title="Layout">
            <v-label class="mb-2">Label</v-label>
            <v-text-field
              label="Label"
              aria-label="label"
              single-line
              hint="Full Width!"
              v-model="full_text"
              persistent-hint
              variant="outlined"
              color="primary"
            ></v-text-field>
            <v-row class="mt-5">
              <v-col cols="12" md="4">
                <v-label class="mb-2">None</v-label>
                <v-text-field
                  label="None"
                  aria-label="none"
                  single-line
                  hint="Some important text"
                  v-model="some_imp1"
                  persistent-hint
                  variant="outlined"
                  color="primary"
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="4">
                <v-label class="mb-2">Dense</v-label>
                <v-text-field
                  label="Dense"
                  aria-label="dense"
                  single-line
                  hint="Some important text"
                  v-model="some_imp2"
                  persistent-hint
                  variant="outlined"
                  color="primary"
                  density="compact"
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="4">
                <v-label class="mb-2">Normal</v-label>
                <v-text-field
                  label="Normal"
                  aria-label="normal"
                  single-line
                  hint="Some important text"
                  v-model="some_imp3"
                  persistent-hint
                  variant="outlined"
                  color="primary"
                ></v-text-field>
              </v-col>
            </v-row>
          </UiParentCard>
        </v-col>
        <v-col cols="12">
          <v-card variant="outlined" elevation="0" class="bg-surface" rounded="lg">
            <v-card-item class="pa-5">
              <v-card-title class="text-subtitle-1" style="line-height: 1.57">
                Confirm Edit
                <v-chip variant="tonal" color="primary" class="ms-1" size="small">new</v-chip>
              </v-card-title>
            </v-card-item>
            <v-divider></v-divider>
            <v-card-text>
              <v-confirm-edit v-model="model">
                <template v-slot:default="{ model: proxyModel, actions }">
                  <v-card class="mx-auto pa-0" variant="text">
                    <v-label class="mb-2" for="update-value">Update field</v-label>
                    <v-text-field
                      v-model="proxyModel.value"
                      variant="outlined"
                      id="update-value"
                      single-line
                      messages="Modify my value"
                    ></v-text-field>
                    <template v-slot:actions>
                      <v-spacer />

                      <component :is="actions"></component>
                    </template>
                  </v-card>
                </template>
              </v-confirm-edit>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
