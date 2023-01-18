import { defineStore } from 'pinia'
import { useGlobalStore } from './global'

export const useUserStore = defineStore('user', {
    state: () => {
        return {
            userData: {
                token: null,
                isAuthenticated: false,
                pending: false,
                error: '',
                user: {
                    id: null,
                    email: '',
                    username: ''
                },
            },
            register: {
                errorMessage: '',
                succes: '',
            },
        }
    },
    getters: {
        isAuthenticated: (state) => state.userData.isAuthenticated,
    },
    actions: {
        /**
         * See if user is logged-in
         * Remember this only works client side, make user to use `if (process.client) {}` or the `onMounted()` hook in a vue component
         */
        async loadUser() {
            this.userData.error = ''
            this.userData.pending = true
            const token = this.userData.token || localStorage.getItem('token')

            const config = {
                headers: {
                    'Content-Type': 'application/json'
                },
            }

            if (token) {
                config.headers['Authorization'] = `Token ${token}`
            }

            await $backendApi('/api/auth/me/', config)
                .then(response => {
                    this.userData = {
                        ...this.userData,
                        isAuthenticated: true,
                        user: response,
                    }
                })
                .catch(error => {
                    console.log('error //> ', error)
                    this.resetUser()
                    this.userData.error = error
                    this.userData.isAuthenticated = false
                }).finally(() => {
                    this.userData.pending = false
                })
        },
        /**
         * Register user
         * @param {username, email, password} body 
         */
        async registerUser(body) {
            const global = useGlobalStore()

            const config = {
                headers: {
                    'Content-Type': 'application/json'
                },
                method: 'POST',
                body
            }

            const { data: register, pending, error } = await useAsyncData('register', () => $backendApi('/api/auth/register/', config))

            if (error.value) {
                let warnMessage = null
                for (const [key, value] of Object.entries(error._value.data)) {
                    warnMessage = warnMessage ? `${warnMessage} \n\n ${key}: ${value}` : `${key}: ${value}`
                }
                this.register.succes = false
                // Notification
                global.negativeNotify(warnMessage)

            }
            if (register?.value) {
                this.register.succes = true
                // Notification
                global.succesNotify('Register complete')
                await navigateTo('/login')
            }

        },
        /**
         * Login user
         * @param {*} email 
         * @param {*} password 
         * TODO: add pending functionality
         */
        async loginUser(
            email,
            password,
        ) {
            const global = useGlobalStore()
            this.userData.error = ''
            this.userData.pending = true

            const config = {
                method: 'POST',
                body: {
                    email,
                    password,
                },
            }

            const { data: login, pending, error } = await useAsyncData('login', () => $backendApi('/api/auth/login/', config))

            if (error.value) {
                console.log('error: ', error.value)
                let warnMessage = null
                for (const [key, value] of Object.entries(error._value.data)) {
                    warnMessage = warnMessage ? `${warnMessage} \n\n ${key}: ${value}` : `${key}: ${value}`
                }

                // this.userData.error = err
                this.userData.isAuthenticated = false

                // Notification
                global.negativeNotify(warnMessage)

            }
            if (login?.value) {
                console.log('login //> ', login.value)
                this.userData = {
                    ...this.userData,
                    isAuthenticated: true,
                    token: login?.value.token,
                    user: login?.value.user,
                    // ...res
                }
                localStorage.setItem('token', this.userData.token)
                // Notification
                global.succesNotify('Login complete')
                // NICETOHAVE: It mees like with the route `redirectedFrom` api you can get the previous link, you can use this to pass in the navigateTo function
                // See: https://nuxt.com/docs/api/composables/use-route
                await navigateTo('/design')
            }

        },
        /**
         * User logout
         */
        async logout() {
            const global = useGlobalStore()
            const token = this.userData.token || localStorage.getItem('token')

            if (!token) {
                // Resets all stores to initial data
                this.resetUser()
                $q.notify({
                    color: 'blue-5',
                    textColor: 'white',
                    // icon: 'warning',
                    message: 'You are already logged-out'
                })
                // Notification
                global.infoNotify('You are already logged-out')
                return
            }

            const config = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
            }

            if (token) {
                config.headers['Authorization'] = `Token ${token}`
            }

            await $backendApi('/api/auth/logout/', config).then(async () => {
                localStorage.removeItem('token')
                this.$reset()
                // Notification
                global.succesNotify('Logged-out successfully')
                await navigateTo('/')
            }).catch(err => {
                global.negativeNotify('Something went wrong')
            }).finally(() => {
                return
            })

        },
        /**
          * Resets all store values to initial data
          */
        async resetUser() {
            this.$reset()
        }
    },
})