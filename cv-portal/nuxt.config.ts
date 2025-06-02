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
    // API party configuration
    apiParty: {
        endpoints: {
            cmsApiV1: {
                url: process.env.API_PARTY_CMS_URL!,
                schema: `${process.env.API_PARTY_CMS_URL}/civilian/v1/schema`
            },
            // cmsApi: {
            //     url: process.env.API_PARTY_CMS_URL!,
            //     schema: `${process.env.API_PARTY_CMS_URL}/api/v2/schema`
            // },
            cmsApiV3: {
                url: process.env.API_PARTY_CMS_URL!,
                schema: `${process.env.API_PARTY_CMS_URL}/voice/v3/schema`
            },
        }
    },
})

console.log(process.env.API_PARTY_CMS_URL)