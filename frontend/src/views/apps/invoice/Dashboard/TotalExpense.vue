<script setup lang="ts">
import { computed, shallowRef } from 'vue';
import { useTheme } from 'vuetify';

import SvgSprite from '@/components/shared/SvgSprite.vue';
import CardHeader from '@/components/shared/CardHeader.vue';

const theme = useTheme();
const successColor = theme.current.value.colors.success;
const warningColor = theme.current.value.colors.warning;
const errorColor = theme.current.value.colors.error;
const lightprimaryColor = theme.current.value.colors.lightprimary;

const chartOptions = computed(() => {
  return {
    chart: {
      type: 'donut',
      height: 230,
      fontFamily: `inherit`
    },
    colors: [warningColor, successColor, errorColor, lightprimaryColor],
    plotOptions: {
      donut: {
        size: '15%'
      }
    },
    stroke: {
      width: 0
    },
    labels: ['Pending', 'Paid', 'Overdue', 'Draft'],
    legend: {
      show: false
    },
    dataLabels: {
      enabled: false
    },
    tooltip: {
      theme: 'light',
      fillSeriesColor: false
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          }
        }
      }
    ]
  };
});

const redialChart = {
  series: [30, 28, 22, 20]
};

const Expensedata = shallowRef([
  {
    status: 'Pending',
    color: 'warning',
    price: '$3,202'
  },
  {
    status: 'Paid',
    color: 'success',
    price: '$45,050'
  },
  {
    status: 'Overdue',
    color: 'error',
    price: '$25,000'
  },
  {
    status: 'Draft',
    color: 'lightprimary',
    price: '$7,694'
  }
]);
</script>

<template>
  <CardHeader title="Total Expenses" class="overflow-hidden">
    <template v-slot:header>
      <v-btn variant="text" aria-label="menu" color="secondary" icon rounded="md" size="small">
        <SvgSprite name="custom-more-outline" style="width: 20px; height: 20px" />
      </v-btn>
    </template>
    <div class="pa-5">
      <apexchart type="donut" height="230" :options="chartOptions" class="invoiceChart" :series="redialChart.series"> </apexchart>
      <v-list density="compact" class="pb-0" aria-label="expense list" aria-busy="true">
        <v-list-item v-for="(item, i) in Expensedata" :key="i" class="pa-0">
          <h6 class="text-subtitle-1 text-lightText mb-0">
            <v-badge dot :color="item.color" size="large" inline> </v-badge>
            {{ item.status }}
          </h6>
          <template v-slot:append>
            <h5 class="text-h6 font-weight-medium mb-0">{{ item.price }}</h5>
          </template>
        </v-list-item>
      </v-list>
    </div>
  </CardHeader>
</template>
<style lang="scss">
.invoiceChart {
  .apexcharts-canvas {
    margin: 0 auto;
  }
}
</style>
