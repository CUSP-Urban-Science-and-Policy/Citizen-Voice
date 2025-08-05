<template>
    <div>
        <HeaderCVPortal />
        <main style="padding-top: 0">
            <div
                class="w-full h-[420px] lg:h-[538px] overflow-hidden gradient-hero flex-col justify-end items-start inline-flex">
                <div
                    class="max-w-[1440px] p-16 flex-col justify-end items-start gap-4 inline-flex w-full ml-auto mr-auto">
                    <div
                        class="w-full text-[#ff4c50] text-[55px] font-semibold font-['Chillax'] leading-[60px] tracking-wide">
                        Welcome to the <br />Community Voices Portal!
                    </div>
                    <div
                        class="w-full max-w-[780px] text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide mt-4">
                        The Community Voices Portal is a dashboard that gives citizen data
                        back to citizens. The dashboard presents local data on how
                        citizens experience their neighbourhood, including their their
                        favourite and least favourite places or where to find green
                        spaces.
                    </div>
                    <ButtonOval class="mt-4" label="Try the dashboard" href="/disclaimer" />
                </div>
            </div>
            <div
                class="w-full max-w-[1440px] mx-auto p-16 bg-white flex-col justify-start items-start gap-4 flex overflow-hidden">
                <div class="text-[#ff4c50] text-[32px] font-semibold font-['Chillax'] leading-loose tracking-wide">
                    This is how Community Voices works:
                </div>
                <div
                    class="w-full max-w-[1062px] text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">
                    The Community Voices Portal shows data collected through a spatial
                    survey by the Citizen Voice team at the Delft University of
                    Technology. The survey covers a variety of topics relevant to
                    urban everyday life, which can give insights into how to better
                    plan and design our neighbourhoods.
                </div>
                <img class="self-stretch h-[927px]" src="~/assets/img/InfoPageFinal_bubble.png" />
                <div class="self-stretch bg-white justify-center items-start gap-10 inline-flex overflow-hidden">
                    <div class="grow shrink basis-0">
                        <span
                            class="text-[#83d873] text-base font-semibold font-['Chillax'] leading-[18px] tracking-wide"><br />1.
                            Survey<br /></span><span
                            class="text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">Citizens
                            answer a survey about how they perceive their
                            neighbourhood. The survey covers a range of topics relevant to
                            urban quality of life. The survey is designed to be inclusive
                            and accessible to all community members.</span>
                    </div>
                    <div class="grow shrink basis-0">
                        <span
                            class="text-[#578dfc] text-base font-semibold font-['Chillax'] leading-[18px] tracking-wide"><br />2.
                            Research<br /></span><span
                            class="text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">Researchers
                            process and analyse the collected data. They
                            group and compare information in ways that allow them to have
                            a deeper understanding of urban spaces and how citizens
                            perceive the city.</span>
                    </div>
                    <div class="grow shrink basis-0">
                        <span
                            class="text-[#ff4c50] text-base font-semibold font-['Chillax'] leading-[18px] tracking-wide"><br />3.
                            Dashboard<br /></span><span
                            class="text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">The
                            dashboard shows citizens perspectives on different
                            aspects of the neighbourhood. The data can be filtered by
                            category to gain deeper insights into specific areas of
                            interest, such as greenery or air pollution.</span>
                    </div>
                    <div class="grow shrink basis-0">
                        <span
                            class="text-[#83d873] text-base font-semibold font-['Chillax'] leading-[18px] tracking-wide"><br />4.
                            Co-creation<br /></span><span
                            class="text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">The
                            citizen data on the dashboard highlights what are the
                            local assets and local priorities of the neighbourhood: what
                            is good and what needs improvement. Urban planners and
                            designers can use these data to make better decisions for the
                            neighbourhood.</span>
                    </div>
                    <div class="grow shrink basis-0">
                        <span
                            class="text-[#937549] text-base font-semibold font-['Chillax'] leading-[18px] tracking-wide"><br />5.
                            Something beautiful<br /></span><span
                            class="text-black text-base font-normal font-['Chillax'] leading-[18px] tracking-wide">We
                            hope this dashboard can help you better understand your
                            neighbourhood and, eventually, create beautiful things
                            together with your neighbours. We encourage anyone to use the
                            data from the dashboard to start their own project and improve
                            the city.
                        </span>
                    </div>
                </div>
            </div>
            <div class="w-full p-14 bg-[#edece7] flex-col items-center  inline-flex mx-auto">
                <p class="text-[#ff4c50] text-[32px] font-semibold font-['Chillax'] leading-loose tracking-wide">
                    Try the dashboard or answer the survey:
                </p>
                <div class="relative max-w-2xl w-full flex justify-between">
                    <ButtonOval class="mt-4" label="I want to see the dashboard" href="/disclaimer" />
                    <ButtonOval class="mt-4" label="I want answer the survey" href="#" />
                </div>

            </div>
        </main>
        <FooterCVPortal />
    </div>
</template>

<script setup>
// import bg from '~/assets/img/portal-hero.jpg'

definePageMeta({
    layout: false
})
</script>

<style scoped>
.padding-16 {
    padding: 16px;
}

.gradient-hero {
    background: linear-gradient(180deg, rgba(237, 236, 231, 0.00) 10.34%, #EDECE7 100%), url('~/assets/img/portal-hero.jpg') lightgray 50% / cover no-repeat;
}
</style>
