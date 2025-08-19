import { useUserStore } from "~/stores/user"

export default defineNuxtRouteMiddleware(async (to, from) => {
    const store = useUserStore()
    // See if user is logged-in
    await store.loadUser()

    if (!store.isAuthenticated) {
        return navigateTo('/login')
    }

})
