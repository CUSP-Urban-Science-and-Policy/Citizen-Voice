import { defineStore } from 'pinia'

// toast.info("Info toast");
// toast.success("Success toast");
// toast.error("Error toast");
// toast.warning("Warning toast");

export const useGlobalStore = defineStore('global', {
    state: () => {
        return {
            notify: null
        }
    },
    getters: {
        getNotify: (state) => state.notify
    },
    actions: {
        initalizeNotify() {
            (async () => {
                const { useToast } = await import("vue-toastification")
                this.notify = useToast()
            })()
        },
        succes(message = 'Succes') {
            this.notify.info(message);
        },
        warning(message = 'Something went wrong') {
            this.notify.warning(message);
        },
        error(message = 'Something went wrong') {
            this.notify.error(message);
        },
        info(message) {
            this.notify.info(message);
        },
    }
})