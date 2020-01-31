from typing import List
from laika_conf import get_probes
from folium import Popup, Map, Marker, TileLayer, Icon


def create_pop_up(probe: List[str]) -> str:
    print(f"Processing {probe.id_}")
    return Popup(f"<b>Name:</b> {probe.id_}</br><b>Status: </b>{'online' if probe.online else 'offline'}", max_width=500)


def add_markers(map_object: Map, file_name: str):
    probes = get_probes(file_name)
    [Marker(probe.coordinates, create_pop_up(probe)).add_to(map_object) for probe in probes]


def draw_map(file_name: str):
    m = Map(location=[38.320907, 26.639365], attr='Data from <a href="https://openflights.org/data.html">Openflight</a> using Folium and Leaflet.js', zoom_start=15.4)
    TileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',
        attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>').add_to(m)
    add_markers(m, file_name)
    m.save("map.html")

if __name__ == "__main__":
    draw_map('data/laika_config.csv')