import csv
import requests

from database import *
from seismicModel import *
from settings import *


def retrieveSeismicData():
    base_url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
    format = 'geojson'
    url = base_url + 'format=' + format + '&starttime=' + START_DATE + '&endtime=' + END_DATE
    response = requests.get(url)
    raw_data = response.json()

    return raw_data


def createEarthquakes(earthquakes_data):
    earthquakes = []
    # all_magnitudes = []
    for row in earthquakes_data['features']:
        seismic_point = Earthquake(row)
        earthquakes.append(seismic_point)
        # all_magnitudes.append(seismic_point.magnitude)

    # print (max(all_magnitudes))
    # print (min(all_magnitudes))

    return earthquakes


def createEarthquakesFile(earthquakes):
    with open('seismicData.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['name','latitude','longitude','depth','magnitude'])
        for earthquake in earthquakes:
            name = earthquake.name
            lat = earthquake.latitude
            lon = earthquake.longitude
            depth = earthquake.depth
            mag = earthquake.magnitude
            writer.writerow([name, lat, lon, depth, mag])


def plotEarthquakes():
    file_name = 'seismicData.csv'
    data = numpy.genfromtxt(file_name, delimiter=',', usecols=(0, 1, 2, 3, 4))

    # Instanciate the mapRegion class
    region = Region(lat_column=1, lon_column=2)

    # Create basemap object from file and load lat and long
    map = region.create_map_object(data)

    # Map with stations
    region.plot_geographic_points(map)

    # Map the depth with colors
    region.plot_color_depth(map, data)

    # Map the magnitude with colors
    region.plot_earthquake_magnitude(map, data)

    plot.show()


def storeData(earthquakes):
    for element in earthquakes:
        row_data = {
            'place': element.name,
            'lat': element.latitude,
            'lon': element.longitude,
            'depth': element.depth,
            'mag': element.magnitude
        }

        saveEarthquakeData(row_data, data_type='EARTHQUAKES')
        saveEarthquakeData(row_data, data_type='BIG_EARTHQUAKES')


def main():
    raw_data = retrieveSeismicData()
    earthquakes = createEarthquakes(raw_data)
    createEarthquakesFile(earthquakes)
    storeData(earthquakes)
    plotEarthquakes()
    # deleteDataTable()


if __name__ == "__main__":
    main()


# ToDo:
# - Circulos linea negra
# - Extraer datos con magnitud negativa
