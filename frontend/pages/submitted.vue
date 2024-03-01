<template>
    <NuxtLayout name="default">
        <div class="padding-16">
          <v-sheet
            class="d-flex align-center flex-column"
            height="200"
          >
          <v-card 
            class="my-card" 
            title="Thank you"   
            text="Your response has been submitted successfully. Thank you for participating in the survey."
            variant="flat"
            >
          </v-card>
          </v-sheet>
          </div>
    </NuxtLayout>
</template>

<script setup>

</script>

<style lang="scss" scoped>
.padding-16 {
    padding: 16px;
}
</style>
