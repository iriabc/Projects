import csv
import requests

from database import *
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


def create_earthquakes(earthquakes_data):
    earthquakes = []
    # all_magnitudes = []
    for row in earthquakes_data['features']:
        seismic_point = Earthquake(row)
        earthquakes.append(seismic_point)
        # all_magnitudes.append(seismic_point.magnitude)

    # print (max(all_magnitudes))
    # print (min(all_magnitudes))

    return earthquakes


def create_earthquakes_file(file_name, earthquakes):
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['name','latitude','longitude','depth','magnitude'])
        for earthquake in earthquakes:
            name = earthquake.name
            lat = earthquake.latitude
            lon = earthquake.longitude
            depth = earthquake.depth
            mag = earthquake.magnitude
            writer.writerow([name, lat, lon, depth, mag])


def plot_earthquakes(file_name):
    """
    Instantiate Region, create basemap object (and load lat ang lon data)
    and plot earthquakes locations, depths and magnitudes.
    """
    data = numpy.genfromtxt(file_name, delimiter=',', usecols=(0, 1, 2, 3, 4))

    region = Region(lat_column=1, lon_column=2)

    map = region.create_map_object(data)

    region.plot_locations(map)
    region.plot_depths(map, data)
    region.plot_magnitudes(map, data)

    plot.show()


def store_data(earthquakes):
    for element in earthquakes:
        row_data = {
            'place': element.name,
            'lat': element.latitude,
            'lon': element.longitude,
            'depth': element.depth,
            'mag': element.magnitude
        }

        save_earthquake_data(row_data, data_type='EARTHQUAKES')
        save_earthquake_data(row_data, data_type='BIG_EARTHQUAKES')


def main():
    raw_data = retrieve_seismic_data()
    earthquakes = create_earthquakes(raw_data)
    create_earthquakes_file('seismicData.csv', earthquakes)
    store_data(earthquakes)
    plot_earthquakes('seismicData.csv')
    # delete_data_table()


if __name__ == "__main__":
    main()


# ToDo:
# - Black border
# - Remove data with negative magnitudes
