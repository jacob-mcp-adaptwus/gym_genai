<script setup lang="ts">
// imported components
import IncomeOverview from '@/views/widgets/chart/components/IncomeOverview.vue';
import LanguageSupport from '@/views/widgets/chart/components/LanguageSupport.vue';
import NewOrder from '@/views/widgets/chart/components/NewOrder.vue';
import NewUser from '@/views/widgets/chart/components/NewUser.vue';
import NewUser2 from '@/views/widgets/chart/components/NewUser2.vue';
import OverviewCard from '@/views/widgets/chart/components/OverviewCard.vue';
import OverviewTab from '@/views/widgets/chart/components/OverviewTab.vue';
import TotalEarning from '@/views/widgets/chart/components/TotalEarning.vue';
import TotalEarning2 from '@/views/widgets/chart/components/TotalEarning2.vue';
import PaymentHistory from '@/views/widgets/data/components/PaymentHistory.vue';
import StorageCard from '@/views/widgets/statistics/components/StorageCard.vue';
</script>

<template>
  <v-row class="mt-0">
    <v-col cols="12" xl="3" md="6">
      <NewOrder />
    </v-col>

    <v-col cols="12" xl="3" md="6">
      <NewUser />
    </v-col>

    <v-col cols="12" xl="3" md="6">
      <NewUser2 />
    </v-col>

    <v-col cols="12" xl="3" md="6">
      <StorageCard />
    </v-col>

    <v-col cols="12">
      <OverviewTab />
    </v-col>

    <v-col cols="12" xl="3" md="6">
      <v-row>
        <v-col cols="12">
          <IncomeOverview />
        </v-col>
        <v-col cols="12">
          <LanguageSupport />
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="12" xl="6" md="6">
      <OverviewCard />
    </v-col>

    <v-col cols="12" xl="3" md="12">
      <v-row>
        <v-col cols="12" xl="12" md="4">
          <PaymentHistory />
        </v-col>
        <v-col cols="12" xl="12" md="4">
          <v-row>
            <v-col cols="12">
              <TotalEarning />
            </v-col>
            <v-col cols="12">
              <TotalEarning2 />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
