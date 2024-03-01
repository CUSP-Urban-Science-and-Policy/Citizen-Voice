<template>
    <v-sheet width="100%" border rounded w class="mb-4">
        <v-toolbar theme="grey-lighten-2" density="compact">
            <v-btn icon>
                <v-icon class="!cursor-grab">mdi-drag</v-icon>
            </v-btn>
            <input v-if="modelValue" type="number" class="font-bold w-10" :value="modelValue.order"
                @input="$emit('update:modelValue', { ...modelValue, order: Number($event.target.value) })">
            <span v-if="questionType"
                class="ml-2 m-1 flex flex-wrap justify-between items-center text-xs sm:text-sm bg-gray-200 rounded px-3 py-1 font-bold leading-loose capitalize">{{
                    questionType }}</span>
            <v-toolbar-title class="ml-2" v-if="title">{{ title }}</v-toolbar-title>
            <v-menu open-on-hover>
                <template v-slot:activator="{ props }">
                    <v-btn icon class="ml-auto" v-bind="props">
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>

                <v-list style="background-color: white;">
                    <!-- Don't remove 'some-value' see:https://github.com/vuetifyjs/vuetify/issues/16558 -->
                    <v-list-item value="some-value" @click="addMapView()">
                        <v-list-item-title>Add Map View</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-toolbar>

        <!-- SLOT -->
        <div class="px-6 p-6">
            <slot></slot>
        </div>

        <!-- MAPVIEW -->
        <div v-if="mapViewActive" class="px-6 pb-6">
            <MapViewComp :questionIndex="questionIndex" :mapViewId="modelValue?.map_view" />
        </div>
    </v-sheet>
</template>

<script setup>
import { useMapViewStore } from "~/stores/mapview"
const MapViewComp = defineAsyncComponent(() => import("../MapView.vue"));

const mapViewActive = ref(false)
const mapviewOptions = ref([])
const selectOption = ref(null)

const mapViewStore = useMapViewStore()

const props = defineProps({
    questionType: String,
    title: String,
    modelValue: Object,
    questionIndex: Number
})

defineEmits(['update:modelValue'])

onMounted(async () => {
    if (props.modelValue?.map_view) {
        mapViewActive.value = true
    }
})

const addMapView = () => {
    mapViewActive.value = true
}

// watch(mapViewActive, async (newQuestion, oldQuestion) => {
//     if (mapViewActive.value) {
//         try {
//             const { data: mapview } = await useAsyncData(() => $cmsApi('/api/map_views/id_names/'));
//             mapviewOptions.value = mapview.value.map(item => ({
//                 id: item.id,
//                 label: item.name
//             }))
//         } catch (error) {
//             console.log(error);
//         }
//     }
// })

// watch(selectOption, async (newQuestion, oldQuestion) => {
//     if (selectOption.value) {
//         try {
//             const { data } = await useAsyncData(() => $cmsApi('/api/map_views/' + selectOption.value + '/'));
//             console.log('data //> ', data)
//             mapviewData.value = data.value
//         } catch (error) {
//             console.log(error);
//         }
//     }
// })


</script>