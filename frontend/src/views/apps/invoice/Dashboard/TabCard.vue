<script setup lang="ts">
import { ref } from 'vue';
import SvgSprite from '@/components/shared/SvgSprite.vue';

import TotalChart from './TotalChart.vue';
import PaidChart from './PaidChart.vue';
import PendingChart from './PendingChart.vue';
import OverdueChart from './OverdueChart.vue';

// tabs data
const tab = ref(0);
</script>

<template>
  <v-card variant="outlined" class="bg-surface">
    <v-card-text>
      <v-tabs v-model="tab" color="primary" class="invoiceTab">
        <v-row no-gutters>
          <v-col cols="12" md="3" sm="6" class="pa-2">
            <v-tab value="1" tag="div" color="dark" hide-slider rounded="lg">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div class="d-flex align-start justify-space-between">
                    <div>
                      <h6 class="text-subtitle-1">Total</h6>
                      <h5 class="text-h5 mb-0">£5678.09</h5>
                      <div class="d-flex align-center">
                        <h5 class="text-h5 mb-0 me-1">3</h5>
                        <p class="text-h6 text-lightText mb-0">invoices</p>
                      </div>
                    </div>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-down" class="text-warning" style="width: 16px; height: 16px" />
                      <h5 class="text-body-1 font-weight-medium text-lightText mb-0 ms-1">20.3%</h5>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </v-tab>
          </v-col>
          <v-col cols="12" md="3" sm="6" class="pa-2">
            <v-tab value="2" tag="div" color="dark" hide-slider rounded="lg">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div class="d-flex align-start justify-space-between">
                    <div>
                      <h6 class="text-subtitle-1 text-start">Paid</h6>
                      <h5 class="text-h5 mb-0">£5678.09</h5>
                      <div class="d-flex align-center">
                        <h5 class="text-h5 mb-0 me-1">5</h5>
                        <p class="text-h6 text-lightText mb-0">invoices</p>
                      </div>
                    </div>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-down" class="text-error" style="width: 16px; height: 16px" />
                      <h5 class="text-body-1 font-weight-medium text-lightText mb-0 ms-1">-8.73%</h5>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </v-tab>
          </v-col>
          <v-col cols="12" md="3" sm="6" class="pa-2">
            <v-tab value="3" tag="div" color="dark" hide-slider rounded="lg">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div class="d-flex align-start justify-space-between">
                    <div>
                      <h6 class="text-subtitle-1 text-start">Pending</h6>
                      <h5 class="text-h5 mb-0">£5678.09</h5>
                      <div class="d-flex align-center">
                        <h5 class="text-h5 mb-0 me-1">20</h5>
                        <p class="text-h6 text-lightText mb-0">invoices</p>
                      </div>
                    </div>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-up-fill" class="text-success" style="width: 16px; height: 16px" />
                      <h5 class="text-body-1 font-weight-medium text-lightText mb-0 ms-1">10.73%</h5>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </v-tab>
          </v-col>
          <v-col cols="12" md="3" sm="6" class="pa-2">
            <v-tab value="4" tag="div" color="dark" hide-slider rounded="lg">
              <v-card variant="outlined" rounded="lg">
                <v-card-text>
                  <div class="d-flex align-start justify-space-between">
                    <div>
                      <h6 class="text-subtitle-1 text-start">Overdue</h6>
                      <h5 class="text-h5 mb-0">£5678.09</h5>
                      <div class="d-flex align-center">
                        <h5 class="text-h5 mb-0 me-1">5</h5>
                        <p class="text-h6 text-lightText mb-0">invoices</p>
                      </div>
                    </div>
                    <div class="d-flex align-center">
                      <SvgSprite name="custom-chevron-down" class="text-primary" style="width: 16px; height: 16px" />
                      <h5 class="text-body-1 font-weight-medium text-lightText mb-0 ms-1">-4.73%</h5>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
            </v-tab>
          </v-col>
        </v-row>
      </v-tabs>
      <v-window v-model="tab" class="mt-5">
        <v-window-item value="1">
          <TotalChart />
        </v-window-item>

        <v-window-item value="2">
          <PaidChart />
        </v-window-item>

        <v-window-item value="3">
          <PendingChart />
        </v-window-item>

        <v-window-item value="4">
          <OverdueChart />
        </v-window-item>
      </v-window>
    </v-card-text>
  </v-card>
</template>
<style lang="scss">
.invoiceTab {
  --v-tabs-height: unset;
  .v-slide-group__content {
    @media (max-width: 960px) {
      flex: unset;
    }
  }
  .v-tab {
    width: auto;
    height: 100%;
    min-width: unset;
    --v-btn-height: unset;
    padding: 0;
    display: block;
    &.v-tab-item--selected {
      .v-card--variant-outlined {
        border: 1px solid transparent;
      }
      > .v-btn__overlay {
        opacity: calc(var(--v-hover-opacity) * var(--v-theme-overlay-multiplier));
      }
    }
  }
}
</style>
