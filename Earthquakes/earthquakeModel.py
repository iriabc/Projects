from database import *
from settings import *


class Earthquake:
    """
    Set up the seismic info for a certain point
    """
    def __init__(self, data):
        self.name = data['properties']['place'].replace(',', '-')
        self.date = DATE_0 + datetime.timedelta(milliseconds=data['properties']['time'])
        self.longitude = data['geometry']['coordinates'][0]
        self.latitude = data['geometry']['coordinates'][1]
        self.depth = data['geometry']['coordinates'][2]
        self.magnitude = data['properties']['mag']

    def save(self):
        earthquake_data = {
            'place': self.name,
            'date': self.date,
            'lat': round(self.latitude, 3),
            'lon': round(self.longitude, 3),
            'depth': round(self.depth, 3),
            'mag': round(self.magnitude, 3)
        }
        save_earthquake_data(earthquake_data)