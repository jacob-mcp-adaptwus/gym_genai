<script setup lang="ts">
const barChart = {
  series: [
    {
      data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
    }
  ],
  chartOptions: {
    chart: {
      type: 'bar',
      height: 350,
      fontFamily: `inherit`,
      foreColor: 'rgba(var(--v-theme-secondary), var(--v-high-opacity))'
    },
    colors: 'rgba(var(--v-theme-success), var(--v-high-opacity))',
    plotOptions: {
      bar: {
        borderRadius: 4,
        horizontal: true
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },

    xaxis: {
      categories: [
        'South Korea',
        'Canada',
        'United Kingdom',
        'Netherlands',
        'Italy',
        'France',
        'Japan',
        'United States',
        'China',
        'Germany'
      ]
    },
    fill: {
      opacity: 1
    },
    grid: {
      borderColor: 'rgba(0,0,0,0.1)'
    }
  }
};
</script>

<template>
  <!-- ---------------------------------------------------- -->
  <!-- Bar Chart -->
  <!-- ---------------------------------------------------- -->

  <apexchart type="bar" height="350" :options="barChart.chartOptions" :series="barChart.series"> </apexchart>
</template>
