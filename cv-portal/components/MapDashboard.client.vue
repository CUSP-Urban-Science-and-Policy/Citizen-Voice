<template>
    <div class="-z-0 h-[calc(100vh-72px)]" style="width: auto">
        <l-map class="z-0" ref="mapRef" v-model:zoom="zoomModel" :center="center" :useGlobalLeaflet="false"
            :key="updatekey" :options="{ zoomControl: false }">
            <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"
                name="OpenStreetMap"></l-tile-layer>
            <l-control-zoom position="bottomright"></l-control-zoom>
            <l-geo-json v-if="geoJsonReady" :geojson="geoJson" :options="geoJsonOptions"></l-geo-json>
        </l-map>
    </div>
</template>

<script setup>
import { filename } from 'pathe/utils'
import "leaflet/dist/leaflet.css";
// import "leaflet-draw/dist/leaflet.draw.css";
import L from 'leaflet';
import { isEmpty } from 'ramda'

const glob = import.meta.glob('@/assets/icons/*.png', { eager: true })
const images = Object.fromEntries(
    Object.entries(glob).map(([key, value]) => [filename(key), value.default])
)

const props = defineProps({
    zoom: {
        default: 8,
        type: Number,
    },
    center: {
        default: () => [52.045, 5.1],
        type: Array,
    },
    features: {
        type: Array,
        default: null
    },
    filteredFeatures: {
        type: Array,
        default: null
    },
});

const mapRef = ref(null);
const zoomLevel = ref(props.zoom);
const updatekey = ref(1);
const geoJsonReady = ref(false)
const geoJson = shallowRef(null)


const geoJsonOptions = {
    onEachFeature: (feature, layer) => {
        if (feature?.properties && feature?.properties?.question) {


            const icon = feature.properties.question?.topics[0]
            const options = {
                direction: "top",
                opacity: 1,
            }

            if (layer?.setIcon && icon) {
                const iconString = icon.toLowerCase().split(' ').join('_')

                const myIcon = feature.properties?.annotation ? L.divIcon({
                    className: 'my-div-icon', // Add your own class name
                    html: `<div class="wrapper_icon-bubble icon-${iconString}"><img src="${images[iconString]}" class="leaflet-marker-icon icon-pin-bubble icon-${iconString} w-9 h-9" alt="Marker" tabindex="0" role="button"></div>`,
                    tooltipAnchor: [0, -19],
                    iconSize: [56, 36],
                }) : L.icon({
                    iconUrl: images[iconString],
                    iconSize: [38, 38],
                    className: `${feature.properties?.annotation ? 'icon-pin-bubble' : 'icon-pin-circle'} icon-${iconString}`
                })
                options.offset = feature.properties?.annotation ? [0, 0] : [0, -16]

                layer.setIcon(myIcon);
            } else {
                options.offset = [-15, -10]
            }

            layer.bindTooltip(`<strong>Question</strong>: ${feature.properties.question.text} ${feature.properties?.annotation ? '<br/> <strong>Answer</strong> ' + feature.properties?.annotation : ''}`, options);
        }
    }
};

// This makes sure the map will be rerenderd or else the changes will not be visible
const zoomModel = computed({
    get() {
        return zoomLevel.value;
    },
    set(newValue) {
        zoomLevel.value = newValue;
    },
});

// Watch for GeoJSON changes
watch(
    () => props.features,
    (newGeojson) => {
        if (isEmpty(props.features)) return
        geoJsonReady.value = true
        geoJson.value = props.features
    }
)

watch(
    () => props.filteredFeatures,
    (newGeojson) => {
        if (isEmpty(props.filteredFeatures)) return
        geoJson.value = props.filteredFeatures
    }
)

</script>

<style>
.icon-pin-circle {
    border-radius: 50%;
}

.icon-pin-bubble {
    /* fill: url('@/assets/icons/pin-bubble.svg') lightgray 6.02px -1.609px / 75.95% 80.902% no-repeat, #36B17A; */
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    position: relative;
    width: 30px;


    padding-left: 10px !important;
    border-radius: 6px;
    /* width: 48.999px !important; */
    flex-shrink: 0;
    padding-right: 10px !important;
    min-width: fit-content;
}

.wrapper_icon-bubble {
    width: fit-content;
    height: auto;
    background: transparent;
}

.wrapper_icon-bubble:after {
    content: "";
    border: 14px solid transparent;
    position: absolute;
    border-top-color: inherit;
    border-bottom: 0;
    bottom: -12px;
    border-radius: 8px;
    transform: translateX(calc(50%));
}

.leaflet-tooltip {
    width: 270px;
    white-space: normal;
}

/* .leaflet-marker-icon:has(.wrapper_icon-bubble) {
    width: auto !important;
    height: auto !important;
} */
</style>
