<template>
    <div class="custom-container-center-div">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: "centerDiv"
}
</script>

<style scoped>
.custom-container-center-div {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
