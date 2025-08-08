<template>
    <NuxtLayout name="default">
        <div>
            <h1 class="text-h6">User details</h1>
            <p style="color: black">Username: {{ user.userData.user.username }}</p>
            <p style="color: black">Email: {{ user.userData.user.email }}</p>
            <span>TODO: add edit button</span>
        </div>
    </NuxtLayout>
</template>

<script setup>

import { useUserStore } from '~/stores/user'

// Make sure the user is authenticated or trigger the reroute to login
definePageMeta({ middleware: 'authorization' })
const user = useUserStore()

onMounted(async () => {
    await user.loadUser()
})
</script>

<style lang="scss" scoped>
.padding-16 {
    width: 100%;
    height: 100%;
    padding: 16px;
}

.custom-container {
    width: 100%;
    height: 100vh;
}

.custom-login-form {
    width: 33%;
    min-width: 100px;
}
</style>
