<template>
    <NuxtLayout name="default">
        <div class="padding-16">
            <center-div>
                <div class="q-pa-md custom-login-form">
                    <h1 class="text-h6">Register</h1>
                    <form class="mt-4" @submit="onSubmit">
                        <v-text-field class="mb-2" name="username" v-model="username" :error-messages="errorUsername"
                            label="Username"></v-text-field>
                        <v-text-field class="mb-2" name="email" v-model="email" :error-messages="errorEmail"
                            label="E-mail"></v-text-field>
                        <v-text-field class="mb-2" name="password"  @click:append="showPass = !showPass" :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'" :type="showPass ? 'text' : 'password'" v-model="password" :error-messages="errorPassword"
                            label="Password"></v-text-field>

                        <div class="flex flex-row mt-4">
                            <v-btn class="mr-4" variant="outlined" type="submit">
                                submit
                            </v-btn>

                            <v-btn variant="outlined" @click="resetForm">
                                clear
                            </v-btn>
                        </div>
                    </form>

                </div>
            </center-div>
        </div>
    </NuxtLayout>
</template>

<script setup>
import { Form, useForm, useField } from 'vee-validate';
import CenterDiv from "../layouts/centerDiv";
import { useUserStore } from "~/stores/user"
import * as yup from 'yup'

const showPass = ref(false)
const userStore = useUserStore()

const schema = yup.object({
    email: yup.string().min(4).email().required(),
    password: yup.string().required().min(8),
    username: yup.string().min(4).required(),
});

const { handleSubmit, resetForm } = useForm({
    validationSchema: schema,
});

// Use useField and not useFieldModel for error messages because it doesn't get trickerd on mount
const { value: username, errorMessage: errorUsername } = useField('username')
const { value: email, errorMessage: errorEmail } = useField('email')
const { value: password, errorMessage: errorPassword } = useField('password')

const onSubmit = handleSubmit(async (values) => {
    await userStore.registerUser({ username: values.username, email: values.email, password: values.password })
});

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
