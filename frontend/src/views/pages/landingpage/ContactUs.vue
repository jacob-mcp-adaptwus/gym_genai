<script setup lang="ts">
import { ref } from 'vue';
import Appbar from './Components/AppBarMenu.vue';
import BannerInnerpage from './Components/BannerInnerpage.vue';
import FooterSection from './Components/FooterSection.vue';
import NewsLetter from './Components/NewsLetter2.vue';
import { useCustomizerStore } from '@/stores/customizer';

const checked = ref(true);
const customizer = useCustomizerStore();
</script>

<!-- <template>
  <v-layout class="flex-column" :class="customizer.actTheme === 'dark' ? 'bg-containerBg' : 'bg-surface'">
    <Appbar />
    <v-row class="justify-center">
      <v-col cols="12" class="pb-0">
        <BannerInnerpage
          subtitle="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    "
        >
        </BannerInnerpage>
      </v-col>
      <v-col cols="12" sm="8" md="6" lg="5" class="pt-0">
        <div class="pa-6 py-md-16 py-12 v-col-lg-10 offset-lg-1">
          <v-row>
            <v-col cols="12" lg="6" sm="6">
              <v-label class="mb-2 text-subtitle-1 text-lightText">First Name</v-label>
              <v-text-field density="comfortable" variant="outlined" color="primary" placeholder="First Name" hide-details></v-text-field>
            </v-col>
            <v-col cols="12" lg="6" sm="6">
              <v-label class="mb-2 text-subtitle-1 text-lightText">Last Name</v-label>
              <v-text-field density="comfortable" variant="outlined" color="primary" placeholder="Last Name" hide-details> </v-text-field>
            </v-col>
            <v-col cols="12" sm="12">
              <v-label class="mb-2 text-subtitle-1 text-lightText">Email Address</v-label>
              <v-text-field density="comfortable" variant="outlined" color="primary" placeholder="Email Address" hide-details>
              </v-text-field>
            </v-col>
            <v-col cols="12" sm="12">
              <v-label class="mb-2 text-subtitle-1 text-lightText">Phone Number</v-label>
              <v-text-field
                density="comfortable"
                variant="outlined"
                color="primary"
                placeholder="Phone number"
                type="number"
                hide-details
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="12">
              <v-select
                label="Company Size"
                role="link"
                density="comfortable"
                hide-details
                single-line
                variant="outlined"
                color="primary"
                :items="['1-5', '5-10', '10+']"
              ></v-select>
            </v-col>
            <v-col cols="12" lg="8" md="8">
              <v-checkbox-btn color="primary" class="checkboxLabel" hide-details v-model="checked">
                <template v-slot:label>
                  <p class="mb-0 text-h6">
                    I agree to all the
                    <router-link to="/pages/contact-us" class="mx-1 text-primary text-decoration-none"> Terms & Condition</router-link>
                  </p>
                </template>
              </v-checkbox-btn>
            </v-col>
            <v-col cols="12">
              <v-btn variant="flat" rounded="md" block color="primary">Submit</v-btn>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
    <NewsLetter />
    <FooterSection />
  </v-layout>
</template> -->

<style lang="scss">
.contact-content {
  width: 50%;
  margin-inline: auto;
  @media (max-width: 1530px) {
    width: 60%;
  }
  @media (max-width: 600px) {
    width: 100%;
  }
}
.checkboxLabel {
  .v-label {
    opacity: 1;
  }
}
</style>
