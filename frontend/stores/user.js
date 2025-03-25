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
                    url: '',
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
        getAuthToken: (state) => process.client ? localStorage.getItem('token') : state.userData.token
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

            await $authApi('/me/', config)
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

            let res

            try {
                res = await $cmsApi('/api/auth/register/', config)
            } catch (e) {
                // For debugging
                // console.error('statusCode:', e.statusCode)
                // console.error('statusMessage:', e.statusMessage)
                // console.error('data:', e.data)

                let warnMessage = null
                for (const [key, value] of Object.entries(e.data.data)) {
                    warnMessage = warnMessage ? `${warnMessage} \n\n ${key}: ${value}` : `${key}: ${value}`
                }

                // this.userData.error = err
                this.userData.isAuthenticated = false

                // Notification
                global.warning(warnMessage)
            }

            if (res?.token) {
                this.register.succes = true
                // Notification
                global.succes('Register complete')
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

            try {
                const res = await $cmsApi('/api/auth/login/', config)

                if (res?.token) {
                    this.userData = {
                        ...this.userData,
                        isAuthenticated: true,
                        token: res.token,
                        user: res.user,
                        // ...res
                    }
                    localStorage.setItem('token', res.token)

                    // NICETOHAVE: It mees like with the route `redirectedFrom` api you can get the previous link, you can use this to pass in the navigateTo function
                    // See: https://nuxt.com/docs/api/composables/use-route
                    await navigateTo('/design')

                    // Notification
                    global.succes('Login complete')
                }
            } catch (e) {
                // For debugging
                // console.error('statusCode:', e.statusCode)
                // console.error('statusMessage:', e.statusMessage)
                // console.error('data:', e.data.data.non_field_errors)

                // this.userData.error = err
                this.userData.isAuthenticated = false

                // Notification
                if (e.data.data) {
                    global.warning(e.data.data.non_field_errors[0])
                } else {
                    global.warning("Something went wrong with the login")
                }
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
                // Notification
                global.info('You are already logged-out')
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

            await $cmsApi('/api/auth/logout/', config).then(async () => {
                localStorage.removeItem('token')
                this.$reset()
                // Navigate to home
                await navigateTo('/')
                // Notification
                global.succes('Logged-out successfully')
            }).catch(err => {
                global.warning('Something went wrong')
            })

        },
        /**
          * Resets all store values to initial data
          */
        async resetUser() {
            this.$reset()
        },
        /**
         * Get the CSRF token in the cookie stored in the browser
         *  */
        async getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    },
})