import requests

from earthquakeModel import *
from regionModel import *
from settings import *


def retrieve_seismic_data():
    base_url = BASE_URL
    format = FORMAT
    url = base_url + 'format=' + format + '&starttime=' + START_DATE + '&endtime=' + END_DATE
    response = requests.get(url)
    raw_data = response.json()

    return raw_data


def is_valid_data(row):
    return False if row['properties']['mag'] <= 0 else True


def create_earthquakes(earthquakes_data):
    earthquakes = []
    for row in earthquakes_data['features']:
        if is_valid_data(row) == True:
            seismic_point = Earthquake(row)
            earthquakes.append(seismic_point)

    return earthquakes


def prepare_data_to_plot(earthquakes):
    arrays = []
    for earthquake in earthquakes:
        lat = earthquake.latitude
        lon = earthquake.longitude
        depth = earthquake.depth
        mag = earthquake.magnitude
        arrays.append([lat, lon, depth, mag])

    data = numpy.asarray(arrays, dtype=numpy.float32)

    return data


def plot_earthquakes(earthquakes):
    """
    Instantiate Region, create basemap object (and load lat ang lon data)
    and plot earthquakes locations, depths and magnitudes.
    """
    data = prepare_data_to_plot(earthquakes)

    region = Region(lat_column=0, lon_column=1)

    map = region.create_map_object(data)

    loc_figure = region.plot_locations(map)
    depth_figure = region.plot_depths(map, data)
    mag_figure = region.plot_magnitudes(map, data)

    return loc_figure, depth_figure, mag_figure


def save_plots(earthquakes):
    loc_figure, depth_figure, mag_figure = plot_earthquakes(earthquakes)

    loc_figure.savefig('figures/Locations {} to {}'.format(START_DATE, END_DATE),
                       dpi=800)
    depth_figure.savefig('figures/Depths {} to {}'.format(START_DATE, END_DATE),
                         dpi=800)
    mag_figure.savefig('figures/Magnitudes {} to {}'.format(START_DATE, END_DATE),
                       dpi=800)


def store_data(earthquakes):
    create_earthquakes_table()
    for earthquake in earthquakes:
        earthquake.save()


def main():
    raw_data = retrieve_seismic_data()
    earthquakes = create_earthquakes(raw_data)

    store_data(earthquakes)
    save_plots(earthquakes)
    query_earthquake_data(min_magnitude=5)


if __name__ == "__main__":
    main()
