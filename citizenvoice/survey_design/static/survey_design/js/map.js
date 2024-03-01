// Setup LeafletJS
var longLat = [52.011, 4.358]
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
    minZoom: 3,
    zoomControl: false
})
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
map.setView(longLat, 12);

L.control.zoom({
    position: 'bottomright'
}).addTo(map);

var group_circle = L.featureGroup();
map.addLayer(group_circle)

// Polygon Test
var polygon = 0
var overlay_selected = 1
function onMapLeftClick(e) {
    if(overlay_selected==1) {
        L.circle(e.latlng, {
            color: 'green',
            fillColor: '#7FFF00',
            fillOpacity: 0.3,
            radius: 2000
        }).addTo(group_circle)
    }
    else if(overlay_selected==2) {
    L.circle(e.latlng, {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.3,
        radius: 2000
    }).addTo(group_circle)
    }
    else {
        if(polygon==0){
            polygon = L.polygon([e.latlng], {color: 'blue'}).addTo(map);
        }
        else {
            polygon.addLatLng(e.latlng);
        }
    }
}

map.on('click', onMapLeftClick);

function select_circle_green() {
    overlay_selected = 1
}

function select_circle_red() {
    overlay_selected = 2
}

function select_polygon() {
    overlay_selected = 3
}

