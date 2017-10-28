import csv
import requests

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
    for row in earthquakes_data['features']:
        seismic_point = Earthquake(row)
        earthquakes.append(seismic_point)

    return earthquakes


def saveEarthquakesData(earthquakes):
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



def main():
    raw_data = retrieveSeismicData()
    earthquakes = createEarthquakes(raw_data)
    saveEarthquakesData(earthquakes)
    plotEarthquakes()



if __name__ == "__main__":
    main()
