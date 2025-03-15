// src/components/home/HomeBanner.vue
<script setup lang="ts">
import { ref } from 'vue';
import { useDisplay } from 'vuetify';
import { useRouter } from 'vue-router';
import { Brain, Users, Clock } from 'lucide-vue-next';

const { smAndUp } = useDisplay();
const router = useRouter();

const handleGetStarted = () => {
  router.push('/auth/login1');
};

const handleLearnMore = () => {
  // Smooth scroll to features 
  router.push('/info');
};
</script>

<template>
  <div class="home-bg">
    <v-container class="maxWidth">
      <v-row class="spacer align-center justify-center min-h-screen">
        <v-col cols="12" lg="8" md="10" class="text-center">
          <div 
            class="banner-content"
            data-aos="fade-up" 
            data-aos-duration="800"
          >
            <!-- Main Heading -->
            <h1 class="text-h1 font-weight-bold mb-6">
              Transform Teaching with
              <span class="gradient-text">AI-Powered</span>
              <br>
              Lesson Planning
            </h1>

            <!-- Subheading -->
            <p class="text-h5 font-weight-regular text-neutral-dark mb-8">
              Create personalized, engaging lesson plans in minutes using advanced AI technology. 
              Built by teachers, for teachers.
            </p>

            <!-- CTA Buttons -->
            <div class="d-flex justify-center gap-4">
              <v-btn
                color="primary"
                size="x-large"
                rounded="pill"
                elevation="3"
                class="px-8 text-white font-weight-bold"
                @click="handleGetStarted"
              >
                Get Started Free
              </v-btn>
              <v-btn
                color="secondary"
                size="x-large"
                rounded="pill"
                variant="outlined"
                class="px-8 font-weight-bold"
                @click="handleLearnMore"
              >
                See How It Works
              </v-btn>
            </div>

            <!-- Features Preview -->
            <div 
              class="features-preview mt-16"
              data-aos="fade-up" 
              data-aos-delay="200"
            >
              <v-row justify="center" class="gap-4">
                <v-col cols="auto">
                  <div class="feature-card">
                    <div class="feature-icon primary">
                      <Brain :size="32" />
                    </div>
                    <div class="feature-text">
                      <h3 class="text-h6 font-weight-bold">AI-Powered</h3>
                      <p class="text-body-2 text-neutral-dark">
                        Advanced AI customization
                      </p>
                    </div>
                  </div>
                </v-col>
                <v-col cols="auto">
                  <div class="feature-card">
                    <div class="feature-icon secondary">
                      <Users :size="32" />
                    </div>
                    <div class="feature-text">
                      <h3 class="text-h6 font-weight-bold">Student-Focused</h3>
                      <p class="text-body-2 text-neutral-dark">
                        Personalized learning paths
                      </p>
                    </div>
                  </div>
                </v-col>

                <v-col cols="auto">
                  <div class="feature-card">
                    <div class="feature-icon accent">
                      <Clock :size="32" />
                    </div>
                    <div class="feature-text">
                      <h3 class="text-h6 font-weight-bold">Time-Saving</h3>
                      <p class="text-body-2 text-neutral-dark">
                        Create lessons in minutes
                      </p>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <!-- Background Elements -->
    <div class="background-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.home-bg {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  background: linear-gradient(
    135deg,
    rgba(#78C0E5, 0.1) 0%,
    rgba(#B7E6F2, 0.1) 100%
  );
}

.banner-content {
  position: relative;
  z-index: 2;
}

// Typography styles based on design guide
.text-h1 {
  font-family: 'Museo Moderno', sans-serif;
  font-size: clamp(2.5rem, 5vw, 4rem);
  line-height: 1.2;
  color: #5C6970;
  
  @media (max-width: 600px) {
    font-size: 2rem;
  }
}

.gradient-text {
  background: linear-gradient(135deg, #78C0E5, #EF8D61);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  position: relative;
  display: inline-block;
}

// Feature cards
.feature-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(#78C0E5, 0.1);
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(#5C6970, 0.1);
  }

  .feature-icon {
    padding: 12px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;

    &.primary {
      background: rgba(#78C0E5, 0.1);
      color: #78C0E5;
    }

    &.secondary {
      background: rgba(#EF8D61, 0.1);
      color: #EF8D61;
    }

    &.accent {
      background: rgba(#B7E6F2, 0.1);
      color: #B7E6F2;
    }
  }

  .feature-text {
    text-align: left;
    
    h3 {
      color: #5C6970;
      margin-bottom: 4px;
    }
    
    p {
      color: #B7BBBE;
      margin: 0;
    }
  }
}

// Background shapes
.background-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: 50%;
  
  &-1 {
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(#78C0E5, 0.1) 0%, rgba(#78C0E5, 0) 70%);
    top: -100px;
    right: -100px;
  }
  
  &-2 {
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(#EF8D61, 0.1) 0%, rgba(#EF8D61, 0) 70%);
    bottom: -50px;
    left: -50px;
  }
  
  &-3 {
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(#B7E6F2, 0.1) 0%, rgba(#B7E6F2, 0) 70%);
    top: 30%;
    left: 20%;
  }
}

// Responsive styles
@media (max-width: 960px) {
  .features-preview {
    margin-top: 2rem;
  }
  
  .feature-card {
    flex-direction: column;
    text-align: center;
    
    .feature-text {
      text-align: center;
    }
  }
}

// Animation keyframes
@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}
</style>