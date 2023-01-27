<template>
    <NuxtLayout name="default">
        <q-page style="display: flex;justify-content: center;align-items: center">
            <div class="padding-16">
                <center-div>
                    <div class="q-pa-md custom-login-form">

                        <q-form ref="myForm" class="q-gutter-md">
                            <h1 class="text-h6">Register</h1>

                            <q-input filled v-model="username" label="Username *" lazy-rules
                                :rules="[val => val && val.length > 0 || 'Please type something']" />

                            <q-input filled v-model="email" label="Email *" lazy-rules
                                :rules="[val => val && val.length > 0 || 'Please type something']" />

                            <q-input filled v-model="password" label="Password *" lazy-rules
                                :rules="[val => val !== null && val !== '' || 'Please enter your password']" />

                        </q-form>
                        <div class="q-mt-md">
                            <q-btn label="Submit" @click="onSubmit" color="primary" />
                        </div>
                    </div>
                </center-div>
            </div>
        </q-page>
    </NuxtLayout>
</template>

<script setup>
import CenterDiv from "../layouts/centerDiv";
import { useUserStore } from "~/stores/user"

const userStore = useUserStore()

const username = ref(null)
const email = ref(null)
const password = ref(null)

const onSubmit = async () => {
    await userStore.registerUser({ username: username.value, email: email.value, password: password.value })
}
</script>

<style lang="scss" scoped>
.padding-16 {
    width: 100%;
    height: 100%;
    padding: 16px;
}

.custom-container {
    width: 100%;
    height: 100vh;
}

.custom-login-form {
    width: 33%;
    min-width: 100px;
}
</style>
