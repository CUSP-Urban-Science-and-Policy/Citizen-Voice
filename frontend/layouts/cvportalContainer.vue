<template>
  <v-app>
    <HeaderCVPortal />
    <v-main style="padding-top: 0">
      <v-container>
        <div class="pt-10">
          <slot />
        </div>
      </v-container>
    </v-main>
    <FooterCVPortal />
  </v-app>
</template>

<script setup></script>

<style lang="scss" scoped>
.custom-zero-padding {
  padding: 0;
  padding-left: 0;
}
</style>
