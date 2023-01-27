import { useUserStore } from "~/stores/user"

export default defineNuxtRouteMiddleware(async (to, from) => {
    // This only works clientside
    if (process.client) {
        const store = useUserStore()
        // See if user is logged-in
        await store.loadUser()

        if (!store.isAuthenticated) {
            return navigateTo('/login')
        }
    }

})
