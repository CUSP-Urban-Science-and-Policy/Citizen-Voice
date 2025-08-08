<template>
    <v-app>
        <Header />
        <v-main style="padding-top: 0">
            <v-container>
                <div class="pt-10">
                    <slot />
                </div>
            </v-container>
        </v-main>
        <v-footer>
            <img class="full-height q-py-sm" height="30" width="100" src="~/assets/img/logos/logo-white.png" />
        </v-footer>
    </v-app>
</template>

<script setup>
import Header from '@/components/Header.vue'

</script>

<style lang="scss" scoped>
.custom-zero-padding {
    padding: 0;
    padding-left: 0;
}
</style>