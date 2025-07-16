<template>
    <div class="w-full h-[72px] px-8 lg:px-16 py-[15px] bg-white justify-between items-center inline-flex">
        <a href="/">
            <img class="w-fit max-h-[42px] max-w-full h-auto" src="~/assets/img/logos/logo-black.png" />
        </a>
        <h1
            class="text-black text-[32px] text-center w-full font-semibold font-['Chillax'] leading-loose tracking-wide">
            Community Voices Portal
        </h1>
        <div class="justify-center items-end gap-5 flex">
            <div class="justify-center items-end gap-[30px] flex overflow-hidden">
                <span
                    class="text-center text-black text-base font-semibold font-['Chillax'] leading-none tracking-wide">Map</span>
            </div>
            <div class="relative -bottom-1" data-svg-wrapper>
                <svg width="2" height="26" viewBox="0 0 2 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1.5L1 24.5" stroke="black" stroke-width="2" stroke-linecap="round" />
                </svg>
            </div>
            <div class="justify-center items-end gap-[30px] flex overflow-hidden">
                <span
                    class="text-center text-black text-base font-medium font-['Chillax'] leading-none tracking-wide">Info</span>
            </div>
        </div>
    </div>
</template>

<script setup>
// optional logic
</script>