import Toast, { POSITION } from "vue-toastification/dist/index.mjs";
import "vue-toastification/dist/index.css";

export default defineNuxtPlugin(nuxtApp => {
    const config = {
        // Setting the global default position
        position: POSITION.BOTTOM_CENTER,
        timeout: 2000
    }
    nuxtApp.vueApp.use(Toast, config)
})