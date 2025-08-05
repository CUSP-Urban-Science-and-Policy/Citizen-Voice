<template>
    <main>
        <img class="w-full h-screen absolute top-0 bottom-0 left-0 right-0" src="~/assets/img/blur-bg.jpg" alt="">
        <div class="w-full h-screen flex justify-center items-center">
            <div
                class="h-[236px] p-3 relative z-20 bg-white shadow-[0px_4px_8px_3px_rgba(0,0,0,0.15)] flex-col justify-start items-center gap-3 inline-flex overflow-hidden">
                <div class="w-[491.36px] h-5 relative flex">
                    <div
                        class="w-[466px] text-black text-xl font-semibold font-['Chillax'] leading-tight tracking-wide">
                        Code of conduct</div>
                    <NuxtLink to="/tour-1" class=" flex-col justify-start items-start inline-flex ">
                        <img src="~/assets/icons/close.svg" class="w-5 h-5" alt="">
                    </NuxtLink>
                </div>
                <div class="w-[491px]">
                    <div
                        class="w-[491px] h-auto text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">
                        The Community Voices Portal is a platform to show what citizens think of their neighbourhood.
                        The
                        data presented have been collected by the Citizen Voice team at TU Delft. <br /><br />While
                        interpreting the data, please keep in mind that all the comments are opinions and observations
                        of
                        citizens and not scientifically proven information. By closing this window, you acknowledge the
                        given information, and you agree not to use the data in any manner intended to harm or
                        disadvantage
                        any third party.</div>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>

</script>

<style lang="scss" scoped></style>
