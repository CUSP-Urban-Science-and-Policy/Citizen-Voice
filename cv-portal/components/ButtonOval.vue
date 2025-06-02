<template>
    <div class=" justify-center items-center inline-flex cursor-pointer">
        <a :href="href"
            class="text-center text-white px-4 py-2 bg-black rounded-3xl cursor-pointer text-xl font-semibold font-['Chillax'] leading-tight tracking-wide">{{
                label }}
        </a>
    </div>
</template>

<script setup>
const props = defineProps({
    label: String | undefined,
    href: String | undefined,
})
</script>