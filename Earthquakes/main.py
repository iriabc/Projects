import requests

from earthquakeModel import *
from regionModel import *
from settings import *


def retrieve_seismic_data():
    """
    Requests data from the API.
    Returns the raw data converted to JSON.
    """
    base_url = BASE_URL
    format = FORMAT
    url = base_url + 'format=' + format + '&starttime=' + START_DATE + '&endtime=' + END_DATE
    response = requests.get(url)
    raw_data = response.json()

    return raw_data


def is_valid_data(row):
    """
    Validates a row of data.
    Returns True if valid.
    """
    return False if row['properties']['mag'] <= 0 else True


def create_earthquakes(earthquakes_data):
    """
    Creates Earthquake objects.
    Returns a list containing earthquake objects.
    """
    earthquakes = []
    for row in earthquakes_data['features']:
        if is_valid_data(row) == True:
            seismic_point = Earthquake(row)
            earthquakes.append(seismic_point)

    return earthquakes


def prepare_data_to_plot(earthquakes):
    """
    Prepares the data to be plotted using Numpy library.
    Returns a list of numpy arrays.
    """
    arrays = []
    for earthquake in earthquakes:
        lat = earthquake.latitude
        lon = earthquake.longitude
        depth = earthquake.depth
        mag = earthquake.magnitude
        arrays.append([lat, lon, depth, mag])

    data = numpy.asarray(arrays, dtype=numpy.float32)

    return data


def generate_plots(earthquakes):
    """
    Creates a Region object and a Basemap object (loading lat and lon data) and creates
    the figures with locations, depths and magnitudes for the earthquakes.
    Returns three figures (locations, depths and magnitudes).
    """
    data = prepare_data_to_plot(earthquakes)

    region = Region()

    map = region.create_map_object(data)

    loc_figure = region.plot_locations(map)
    depth_figure = region.plot_depths(map, data)
    mag_figure = region.plot_magnitudes(map, data)

    return loc_figure, depth_figure, mag_figure


def save_figures(path, earthquakes):
    """
    Saves the figures on the given path.
    """
    loc_figure, depth_figure, mag_figure = generate_plots(earthquakes)

    loc_figure.savefig(path + 'Locations {} to {}'.format(START_DATE, END_DATE),
                       dpi=500)
    depth_figure.savefig(path + 'Depths {} to {}'.format(START_DATE, END_DATE),
                         dpi=500)
    mag_figure.savefig(path +'Magnitudes {} to {}'.format(START_DATE, END_DATE),
                       dpi=500)


def store_data(earthquakes):
    """
    Stores the data in the earthquakes database.
    """

    create_earthquakes_table()
    for earthquake in earthquakes:
        earthquake.save()


def main():
    print('Retrieving data from API...')
    raw_data = retrieve_seismic_data()

    print('Generating earthquakes objects...')
    earthquakes = create_earthquakes(raw_data)

    print('Storing the data into earthquakes database...')
    store_data(earthquakes)

    print('Saving figures to local machine...')
    save_figures('figures/', earthquakes)

    print('--- REQUESTED INFORMATION ---')
    query_earthquake_data(min_magnitude=5)


if __name__ == "__main__":
    main()
