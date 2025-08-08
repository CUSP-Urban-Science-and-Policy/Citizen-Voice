<template>
    <NuxtLayout name="default">
      <v-dialog  
        v-model="isDialogOpen" 
        max-width="500"
        persistent
        >
  <template v-slot:default="{ isActive }">
    <v-card >
      <v-card-title class="text-center"> 
        Thank you for Participating!
      </v-card-title>
      <v-card-subtitle class="text-center">
        Your response has been recorded successfully.
      </v-card-subtitle>
      <v-card-text>
      You can customize this message to suit your needs.
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          variant="tonal"
          text="Try Another"
          @click="redirectTo('/surveys')"
        ></v-btn>
        <v-btn
          text="To Home Page"
          @click="redirectTo('/')"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </template>
</v-dialog>
</NuxtLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const isDialogOpen = ref(false);
const router = useRouter();

onMounted(() => {
  isDialogOpen.value = true;
});

function redirectTo(path) {
  isDialogOpen.value = false;
  router.push(path);
}
</script>

<style lang="scss" scoped>
.padding-16 {
    padding: 16px;
}
</style>
