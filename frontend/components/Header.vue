<template>
    <v-app-bar density="default" style="width: 100%; height: 112px; position: relative" color="#578DFC">
        <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

        <v-app-bar-title> 
            <a href="/" >
                <img class="full-height q-py-sm" height="60" width="120"
                src="~/assets/img/logos/logo-white.png" />
                </a>
            </v-app-bar-title>

        <v-spacer></v-spacer>

        <v-menu open-on-hover>
            <template v-slot:activator="{ props }">
                <v-btn class="text-none" color="white" v-bind="props">
                    <v-icon size="x-large">mdi-account</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item value="some-value" v-if="isAuthenticated" to="/user">
                    <v-list-item-title>Profile</v-list-item-title>
                </v-list-item>
                <v-list-item value="some-value" v-if="!isAuthenticated" to="/login">
                    <v-list-item-title>Login</v-list-item-title>
                </v-list-item>
                <v-list-item value="some-value" v-if="!isAuthenticated" to="/register">
                    <v-list-item-title>Register</v-list-item-title>
                </v-list-item>
                <v-list-item value="some-value" v-if="isAuthenticated" @click="logoutHandler()">
                    <v-list-item-title>Logout</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>

        <template v-slot:extension>
            <v-tabs v-model="tab" align-tabs="title">
                <v-tab v-for="item in items" :key="item.label" :value="item.value" :to="item.link">
                    {{ item.label }}
                </v-tab>
            </v-tabs>
        </template>
    </v-app-bar>
</template>

<script>
import { useUserStore } from "~/stores/user"

export default {
    data() {
        return {
            tab: null,
            items: [
                {
                    label: 'Home',
                    link: '/'
                },
                {
                    label: 'Surveys',
                    link: '/surveys'
                },
                {
                    label: 'Design survey',
                    link: '/design/surveys'
                },
                {
                    label: 'About',
                    link: '/about'
                }
            ],
            itemsAccount: [
                {
                    label: 'Profile',
                    link: '/user'
                },
                {
                    label: 'Login',
                    link: '/login'
                },
                {
                    label: 'Profile',
                    link: '/user'
                },
                {
                    label: 'Profile',
                    link: '/user'
                }
            ]
        }
    },
    setup() {
        const userStore = useUserStore()

        const logoutHandler = async () => {
            await userStore.logout()
            if (!userStore.isAuthenticated) {
                await navigateTo('/')
            }
        }

        return {
            isAuthenticated: userStore.isAuthenticated,
            logoutHandler,
        }
    }
}
</script>
