import { defineStore, } from 'pinia'
import setRequestConfig from './utils/setRequestConfig';
import { useGlobalStore } from './global'

export const useMapViewStore = defineStore('mapView', {
    state: () => ({
        lastSavedZoomLevel: null,
        lastSavedCenter: null
    }),
    getters: {
        // getCurrentQuestions: (state) => state.currentQuestions
    },
    actions: {
        async createMapview(mapSettings) {
            const global = useGlobalStore()
            const config = setRequestConfig({ method: 'POST', body: mapSettings })
            const { data, error, refresh } = await useAsyncData(() => $cmsApi(`/api/map_views/`, config));

            if (error.value) {
                let warnMessage = null
                for (const [key, value] of Object.entries(error._value.data)) {
                    warnMessage = warnMessage ? `${warnMessage} \n\n ${key}: ${value}` : `${key}: ${value}`
                }
                // Notification
                global.warning(warnMessage)
                return null

            }
            // Notification
            global.succes('Map saved')
            return { data: data?.value, refresh }
        },
        async updateMapview(id, mapSettings) {
            const global = useGlobalStore()
            const config = setRequestConfig({ method: 'PATCH', body: mapSettings })
            const { data, error, refresh } = await useAsyncData(() => $cmsApi(`/api/map_views/${id}/`, config));

            if (error.value) {
                let warnMessage = null
                for (const [key, value] of Object.entries(error._value.data)) {
                    warnMessage = warnMessage ? `${warnMessage} \n\n ${key}: ${value}` : `${key}: ${value}`
                }
                // Notification
                global.warning(warnMessage)
                return null

            }
            // Notification
            global.succes('Map update saved')
            return { data: data?.value, refresh }
        },
        async fetchMapView(id) {
            console.log('Map_view id //> ', id)
            const config = setRequestConfig({ method: 'GET' })
            const res = await $cmsApi(`/api/map_views/${id}`, config);
            return res
        }
    },

})