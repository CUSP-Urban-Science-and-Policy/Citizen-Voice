<template>
    <NuxtLoadingIndicator />
    <NuxtPage />
</template>

<script setup>
import { useGlobalStore } from "~/stores/global"
const global = useGlobalStore()

if (process.client) {
    global.initalizeNotify()
}

</script>