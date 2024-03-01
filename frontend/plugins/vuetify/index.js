// Vuetify
import "./vuetify-config.scss";
import { createVuetify } from 'vuetify'
// import * as components from 'vuetify/components'
// import * as directives from 'vuetify/directives'

/**
 * A few defaults
 */
export const defaults = {
    VAppBar: {
        elevation: 0,
    },
    VBtn: {
        variant: "flat",
        height: 38,
        rounded: "lg",
        size: "small",
    },
    VTextField: {
        color: "primary",
        variant: "outlined",
        density: "comfortable",
    },
};

export default defineNuxtPlugin((nuxtApp) => {
    const vuetify = createVuetify({
        ssr: true,

        defaults,
    })

    nuxtApp.vueApp.use(vuetify)
});