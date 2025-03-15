<script setup>
import { ref, computed, reactive } from 'vue';
import moment from 'moment';
import SvgSprite from '@/components/shared/SvgSprite.vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import { vMaska } from 'maska/vue';

const page = ref({ title: 'Mask' });
const breadcrumbs = ref([
  {
    title: 'Plugins',
    disabled: false,
    href: '#'
  },
  {
    title: 'Mask',
    disabled: true,
    href: '#'
  }
]);

const phoneValue = ref('');
const unmaskedPhoneValue = ref('');

const telValue = ref('');
const unmaskedTelValue = ref('');

const usValue = ref('');
const unmaskedUsValue = ref('');

const contactValue = ref('');
const unmaskedContactValue = ref('');

const hexoptions = reactive({
  mask: '!#HHHHHH',
  tokens: {
    H: {
      pattern: /[0-9a-fA-F]/,
      uppercase: true
    }
  }
});
const hexValue = ref('');

const timeValue = ref('');
const unmaskedTimeValue = ref('');

const timeValue1 = ref('');
const unmaskedTimeValue1 = ref('');

const ipValue = ref('');
const unmaskedIpValue = ref('');

const ipv4Value = ref('');
const unmaskedIp4Value = ref('');

const ipv6Value = ref('');
const unmaskedIp6Value = ref('');

const maskedValue = ref('');
const inputValue = ref('');
const maskPattern = computed(() => ({ mask: maskedValue.value }));

defineExpose({
  unmaskedPhoneValue,
  unmaskedTelValue,
  unmaskedUsValue,
  unmaskedContactValue,
  unmaskedTimeValue,
  unmaskedTimeValue1,
  unmaskedIpValue,
  unmaskedIp4Value,
  unmaskedIp6Value,
  hexoptions,
  maskPattern
});

// datepicker
const selectedDate = ref(null);
const selectedDate1 = ref(null);
const computedDateFormattedMomentjs = computed(() => {
  return selectedDate.value ? moment(selectedDate.value).format('D/MM/YYYY') : '';
});
const computedDateFormattedMomentjs1 = computed(() => {
  return selectedDate1.value ? moment(selectedDate1.value).format('D-MM-YYYY') : '';
});
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <!-- Date mask -->
    <v-col cols="12" md="6">
      <UiParentCard title="Date">
        <div>
          <v-row>
            <v-col cols="12">
              <v-label class="mb-2">Insert Date 1</v-label>
              <v-menu>
                <template v-slot:activator="{ props }">
                  <v-text-field
                    single-line
                    hide-details
                    variant="outlined"
                    v-bind="props"
                    v-model="computedDateFormattedMomentjs"
                    placeholder="MM/DD/YYYY"
                    density="comfortable"
                    readonly
                    color="primary"
                  >
                    <template v-slot:append-inner>
                      <SvgSprite name="custom-calendar" class="text-lightText" style="width: 20px; height: 20px" />
                    </template>
                  </v-text-field>
                </template>
                <v-date-picker v-model="selectedDate" hide-header color="primary"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12">
              <v-label class="mb-2">Insert Date 2</v-label>
              <v-menu>
                <template v-slot:activator="{ props }">
                  <v-text-field
                    single-line
                    variant="outlined"
                    hide-details
                    v-bind="props"
                    v-model="computedDateFormattedMomentjs1"
                    placeholder="DD-MM-YYYY"
                    readonly
                    color="primary"
                  >
                    <template v-slot:append-inner>
                      <SvgSprite name="custom-calendar" class="text-lightText" style="width: 20px; height: 20px" />
                    </template>
                  </v-text-field>
                </template>
                <v-date-picker v-model="selectedDate1" hide-header color="primary"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
        </div>
      </UiParentCard>
    </v-col>
    <!-- Time mask -->
    <v-col cols="12" md="6">
      <UiParentCard title="Time">
        <div class="mb-5">
          <v-label class="mb-2">Enter Time 1</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Enter Time"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedTimeValue.unmasked="'##:##:##'"
            v-model="timeValue"
          />
        </div>
        <div>
          <v-label class="mb-2">Enter Time 2</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Enter Date & Time"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedTimeValue1.unmasked="'##/##/#### ##:##:## @@'"
            v-model="timeValue1"
          />
        </div>
      </UiParentCard>
    </v-col>
    <v-col cols="12" md="6">
      <UiParentCard title="Phone no.">
        <div class="mb-5">
          <v-label class="mb-2">Phone Number</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Phone with Code"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedPhoneValue.unmasked="'+1 (###) ###-##-##'"
            v-model="phoneValue"
          />
        </div>
        <div class="mb-5">
          <v-label class="mb-2">Contact Number</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Contact Number"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedContactValue.unmasked="'+91 #### ###-###'"
            v-model="contactValue"
          />
        </div>
        <div class="mb-5">
          <v-label class="mb-2">Telephone with Area Code</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Tel. with Code  Area"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedTelValue.unmasked="'(##) ####-#####'"
            v-model="telValue"
          />
        </div>
        <div class="mb-5">
          <v-label class="mb-2">US Telephone</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="US Telephone"
            variant="outlined"
            density="comfortable"
            v-maska:unmaskedUsValue.unmasked="'(###) ###-#####'"
            v-model="usValue"
          />
        </div>
        <div>
          <v-label class="mb-2">Color code</v-label>
          <v-text-field
            single-line
            hide-details
            color="primary"
            placeholder="Hex color: #121113"
            variant="outlined"
            density="comfortable"
            v-maska="hexoptions"
            v-model="hexValue"
          />
        </div>
      </UiParentCard>
    </v-col>
    <v-col cols="12" md="6">
      <v-row>
        <v-col cols="12">
          <UiParentCard title="Network">
            <div class="mb-5">
              <v-label class="mb-2">Enter IP Address</v-label>
              <v-text-field
                single-line
                hide-details
                color="primary"
                placeholder="Ip Address"
                variant="outlined"
                density="comfortable"
                v-maska:unmaskedIpValue.unmasked="'###.###.###.###'"
                v-model="ipValue"
              />
            </div>
            <div class="mb-5">
              <v-label class="mb-2">Enter IPV4</v-label>
              <v-text-field
                single-line
                hide-details
                color="primary"
                placeholder="Ipv4 Address"
                variant="outlined"
                density="comfortable"
                v-maska:unmaskedIp4Value.unmasked="'####.####.####.####'"
                v-model="ipv4Value"
              />
            </div>
            <div>
              <v-label class="mb-2">Enter IPV6</v-label>
              <v-text-field
                single-line
                hide-details
                color="primary"
                placeholder="Ipv6 Address"
                variant="outlined"
                density="comfortable"
                v-maska:unmaskedIp6Value.unmasked="'####.####.####.####.####.####'"
                v-model="ipv6Value"
              />
            </div>
          </UiParentCard>
        </v-col>
        <v-col cols="12">
          <UiParentCard title="Custom">
            <div class="mb-5">
              <v-label class="mb-2">Make Mask to apply bottom input</v-label>
              <v-text-field
                v-model="maskedValue"
                hide-details
                color="primary"
                single-line
                density="comfortable"
                variant="outlined"
                placeholder="Make Mask to apply bottom input"
              ></v-text-field>
            </div>
            <v-label class="mb-2">Masked Input</v-label>
            <v-text-field
              single-line
              density="comfortable"
              hide-details
              v-maska="maskPattern"
              v-model="inputValue"
              color="primary"
              placeholder="Masked Input"
              variant="outlined"
            ></v-text-field>
          </UiParentCard>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
