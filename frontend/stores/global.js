import { defineStore } from 'pinia'
import { useQuasar } from 'quasar'

export const useGlobalStore = defineStore('global', {
    state: () => {
        return {
            QNotify: null
        }
    },
    getters: {
        getQNotify: (state) => state.QNotify
    },
    actions: {
        succesNotify(message = 'Succes') {
            this.getQNotify({
                color: 'green-4',
                textColor: 'white',
                icon: 'cloud_done',
                message: message
            })
        },
        // Use for fail and errors
        negativeNotify(message = 'Something went wrong') {
            this.getQNotify({
                color: 'negative',
                textColor: 'white',
                icon: 'warning',
                message: message
            })
        },
        infoNotify(message) {
            this.getQNotify({
                color: 'info',
                textColor: 'white',
                icon: 'info',
                message: message
            })
        },
        initalizeNotify() {
            const $q = useQuasar()
            this.QNotify = $q.notify
        },
    }
})