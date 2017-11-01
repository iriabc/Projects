import numpy
import matplotlib.pyplot as plot

from mpl_toolkits.basemap import Basemap
from settings import *


class Region:
    """
    Region of the Earth.

    Atributtes:
        latitudes   Geographic latitudes of the data points
        longitudes  Geographic longitudes of the data points
        parallels   Imaginary parallel circles of constant latitude on the earth's surface
        meridians   Imaginary circles of constant longitude on the earth's surface
    """
    def __init__(self):
        self.latitudes = []
        self.longitudes = []
        self.parallels = []
        self.meridians = []

    def create_map_object(self, data):
        self.latitudes = data[:,0]
        self.longitudes = data[:,1]
        lat_min = LAT_MIN
        lat_max = LAT_MAX
        lon_min = LON_MIN
        lon_max = LON_MAX
        map = Basemap(llcrnrlat=lat_min, urcrnrlat=lat_max,\
            llcrnrlon=lon_min, urcrnrlon=lon_max, resolution='l')
        self.parallels = numpy.linspace(lat_min, lat_max, 5)
        self.meridians = numpy.linspace(lon_min, lon_max, 5)
        return map

    def plot_locations(self, map):
        figure = plot.figure()
        x,y = map(self.longitudes, self.latitudes)
        map.plot(x, y, 'or', markersize=3)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        map.etopo()
        plot.title('Earthquakes locations')
        return figure

    def plot_depths(self, map, data):
        figure = plot.figure()
        x,y = map(self.longitudes, self.latitudes)
        colors = map.scatter(
            x, y, marker='o', s=20, lw=0, c=data[:,2], cmap=plot.cm.jet)
        plot.colorbar(colors, orientation='horizontal', pad=0.2)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        map.etopo()
        plot.title('Earthquakes depth')
        return figure

    def plot_magnitudes(self, map, data):
        figure = plot.figure()
        x, y = map(self.longitudes, self.latitudes)
        min_size = 10
        mag_size = data[:,3]*min_size
        colors = map.scatter(
            x, y, marker='o', s=mag_size, lw=0, c=data[:, 3], cmap=plot.cm.jet)
        plot.colorbar(colors, orientation='horizontal', pad=0.2)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        map.etopo()
        plot.title('Earthquakes magnitudes')
        return figure