<script setup lang="ts">
const props = defineProps({
  subtitle: String
});
</script>

<template>
  <v-main class="mx-0 pt-16 pb-0 position-relative overflow-hidden">
    <div class="bg-blur">
      <div class="round-1"></div>
      <div class="round-2"></div>
    </div>
    <v-container class="maxWidth">
      <v-row class="justify-center py-10">
        <v-col cols="12" lg="5" md="6" sm="8">
          <div class="text-center position-relative">
            <h2 class="text-h2 mb-2">Talk to our Expert</h2>
            <p class="text-h6 text-lightText mb-0">
              {{ props.subtitle }}
            </p>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<style lang="scss">
.headerBg {
  padding-top: 69px;
}
.mailImage {
  margin-top: -50px;
}
</style>
