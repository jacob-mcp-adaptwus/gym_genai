<script setup lang="ts">
import { computed } from 'vue';

const chartOptions = computed(() => {
  return {
    chart: {
      type: 'polarArea',
      width: 450,
      height: 450,
      fontFamily: `inherit`,
      foreColor: 'rgba(var(--v-theme-darkText), var(--v-high-opacity))'
    },
    colors: [
      'rgba(var(--v-theme-darkprimary), var(--v-high-opacity))',
      'rgba(var(--v-theme-primary), var(--v-high-opacity))',
      'rgba(var(--v-theme-success), var(--v-high-opacity))',
      'rgba(var(--v-theme-error), var(--v-high-opacity))',
      'rgba(var(--v-theme-warning), var(--v-high-opacity))',
      'rgba(var(--v-theme-error), var(--v-high-opacity))',
      'rgba(var(--v-theme-darkprimary), var(--v-high-opacity))',
      'rgba(var(--v-theme-primary), var(--v-high-opacity))',
      'rgba(var(--v-theme-success), var(--v-high-opacity))'
    ],
    fill: {
      opacity: 1
    },
    legend: {
      show: true,
      offsetX: 10,
      offsetY: 10,
      labels: {
        useSeriesColors: false
      },
      markers: {
        width: 12,
        height: 12,
        radius: 5
      },
      itemMargin: {
        horizontal: 25,
        vertical: 4
      }
    },
    responsive: [
      {
        breakpoint: 450,
        chart: {
          width: 280,
          height: 280
        },
        options: {
          legend: {
            show: false,
            position: 'bottom'
          }
        }
      },
      {
        breakpoint: 960,
        chart: {
          width: 250,
          height: 250
        },
        options: {
          legend: {
            show: true,
            position: 'right'
          }
        }
      },
      {
        breakpoint: 1280,
        chart: {
          width: 350,
          height: 350
        },
        options: {
          legend: {
            show: true,
            position: 'right'
          }
        }
      },
      {
        breakpoint: 1550,
        chart: {
          width: 350,
          height: 350
        },
        options: {
          legend: {
            show: false,
            position: 'bottom'
          }
        }
      }
    ],
    tooltip: {
      theme: 'light',
      fillSeriesColor: false
    }
  };
});
const polarChart = {
  series: [14, 23, 21, 17, 15, 10, 12, 17, 21]
};
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Polar Chart -->
  <!-- ---------------------------------------------------- -->

  <apexchart type="polarArea" :options="chartOptions" :series="polarChart.series"> </apexchart>
</template>
