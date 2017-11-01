from database import *
from settings import *


class Earthquake:
    """
    Seismic event where the surface of the Earth shakes, releasing energy in the
    lithosphere and creating seismic waves.

    Atributtes:
        name        Name of the place where the event takes place
        date        Date of the event
        longitude   Geographic longitude
        latitude    Geographic latitude
        depth       Depth where the event takes place
        magnitude   Number to quantify the size of the event measure using Richter scale

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