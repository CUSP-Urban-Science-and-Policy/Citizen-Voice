// https://v3.nuxtjs.org/api/configuration/nuxt.config
import { quasar } from "@quasar/vite-plugin"

const ONE_DAY = 60 * 60 * 24 * 1000
const ONE_WEEK = ONE_DAY * 7

export default defineNuxtConfig({
    build: {
        transpile: ["quasar"],
        loaders: {
            vue: {
                prettify: false // this is to make the nuxt application run
            }
        }
    },
    app: {
        head: {
            title: "Citizen Voice",
            link: [
                { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
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
    css: [
        "@quasar/extras/roboto-font/roboto-font.css",
        "@quasar/extras/material-icons/material-icons.css",
        "@quasar/extras/fontawesome-v6/fontawesome-v6.css",
        "~/assets/styles/quasar.sass",
    ],
    imports: {
        dirs: [
            // Scan top-level modules      
            'composables',
            // ... or scan modules nested one level deep with a specific name and file extension      
            'composables/*/index.{ts,js,mjs,mts}',
            // ... or scan all modules within given directory      
            'composables/**'
        ]
    },
    plugins: [],
    vite: {
        define: {
            'process.env.DEBUG': false,
        },
        plugins: [
            /* vue({
              template: { transformAssetUrls }
            }), */
            quasar({
                sassVariables: "~/assets/styles/quasar.variables.sass",
            }),
        ],

    },
    modules: [
        '@vueuse/nuxt', '@pinia/nuxt', 'nuxt-api-party',
    ],
    runtimeConfig: {
        cookieName: process.env.COOKIE_NAME || '__session',
        cookieSecret: process.env.COOKIE_SECRET || 'secret',
        cookieExpires: parseInt(process.env.COOKIE_REMEMBER_ME_EXPIRES || ONE_DAY.toString(), 10), // 1 day
        cookieRememberMeExpires: parseInt(process.env.COOKIE_REMEMBER_ME_EXPIRES || ONE_WEEK.toString(), 10), // 7 days
        public: {
            baseAPI: process.env.BASE_API || 'http://localhost:3000',
            apiHostPayment: '',
        },
        paymentSecretKey: '',
    },
    // See: https://github.com/johannschopplich/nuxt-api-party
    apiParty: {
        endpoints: {
            'cms-api': { // Becomes `$cmsApi()`
                url: process.env.API_PARTY_CMS_URL,
            }
        }
    },
})

