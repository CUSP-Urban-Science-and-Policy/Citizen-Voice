// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2025-05-15',
    devtools: { enabled: true },
    modules: [
        '@nuxt/eslint',
        '@nuxt/fonts',
        '@nuxtjs/tailwindcss',
        '@nuxtjs/leaflet',
        'nuxt-api-party'
    ],
    css: [
        "./assets/css/main.css"
    ],

    app: {
        baseURL: '/cv-portal/',
        head: {
            title: " Civilian Dashboard",
            link: [
                { rel: 'icon', type: 'image/x-icon', href: '/favicon-blue.png' },
                {
                    rel: 'stylesheet', href: 'https://unpkg.com/leaflet@1.9.3/dist/leaflet.css',
                    integrity: 'sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI=', crossorigin: ''
                },
            ],
            script: [
                {
                    src: "https://unpkg.com/leaflet@1.9.3/dist/leaflet.js",
                    integrity: "sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM=",
                    crossorigin: ""
                }
            ]
        }
    },

    runtimeConfig: {

        // API party configuration
        apiParty: {
            endpoints: {
                cmsApiV1: { // Becomes `$cmsApi()` and useCmsApiData()
                    url: process.env.API_PARTY_CMS_URL || 'http://localhost:8000/civilian/v1',
                    // token: '',
                    schema: `${process.env.API_PARTY_CMS_URL || 'http://localhost:8000/civilian/v1'}/schema`,
                    // allowedUrls: [ ],
                }
            }
        },

    }
})