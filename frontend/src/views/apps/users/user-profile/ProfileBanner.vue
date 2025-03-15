<script setup lang="ts">
import { computed } from 'vue';

const chartOptions = computed(() => {
  return {
    chart: {
      type: 'radialBar',
      width: 136,
      height: 150,
      offsetX: -25,
      offsetY: -10,
      foreColor: 'rgba(var(--v-theme-darkText), var(--v-high-opacity))'
    },
    colors: ['rgba(var(--v-theme-darkprimary), var(--v-high-opacity))'],
    plotOptions: {
      radialBar: {
        offsetY: 0,
        hollow: {
          margin: 5,
          size: '60%'
        },
        track: {
          show: true,
          background: '#ffffff'
        },
        dataLabels: {
          name: {
            show: false
          },
          value: {
            show: true,
            offsetY: 5,
            fontWeight: 700
          }
        }
      }
    },
    grid: {
      padding: {
        right: -50,
        left: -35
      }
    },
    legend: {
      show: false
    }
  };
});

const redialChart = {
  series: [30]
};
</script>

<template>
  <div class="d-flex align-center">
    <!-- ---------------------------------------------------- -->
    <!-- Redial Chart -->
    <!-- ---------------------------------------------------- -->
    <apexchart type="radialBar" class="radial-small" height="140" width="140" :options="chartOptions" :series="redialChart.series">
    </apexchart>
    <div>
      <h5 class="text-h5">Edit Your Profile</h5>
      <p class="mb-0 text-caption text-lightText">Complete your profile to unlock all features</p>
    </div>
  </div>
</template>

<style lang="scss">
.radial-small {
  margin-bottom: -25px;
  [dir='rtl'] & {
    margin-right: -35px;
    margin-left: 40px;
  }
}
</style>
