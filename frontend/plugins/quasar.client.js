import { defineNuxtPlugin } from '#app'
import * as components from "quasar"
import { Notify } from "quasar";

export default defineNuxtPlugin(nuxtApp => {
    const quasarUserOptions = {
        components,
        plugins: { Notify },
    }

    nuxtApp.vueApp.use(components.Quasar, quasarUserOptions)
})

