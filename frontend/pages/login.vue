<template>
    <NuxtLayout name="default">
        <div class="custom-login-form">
            <h1 class="text-h6">Login or create an
                <NuxtLink to="/register"> account</NuxtLink>
            </h1>

            <form class="mt-4" @submit.prevent="onSubmit">
                <v-text-field name="email" v-model="email" :error-messages="errorEmail"
                    label="E-mail"></v-text-field>
                <!-- <v-text-field name="password" v-model="password" :error-messages="errorPassword"
                    label="Password"></v-text-field> -->

                <v-text-field class="mb-2" name="password"  @click:append="showPass = !showPass" :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'" :type="showPass ? 'text' : 'password'" v-model="password" :error-messages="errorPassword"
                            label="Password"></v-text-field>

                <VBtn variant="outlined" class="me-4" type="submit">
                    submit
                </VBtn>

                <v-btn variant="outlined" @click="resetForm">
                    clear
                </v-btn>
            </form>
        </div>
    </NuxtLayout>
</template>

<script setup>
import { Form, useForm, useField } from 'vee-validate';
import CenterDiv from "../layouts/centerDiv";
import { useUserStore } from "~/stores/user"
import * as yup from 'yup'

const showPass = ref(false)

const schema = yup.object({
    email: yup.string().email().required(),
    password: yup.string().required(),
});

const { handleSubmit, resetForm } = useForm({
    validationSchema: schema,
});

// Use useField and not useFieldModel for error messages because it doesn't get trickerd on mount
const { value: email, errorMessage: errorEmail } = useField('email')
const { value: password, errorMessage: errorPassword } = useField('password')

const userStore = useUserStore()

const onSubmit = handleSubmit((values) => {
    userStore.loginUser(values.email, values.password)
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
