/**
 * This plugin makes sure that the user store is loaded when using it in the middleware `authorization.js`
 */

import { useUserStore } from "~/stores/user"

export default defineNuxtPlugin(nuxt => {
    const store = useUserStore(nuxt.$pinia);

    addRouteMiddleware('my-middleware', async () => {
    }, { global: true });
});