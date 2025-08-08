<template>
    <div class=" justify-center items-center inline-flex cursor-pointer">
        <NuxtLink :to="props.href"
            class="text-center text-white px-4 py-2 bg-black rounded-3xl cursor-pointer text-xl font-semibold font-['Chillax'] leading-tight tracking-wide">{{
                props.label }}
        </NuxtLink>
    </div>
</template>

<script setup>
const props = defineProps({
    label: String,
    href: String, // keeping href for backward compatibility
})
</script>