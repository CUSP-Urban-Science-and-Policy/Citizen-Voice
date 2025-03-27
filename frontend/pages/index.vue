<template>
    <NuxtLayout name="default">
         <v-sheet d-flex mx-auto px-4 >
            <v-card class="my-card" >
                <v-img
                    height="300px"
                    src="citizens.jpg"
                    eager
                    cover
                    position="center top"
                ></v-img>
                <v-card-title>
                    <h1>Voice Survey Tool</h1>
                </v-card-title>
                <v-card-subtitle>
                   Welcome to Voice Survey Tool
                </v-card-subtitle>
                <v-card-text>
                    <strong>An inclusive, web-based, and open source software platform for collaborative data collection that facilitates the citizen participation.</strong>
                    <br></br>
                    Engaging and understanding communities affected by urban development leads to better planning decisions and improved social outcomes. 
                    As a tool for public participation, Citizen Voice opens a channel for citizens to voice their experiences, needs, and aspirations. 
                    Citizen Voice provides the opportunity for citizen involvement from the early phase to the follow-up phase of urban development projects.
                </v-card-text>  
                <v-card-actions class="d-flex justify-center">
                    <v-btn 
                    size="x-large"
                    rounded="xl"
                    variant="elevated"
                    color="primary"
                    @click="navigateTo('/surveys')">
                    To Survey Demo
                </v-btn>
                </v-card-actions>
            </v-card>
         </v-sheet>

    </NuxtLayout>
</template>

<script setup>

</script>

<style lang="scss" scoped>
.custom-bg-white {
    background-color: #fff;
}
</style>
