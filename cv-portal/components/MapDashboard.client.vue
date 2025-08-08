<template>
    <div class="-z-0 h-[calc(100vh-72px)] relative" style="width: auto">
        <l-map 
            ref="mapRef" 
            :key="updatekey" 
            v-model:zoom="zoomModel" 
            class="z-0" 
            :center="center" 
            :use-global-leaflet="false"
            :options="{ zoomControl: false }">
            <l-tile-layer 
                :url="currentTileProvider.url" 
                :attribution="currentTileProvider.attribution"
                layer-type="base"
                max-zoom="20"
                :name="currentTileProvider.name" />
            <l-control-zoom position="bottomright" />
            <l-geo-json v-if="geoJsonReady" :geojson="geoJson" :options="geoJsonOptions" />
        </l-map>
        
        <!-- Map provider switch button -->
        <div class="absolute top-4 right-4 z-10">
            <button
                class="bg-white hover:bg-gray-50 border border-gray-300 rounded-md px-3 py-2 text-sm font-medium text-gray-700 shadow-sm transition-colors duration-200 flex items-center gap-2"
                @click="toggleMapProvider">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V7.618a1 1 0 01.553-.894L9 4l6 3 5.447-2.724A1 1 0 0121 5.618v8.764a1 1 0 01-.553.894L15 18l-6-3z" />
                </svg>
                {{ currentTileProvider.name }}
            </button>
        </div>
    </div>
</template>


<script setup>

import { filename } from 'pathe/utils'
import "leaflet/dist/leaflet.css";
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

// Map tile providers configuration
const tileProviders = {
    cartodb: {
        name: 'Light Map',
        url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
       attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    },
    openstreetmap: {
        name: 'Colour Map',
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }
}

// Current tile provider (default to CartoDB Light)
const currentProviderKey = ref('cartodb')
const currentTileProvider = computed(() => tileProviders[currentProviderKey.value])

// Function to toggle between map providers
const toggleMapProvider = () => {
    if (mapRef.value && mapRef.value.leafletObject) {
        // Get current map state
        const map = mapRef.value.leafletObject
        const currentCenter = map.getCenter()
        const currentZoom = map.getZoom()
        
        // Store current state
        const tempCenter = [currentCenter.lat, currentCenter.lng]
        const tempZoom = currentZoom
        
        // Switch provider
        currentProviderKey.value = currentProviderKey.value === 'cartodb' ? 'openstreetmap' : 'cartodb'
        
        // Wait for next tick to ensure the new tile layer is rendered
        nextTick(() => {
            if (mapRef.value && mapRef.value.leafletObject) {
                // Restore the map position
                mapRef.value.leafletObject.setView(tempCenter, tempZoom)
            }
        })
    } else {
        // Fallback for when map is not ready
        currentProviderKey.value = currentProviderKey.value === 'cartodb' ? 'openstreetmap' : 'cartodb'
    }
}

const geoJsonOptions = {
    onEachFeature: (feature, layer) => {
        if (feature?.properties?.question) {

            const options = {
                direction: "top",
                opacity: 1,
            }
            const toolTipContent = `<strong>Question</strong>: ${feature.properties.question.text} ${feature.properties?.annotation ? '<br/> <strong>Answer</strong> ' + feature.properties?.annotation : ''}`

            const icon = feature.properties.question?.topics[0]

            if (icon) {
                const iconString = icon.toLowerCase().split(' ').join('-')
                const myIcon = feature.properties?.annotation ? L.divIcon({
                    className: 'my-div-icon',
                    html: `<div class="wrapper_icon-bubble icon-${iconString}"><img src="${images[iconString]}" class="leaflet-marker-icon icon-pin-bubble icon-${iconString} w-9 h-9 p-[1px]" alt="Marker" tabindex="0" role="button"></div>`,
                    tooltipAnchor: [0, -40],
                    iconSize: [56, 36],
                    iconAnchor: [28, 44]
                }) : L.icon({
                    iconUrl: images[iconString],
                    iconSize: [38, 38],
                    tooltipAnchor: [0, -19],
                    className: `icon-pin-circle icon-${iconString}`
                })


                if (feature.geometry.type === 'Point' && icon) {
                    options.offset = feature.properties?.annotation ? [0, 0] : [0, -16]
                    layer.setIcon(myIcon);
                    layer.bindTooltip(toolTipContent, options);
                }

                // Add an pin icon to the center of any non Point types
                if (feature.geometry.type !== 'Point') {
                    layer.setStyle({
                        color: `var(--${iconString})`,
                        weight: 5,
                        fillColor: `var(--${iconString})`,
                        fillOpacity: 0.4
                    });

                    layer.on('add', () => {
                        const centerMarker = L.marker(layer.getCenter(), { icon: myIcon });
                        centerMarker.bindTooltip(toolTipContent, { ...options });
                        centerMarker.addTo(mapRef.value.leafletObject);
                    })
                }
            } else {
                // Some how this speech bubble is not centered so we are centering it with this
                options.offset = [-15, -10]
                layer.bindTooltip(toolTipContent, options);
            }
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
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    (newGeojson) => {
        if (isEmpty(props.features)) return
        geoJsonReady.value = true
        geoJson.value = props.features
    }
)

watch(
    () => props.filteredFeatures,
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
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
