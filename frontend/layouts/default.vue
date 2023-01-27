<template>
    <!-- ClientOnly is needed for quasar to work -->
    <ClientOnly>
        <q-layout view="hHh lpR fFf">

            <q-header elevated class="bg-primary text-white" height-hint="98">
                <q-toolbar>
                    <q-toolbar-title>
                        <img class="full-height q-py-sm" height="30" width="100" src="~/assets/icons/civo-logo.svg">
                    </q-toolbar-title>
                </q-toolbar>

                <div class="row justify-between">
                    <q-tabs align="left">
                        <q-route-tab to="/" label="Home" />
                        <q-route-tab to="/design" label="Start designing" />
                        <q-route-tab to="/surveys" label="Start answering" />
                        <q-route-tab to="/about" label="About" />
                    </q-tabs>

                    <q-tabs align="right">
                        <q-btn-dropdown auto-close flat round stretch icon="person" size="18px">
                            <q-list>
                                <q-item v-if="isAuthenticated" tag="a" to="/user">
                                    <q-item-section>Profile</q-item-section>
                                </q-item>
                                <q-item v-if="!isAuthenticated" tag="a" to="/login">
                                    <q-item-section>Login</q-item-section>
                                </q-item>
                                <q-item v-if="!isAuthenticated" tag="a" to="/register">
                                    <q-item-section>Register</q-item-section>
                                </q-item>
                                <q-item v-if="isAuthenticated" clickable @click="logoutHandler($q)">
                                    <q-item-section>Logout</q-item-section>
                                </q-item>
                            </q-list>
                        </q-btn-dropdown>

                        <!-- <q-route-tab to="/login" label="Login" /> |
                        <q-route-tab to="/register" label="Register" /> -->
                    </q-tabs>
                </div>
            </q-header>


            <q-page-container>
                <!--                <q-page padding>-->
                <slot />
                <!--                </q-page>-->
            </q-page-container>

            <q-footer elevated class="bg-grey-8 text-white">
                <q-toolbar>
                    <q-toolbar-title>
                        <img class="full-height q-py-sm" height="30" width="100" src="~/assets/icons/civo-logo.svg">
                    </q-toolbar-title>
                </q-toolbar>
            </q-footer>

        </q-layout>
    </ClientOnly>
</template>

<script>
import { ref } from 'vue'
import { useUserStore } from "~/stores/user"

export default {
    setup() {
        const userStore = useUserStore()
        const leftDrawerOpen = ref(false)
        const rightDrawerOpen = ref(false)


        const logoutHandler = async ($q) => {
            await userStore.logout($q)
            if (!userStore.isAuthenticated) {
                await navigateTo('/')
            }
        }

        return {
            isAuthenticated: userStore.isAuthenticated,
            logoutHandler,
            leftDrawerOpen,
            toggleLeftDrawer() {
                leftDrawerOpen.value = !leftDrawerOpen.value
            },
            rightDrawerOpen,
            toggleRightDrawer() {
                rightDrawerOpen.value = !rightDrawerOpen.value
            }

        }
    }
}
</script>

<style lang="scss" scoped>
.custom-zero-padding {
    padding: 0;
    padding-left: 0;
}
</style>
