<template>
    <main class="h-screen w-full bg-cover overflow-hidden bg-center bg-[#fefefe]/50 backdrop-blur-[10px] "
        :style="{ backgroundImage: `url(${bg})` }">
        <div class="h-screen w-full  bg-[#fefefe]/50 backdrop-blur-[10px]"></div>
        <div class="w-[1440px] h-[1024px] bg-[#fefefe]/50 backdrop-blur-[10px]"></div>
        <h1
            class="text-center justify-start absolute z-10 top-0 text-black text-[32px] font-semibold font-['Chillax'] leading-loose tracking-wide w-full">
            Dashboard Tour</h1>


        <img class="w-auto absolute top-[76px] bottom-0 left-8 right-0 md:h-[620px]" src="~/assets/img/tour-image.png"
            alt="">

        <a href="/tour-2"
            class="px-4 py-2 absolute bg-black rounded-3xl inline-flex justify-center items-center left-[50%] right-[50%] bottom-8 m-auto translate-x-[-50%] w-max cursor-pointer">
            <div
                class="text-center justify-start text-white text-xl font-semibold font-['Chillax'] leading-tight tracking-wide ">
                Next</div>
        </a>

    </main>
</template>

<script setup>
import bg from '~/assets/img/content-frame.jpg'

</script>

<style lang="scss" scoped></style>
