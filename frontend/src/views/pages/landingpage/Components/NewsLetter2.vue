<template>
  <div class="spacer bg-gray100">
    <v-container class="py-0">
      <v-row class="align-center">
        <v-col cols="12" md="8" lg="9">
          <h2 class="text-h2">Be the first to know</h2>
          <p class="text-body-1 mb-0">
            Simply submit your email, we share you the top news related to Able Pro feature updates, roadmap, and news.
          </p>
        </v-col>
        <v-col cols="12" sm="6" lg="3" md="4">
          <div class="d-flex">
            <v-text-field
              variant="outlined"
              color="primary"
              density="comfortable"
              placeholder="Enter your email"
              hide-details
            ></v-text-field>
            <v-btn color="primary" variant="flat" size="large" rounded="md" class="ms-3">Submit</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
  <v-divider></v-divider>
</template>
