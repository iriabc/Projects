from seismicModel import *

file_name='seismicData.csv'
data = numpy.genfromtxt(file_name, delimiter=',', usecols=(0,1,2,3,4))

# Instanciate the mapRegion class
region = Region(lat_column = 1, lon_column = 2)

# Create basemap object from file and load lat and long
map = region.create_map_object(data)

# Map with stations
region.plot_geographic_points(map)

#Now plot the stations
# WORLD.map_stations(m)
# plt.title('Map of stations')
# WORLD.map_values(m,data[:,3])
# plt.title('Depth Map')
# WORLD.map_values_symbol_size(m,data[:,4])
# plt.title('Magnitude Map')
# l=WORLD.zoom_in(0,80,-180,-30,m)
# WORLD.map_values_symbol_size(l,data[:,4])

plot.show()

# WORLD == earthMap
# m == map