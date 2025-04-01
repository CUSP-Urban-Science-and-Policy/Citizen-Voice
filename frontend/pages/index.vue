<template>
    <NuxtLayout name="default">
         <v-sheet d-flex mx-auto px-4 >
            <v-card class="my-card" >
                <!-- <v-img
                    height="300px"
                    src="https://drive.google.com/file/d/1041hE1qlMs2tgF8s9nhtCab8rofvMdGP"
                    cover
                ></v-img> -->
                <v-card-title>
                    <h1>Citizen Voice</h1>
                </v-card-title>
                <v-card-subtitle>
                    An inclusive, web-based, software platform for collaborative data collection that facilitates the citizen participation
                </v-card-subtitle>
                <v-card-text>
                    <h4>
                    Engaging and understanding communities affected by urban development leads to better planning decisions and improved social outcomes. 
                    As a tool for public participation, Citizen Voice opens a channel for citizens to voice their experiences, needs, and aspirations. 
                    Citizen Voice provides the opportunity for citizen involvement from the early phase to the follow-up phase of urban development projects.
                   </h4>
                </v-card-text>  
                <v-card-actions>
                    <v-btn color="primary" @click="navigateTo('/surveys/')">Take Survey</v-btn>
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
