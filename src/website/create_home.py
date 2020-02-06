from website.laika_conf import get_probes, LaikaProbe
from folium import Popup, Map, Marker, TileLayer, Icon


def create_pop_up(probe: LaikaProbe) -> Popup:
    print(f"Processing {probe.id_}")
    return Popup(f"<b>Name:</b> {probe.id_}</br><b>Location: </b>{probe.desc}", max_width=500)


def add_markers(map_object: Map, file_name: str):
    probes = get_probes(file_name)
    [Marker(probe.coordinates, create_pop_up(probe), icon=Icon(color="darkblue", prefix="fa", icon="wifi")).add_to(map_object) for probe in probes]


def draw_map(file_name: str):
    m = Map(location=[38.319907, 26.639365], attr='Data from <a href="https://openflights.org/data.html">Openflight</a> using Folium and Leaflet.js', zoom_start=15.6)
    TileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',
        attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> Project Laika').add_to(m)
    add_markers(m, file_name)
    m.save("map.html")

if __name__ == "__main__":
    draw_map('../data/laika_config.csv')