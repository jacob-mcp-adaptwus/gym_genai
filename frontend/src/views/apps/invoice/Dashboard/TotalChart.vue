<script setup lang="ts">
import { computed } from 'vue';
import { useTheme } from 'vuetify';

const theme = useTheme();
const warningColor = theme.current.value.colors.warning;
const chartOptions = computed(() => {
  return {
    chart: {
      type: 'line',
      stacked: false,
      height: 255,
      fontFamily: `inherit`,
      foreColor: 'rgba(var(--v-theme-secondary), var(--v-high-opacity))',
      toolbar: {
        show: false
      }
    },
    colors: [warningColor, warningColor],
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: [0, 2]
    },
    plotOptions: {
      bar: {
        columnWidth: '50%'
      }
    },
    fill: {
      type: 'gradient',
      gradient: {
        inverseColors: false,
        shade: 'light',
        type: 'vertical',
        opacityFrom: [0, 1],
        opacityTo: [0.5, 1],
        stops: [0, 100],
        hover: {
          inverseColors: false,
          shade: 'light',
          type: 'vertical',
          opacityFrom: 0.15,
          opacityTo: 0.65,
          stops: [0, 96, 100]
        }
      }
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    legend: {
      show: false
    },
    grid: {
      borderColor: 'rgba(0,0,0,0.1)'
    },
    markers: {
      size: [0, 3],
      colors: '#fff',
      strokeWidth: [0, 2],
      strokeColors: warningColor,
      hover: {
        size: 5,
        colors: warningColor,
        strokeColors: '#fff'
      }
    }
  };
});
const mixedChart = {
  series: [
    {
      name: 'TEAM A',
      type: 'column',
      data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30, 25]
    },
    {
      name: 'TEAM B',
      type: 'line',
      data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39, 35]
    }
  ]
};
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Mixed Chart -->
  <!-- ---------------------------------------------------- -->

  <apexchart type="line" height="255" :options="chartOptions" :series="mixedChart.series"> </apexchart>
</template>
