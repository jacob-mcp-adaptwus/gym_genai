<script setup lang="ts">
import { computed } from 'vue';

const chartOptions = computed(() => {
  return {
    chart: {
      type: 'radialBar',
      height: 250,
      fontFamily: `inherit`
    },
    colors: [
      'rgba(var(--v-theme-darkprimary), var(--v-medium-opacity))',
      'rgba(var(--v-theme-primary), var(--v-medium-opacity))',
      'rgba(var(--v-theme-success), var(--v-medium-opacity))',
      'rgba(var(--v-theme-error), var(--v-medium-opacity))'
    ],
    plotOptions: {
      radialBar: {
        offsetY: 0,
        startAngle: 0,
        endAngle: 270,
        hollow: {
          margin: 5,
          size: '30%',
          background: 'transparent',
          image: undefined
        },
        dataLabels: {
          name: {
            show: false
          },
          value: {
            show: false
          }
        }
      }
    },
    labels: ['Vimeo', 'Messenger', 'Facebook', 'LinkedIn'],
    legend: {
      show: true,
      floating: true,
      fontSize: '16px',
      position: 'left',
      offsetX: 0,
      offsetY: 15,
      labels: {
        useSeriesColors: true
      },
      markers: {
        size: 0
      },
      itemMargin: {
        vertical: 3
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
      }
    ]
  };
});

const redialChart = {
  series: [76, 67, 61, 90]
};
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Redial Chart -->
  <!-- ---------------------------------------------------- -->

  <apexchart type="radialBar" height="350" :options="chartOptions" :series="redialChart.series"> </apexchart>
</template>
