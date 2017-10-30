import numpy
import matplotlib.pyplot as plot

from mpl_toolkits.basemap import Basemap
from settings import *


class Region:
    """
    lcrnrlon: longitude of lower left hand corner of the desired map domain (degrees).
    llcrnrlat: latitude of lower left hand corner of the desired map domain (degrees).
    urcrnrlon: longitude of upper right hand corner of the desired map domain (degrees).
    urcrnrlat: latitude of upper right hand corner of the desired map domain (degrees).
    """
    def __init__(self, lat_column, lon_column):
        self.lat_column = lat_column
        self.lon_column = lon_column
        self.latitudes = []
        self.longitudes = []
        self.parallels = []
        self.meridians = []

    def create_map_object(self, data):
        self.latitudes = data[:,2]
        self.longitudes = data[:,3]
        lat_min = LAT_MIN
        lat_max = LAT_MAX
        lon_min = LON_MIN
        lon_max = LON_MAX
        map = Basemap(llcrnrlat=lat_min, urcrnrlat=lat_max,\
            llcrnrlon=lon_min, urcrnrlon=lon_max, resolution='l')
        self.parallels = numpy.linspace(lat_min, lat_max, 5)
        self.meridians = numpy.linspace(lon_min, lon_max, 5)
        return (map)

    def plot_locations(self, map):
        plot.figure()
        # map.drawcoastlines(linewidth=1)
        # map.drawcountries(linewidth=1)
        x,y = map(self.longitudes, self.latitudes)
        map.plot(x, y, 'or', markersize=3)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        # map.bluemarble()
        map.etopo()
        plot.title('Earthquakes locations')

    def plot_depths(self, map, data):
        plot.figure()
        # map.drawcoastlines(linewidth=1)
        # map.drawcountries(linewidth=1)
        x,y = map(self.longitudes, self.latitudes)
        colors = map.scatter(
            x, y, marker='o', s=80, lw=0, c=data[:,4], cmap=plot.cm.jet)
        plot.colorbar(colors)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        map.etopo()
        plot.title('Earthquakes depth')

    def plot_magnitudes(self, map, data):
        plot.figure()
        # map.drawcoastlines(linewidth=1)
        # map.drawcountries(linewidth=1)
        x, y = map(self.longitudes, self.latitudes)
        min_size = 20
        mag_size = data[:,5]*min_size
        colors = map.scatter(
            x, y, marker='o', s=mag_size, lw=0, c=data[:, 5], cmap=plot.cm.jet)
        plot.colorbar(colors)
        map.drawparallels(self.parallels, labels=[False,True,True,False])
        map.drawmeridians(self.meridians, labels=[True,False,False,True])
        map.etopo()
        plot.title('Earthquakes magnitudes')