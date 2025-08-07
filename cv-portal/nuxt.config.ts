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
        baseURL: '/dashboard/',
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
        public: {
            apiPartyEndpointsCmsApiUrl: process.env.NUXT_API_PARTY_ENDPOINTS_CMS_API_URL || 'http://localhost:8000/civilian/v1/'
        }
    },

    // API party configuration
    apiParty: {
        endpoints: {
            cmsApiV1: {
                url: process.env.NUXT_API_PARTY_ENDPOINTS_CMS_API_URL || 'http://localhost:8000/civilian/v1/',
                schema: `${process.env.NUXT_API_PARTY_ENDPOINTS_CMS_API_URL || 'http://localhost:8000/civilian/v1/'}/schema/`,
            },
        }
    },
})