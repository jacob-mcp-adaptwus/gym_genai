# Script Section
<script setup lang="ts">
import { shallowRef } from 'vue';
import Logo from './LogoMain.vue';

const educatorResources = shallowRef([
  {
    name: 'Lesson Planner',
    link: '/lessons'
  },
  {
    name: 'Student Profiles',
    link: '/profiles'
  },
  {
    name: 'Resource Library',
    link: '/resources'
  },
  {
    name: 'Teaching Guides',
    link: '/guides'
  }
]);

const support = shallowRef([
  {
    name: 'Documentation',
    link: '/docs'
  },
  {
    name: 'FAQ',
    link: '/faq'
  },
  {
    name: 'Contact Support',
    link: '/support'
  },
  {
    name: 'Feature Request',
    link: '/feedback'
  }
]);

const about = shallowRef([
  {
    name: 'Our Mission',
    link: '/about'
  },
  {
    name: 'Privacy Policy',
    link: '/privacy'
  },
  {
    name: 'Terms of Service',
    link: '/terms'
  },
  {
    name: 'Accessibility',
    link: '/accessibility'
  }
]);

const currentYear = new Date().getFullYear();
</script>

# Template Section
<template>
  <v-footer class="bg-gray100 py-md-16 py-8 flex-column position-relative">
    <v-container>
      <v-row>
        <!-- Logo and Description Column -->
        <v-col cols="12" md="5" lg="4">
          <div class="pe-lg-6">
            <Logo />
            <p class="mt-4 text-h6">
              MathTilda empowers educators to create personalized, AI-powered lesson plans
              that adapt to diverse learning styles and cultural backgrounds, making mathematics 
              more engaging and accessible for every student.
            </p>
          </div>
        </v-col>

        <!-- Educator Resources Column -->
        <v-col cols="12" sm="4" md="3" lg="2">
          <h5 class="text-h5 mb-md-6 mb-4">Educator Resources</h5>
          <div class="d-flex flex-column footer-list">
            <a
              v-for="(item, index) in educatorResources"
              :key="index"
              :href="item.link"
              class="text-h6"
            >
              {{ item.name }}
            </a>
          </div>
        </v-col>

        <!-- Support Column -->
        <v-col cols="12" sm="4" md="2" lg="2">
          <h5 class="text-h5 mb-md-6 mb-4">Support</h5>
          <div class="d-flex flex-column footer-list">
            <a
              v-for="(item, index) in support"
              :key="index"
              :href="item.link"
              class="text-h6"
            >
              {{ item.name }}
            </a>
          </div>
        </v-col>

        <!-- About Column -->
        <v-col cols="12" sm="4" md="2" lg="2">
          <h5 class="text-h5 mb-md-6 mb-4">About</h5>
          <div class="d-flex flex-column footer-list">
            <a
              v-for="(item, index) in about"
              :key="index"
              :href="item.link"
              class="text-h6"
            >
              {{ item.name }}
            </a>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>

  <!-- Copyright Bar -->
  <v-divider></v-divider>
  <div class="sub-footer text-surface bg-gray100 py-4">
    <v-container class="py-0">
      <v-row class="align-center">
        <v-col cols="12" sm="6">
          <h6 class="text-h6 text-medium-emphasis mb-0">
            © {{ currentYear }} MathTilda. All rights reserved.
          </h6>
        </v-col>
        <v-col cols="12" sm="6" class="text-sm-end">
          <v-btn
            icon="custom-github"
            variant="text"
            size="small"
            href="https://github.com/mathtilda"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="GitHub"
          >
          </v-btn>
          <v-btn
            icon="custom-twitter"
            variant="text"
            size="small"
            href="https://twitter.com/mathtilda"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Twitter"
          >
          </v-btn>
          <v-btn
            icon="custom-linkedin"
            variant="text"
            size="small"
            href="https://linkedin.com/company/mathtilda"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="LinkedIn"
          >
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

# Style Section
<style lang="scss" scoped>
// Brand Colors from Design Style Guide
$primary: #78C0E5;
$secondary: #EF8D61;
$accent1: #B7E6F2;
$accent2: #FFCDB5;
$accent3: #C8E0D9;
$neutral-dark: #5C6970;
$neutral-medium: #B7BBBE;
$neutral-light: #F1F1F2;

.v-footer {
  border-top: 1px solid rgba($neutral-medium, 0.2);
  background: linear-gradient(to bottom, $neutral-light, white) !important;

  .v-container {
    max-width: 1400px;
  }
}

// Logo section styling
.logo-section {
  img {
    max-width: 180px;
    height: auto;
  }

  p {
    color: $neutral-dark;
    line-height: 1.6;
    font-family: 'Quicksand', sans-serif;
  }
}

// Footer list styling
.footer-list {
  a {
    color: $neutral-dark;
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 1rem;
    padding: 0.5rem 0;
    transition: all 0.3s ease;

    &:hover {
      color: $primary;
      transform: translateX(4px);
    }

    + a {
      margin-top: 0.5rem;
    }
  }
}

// Heading styles
.text-h5 {
  color: $neutral-dark;
  font-family: 'Museo Moderno', sans-serif;
  font-weight: 600;
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
}

// Sub-footer styling
.sub-footer {
  background-color: rgba($primary, 0.05) !important;
  border-top: 1px solid rgba($neutral-medium, 0.1);

  .text-h6 {
    color: $neutral-dark;
    font-family: 'Quicksand', sans-serif;
    font-size: 0.875rem;
  }

  .v-btn {
    color: $neutral-dark;
    transition: all 0.3s ease;

    &:hover {
      color: $primary;
      transform: scale(1.1);
    }

    + .v-btn {
      margin-left: 1rem;
    }
  }
}

// Responsive adjustments
@media (max-width: 960px) {
  .v-footer {
    padding: 2rem 0;
  }

  .text-h5 {
    margin-bottom: 1rem;
    margin-top: 1.5rem;
  }

  .footer-list {
    a + a {
      margin-top: 0.25rem;
    }
  }

  .sub-footer {
    text-align: center;

    .text-sm-end {
      text-align: center !important;
      margin-top: 1rem;
    }
  }
}

// Accessibility improvements
@media (prefers-reduced-motion: reduce) {
  .footer-list a,
  .v-btn {
    transition: none;
  }
}

// High contrast mode support
@media (forced-colors: active) {
  .footer-list a {
    color: LinkText;
    
    &:hover {
      color: ActiveText;
    }
  }
}
</style>