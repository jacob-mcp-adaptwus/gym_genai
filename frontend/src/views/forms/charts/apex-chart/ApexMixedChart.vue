<script setup lang="ts">
import { computed } from 'vue';

const chartOptions = computed(() => {
  return {
    chart: {
      type: 'line',
      stacked: false,
      height: 350,
      fontFamily: `inherit`,
      foreColor: 'rgba(var(--v-theme-darkText), var(--v-high-opacity))'
    },
    colors: [
      'rgba(var(--v-theme-darkprimary), var(--v-medium-opacity))',
      'rgba(var(--v-theme-primary), var(--v-medium-opacity))',
      'rgba(var(--v-theme-success), var(--v-medium-opacity))'
    ],
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: [1, 1, 4]
    },
    xaxis: {
      categories: [1, 2, 3, 4, 5, 6, 7, 8]
    },
    legend: {
      show: true,
      fontFamily: `inherit`,
      position: 'bottom',
      offsetX: 10,
      offsetY: 10,
      labels: {
        useSeriesColors: false
      },
      markers: {
        width: 16,
        height: 16,
        radius: 5
      },
      itemMargin: {
        horizontal: 15,
        vertical: 8
      }
    },
    grid: {
      borderColor: 'rgba(0,0,0,0.1)'
    }
  };
});
const mixedChart = {
  series: [
    {
      name: 'Income',
      type: 'column',
      data: [14, 2, 25, 15, 25, 28, 38, 46]
    },
    {
      name: 'Cashflow',
      type: 'column',
      data: [11, 3, 31, 4, 41, 49, 65, 85]
    },
    {
      name: 'Revenue',
      type: 'line',
      data: [20, 29, 37, 36, 44, 45, 50, 58]
    }
  ]
};
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Mixed Chart -->
  <!-- ---------------------------------------------------- -->

  <apexchart type="line" height="350" :options="chartOptions" :series="mixedChart.series"> </apexchart>
</template>
