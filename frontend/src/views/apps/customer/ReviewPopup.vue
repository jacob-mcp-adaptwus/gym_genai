<script setup>
import { ref, watch } from 'vue';
const props = defineProps({
  dialogs: Object
});
const text = ref(
  'If youre coming from a Series 3, the choice is more difficult. The Series 4 is undoubtedly the better device. And if you care about fall detection, the ECG app, or a larger screen then upgrading makes sense. But I think most people will remain satisfied with their Series 3s.'
);
const items = ref(['Pending', 'Published', 'Confirm']);
const ratting = ref(3.5);

const dialogVisible = ref(props.dialogs.dialog);

// Watch for changes in the prop and update the local state accordingly
watch(
  () => props.dialogs.dialog,
  (newValue) => {
    dialogVisible.value = newValue;
  }
);
</script>
<template>
  <!-- to-do eslint error -->
  <v-dialog v-model="dialogVisible" max-width="400">
    <v-card>
      <v-card-item><h3 class="text-h5 mb-3">Edit Review</h3></v-card-item>
      <v-divider></v-divider>
      <v-card-text>
        <v-label class="mb-2">Product name</v-label>
        <v-text-field
          single-line
          variant="outlined"
          density="comfortable"
          placeholder="Enter Product"
          model-value="Apple Watch Series 4"
        ></v-text-field>
        <v-label class="mb-2">Author</v-label>
        <v-text-field
          single-line
          variant="outlined"
          density="comfortable"
          placeholder="Enter Author"
          model-value="Joseph William"
        ></v-text-field>
        <v-label class="mb-2">Review</v-label>
        <v-textarea single-line variant="outlined" density="comfortable" placeholder="Text of Review" v-model="text"> </v-textarea>
        <div>Rating</div>
        <v-rating
          background-color="orange lighten-3"
          color="warning"
          density="compact"
          half-increments
          hover
          size="16"
          v-model="ratting"
        ></v-rating>
        <br />
        <v-label class="mb-2 mt-5">Status</v-label>
        <v-select single-line :items="items" label="Outlined variant" variant="outlined" model-value="Pending"></v-select>
      </v-card-text>
      <v-card-actions>
        <!-- to-do eslint error -->
        <v-btn color="primary" variant="flat" rounded="md" @click="$emit('close')">Create</v-btn
        ><v-btn variant="flat" rounded="md" @click="$emit('close')">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
