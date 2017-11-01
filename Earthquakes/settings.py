import datetime
# import sys


# API
BASE_URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
FORMAT = 'geojson'

DATE_0 = datetime.date(1970, 1, 1)


# Seismic data period
START_DATE = '2017-01-01'
END_DATE = '2017-01-05'
# START_DATE=sys.argv[1]
# END_DATE=sys.argv[2]


# Map region limits
LAT_MIN = -90
LAT_MAX = 90
LON_MIN = -180
LON_MAX = 180


#Database settings
USER = 'demo'
PASSWORD = '1A34NS453F~ss4JH2FHFJ'
DB_NAME = 'earthquakes'
