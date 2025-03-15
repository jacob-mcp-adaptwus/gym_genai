<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const valid = ref(false);
const logform = ref();
const email = ref('');
// Email validation rules
const emailRules = ref([
  (v: string) => !!v.trim() || 'E-mail is required',
  (v: string) => {
    const trimmedEmail = v.trim();
    return !/\s/.test(trimmedEmail) || 'E-mail must not contain spaces';
  },
  (v: string) => /.+@.+\..+/.test(v.trim()) || 'E-mail must be valid'
]);

const router = useRouter();

function validate() {
  if (logform.value && logform.value.validate()) {
    router.push('/starter');
  }
}
</script>

<template>
  <v-form ref="logform" lazy-validation v-model="valid" action="/starter" @submit.prevent="validate" class="mt-7 loginForm">
    <v-label>Email address</v-label>
    <v-text-field
      v-model="email"
      :rules="emailRules"
      placeholder="Enter email address"
      class="mt-2 mb-6"
      required
      density="comfortable"
      hide-details="auto"
      variant="outlined"
      color="primary"
      @input="email = email.trim()"
    ></v-text-field>

    <h6 class="text-caption">Do not forgot to check SPAM box.</h6>
    <v-btn color="primary" block class="mt-2" variant="flat" size="large" rounded="md" :disabled="!valid" type="submit"
      >Send Password Reset Email</v-btn
    >
  </v-form>
</template>
