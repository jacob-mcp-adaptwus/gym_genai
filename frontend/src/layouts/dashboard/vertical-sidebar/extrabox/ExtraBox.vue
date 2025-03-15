
<template>
  <v-sheet rounded="md" color="surface" class="pa-4 support-box text-center pb-6" border>
    <div class="d-flex align-center flex-column">
      <v-img 
        src="/images/teacher-support.svg" 
        alt="teacher support" 
        class="mb-3" 
        width="160" 
        cover>
      </v-img>
      
      <div class="px-3">
        <h5 class="text-h5 mb-1 font-weight-medium">Need Help?</h5>
        <div class="text-body-1 text-medium-emphasis">
          Our education specialists are here to help
        </div>
        <div class="text-caption text-medium-emphasis mt-1">
          Response time: 24 hours
        </div>
      </div>
    </div>

    <div class="mt-5 d-flex flex-column gap-2">
      <v-btn
        color="primary"
        variant="elevated"
        class="rounded-lg"
        href="mailto:support@adaptwithus.org"
      >
        Email Support
      </v-btn>

      <v-btn
        variant="text"
        color="primary"
        class="rounded-lg"
        to="/faq"
      >
        View FAQ
      </v-btn>
    </div>

    <div class="mt-4">
      <v-divider class="mb-3"></v-divider>
      <div class="text-caption text-medium-emphasis">
        For urgent matters, call: (531) 283-2009
      </div>
    </div>
  </v-sheet>
</template>

<style lang="scss" scoped>
.support-box {
  position: relative;
  overflow: hidden;
  max-width: 320px;
  margin: auto;
  
  // Optional gradient background
  background: linear-gradient(
    to bottom,
    var(--v-surface-base),
    var(--v-surface-lighten3)
  );

  // Hover effect on buttons
  :deep(.v-btn) {
    transition: transform 0.2s ease;
    
    &:hover {
      transform: translateY(-2px);
    }
  }
}
</style>
