<template>
    <NuxtLayout name="default">
        <q-page>
            <pre>{{ data }}</pre>
        </q-page>
    </NuxtLayout>
</template>

<script setup>
const url = "http://localhost:3000/foo"
const { data } = await useAsyncData(() => $fetch(url));
console.log('data //> ', data)
</script>

<style lang="scss" scoped>
.custom-bg-white {
    background-color: #fff;
}
</style>
