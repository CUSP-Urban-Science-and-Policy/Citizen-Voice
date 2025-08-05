<template>
    <div>
        <HeaderCVPortal />
        <main style="padding-top: 0">
            <div>
                <div class="pt-10">
                    <slot />
                </div>
            </div>
        </main>
        <FooterCVPortal />
    </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.custom-zero-padding {
    padding: 0;
    padding-left: 0;
}
</style>
