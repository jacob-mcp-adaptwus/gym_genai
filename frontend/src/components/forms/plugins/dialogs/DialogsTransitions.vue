<script setup lang="ts"></script>

<template>
  <!-- ----------------------------------------------------------------------------- -->
  <!-- Transitions -->
  <!-- ----------------------------------------------------------------------------- -->
  <p class="text-caption text-grey-darken-1">You can make the dialog appear from the top or the bottom.</p>
  <div class="text-center mt-6">
    <v-dialog transition="dialog-bottom-transition">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" variant="flat" v-bind="props">From the bottom</v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-toolbar color="primary" class="px-4">Opening from the bottom</v-toolbar>
          <v-card-item>
            <div class="text-h2 pa-12">Hello world!</div>
          </v-card-item>
          <v-card-actions class="justify-end">
            <v-btn variant="flat" @click="isActive.value = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>

    <v-dialog transition="dialog-top-transition">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" variant="flat" class="ms-2 mt-sm-0" v-bind="props">From the top</v-btn>
      </template>
      <template v-slot:default="{ isActive }">
        <v-card>
          <v-toolbar color="primary" class="px-4">Opening from the top</v-toolbar>
          <v-card-item>
            <div class="text-h2 pa-12">Hello world!</div>
          </v-card-item>
          <v-card-actions class="justify-end">
            <v-btn variant="flat" @click="isActive.value = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </div>
</template>
