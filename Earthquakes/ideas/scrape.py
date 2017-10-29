# import requests
# api_key = 'd82c24988d55220511f4e1335a124017'
# url = 'http://api.openweathermap.org/data/2.5/weather?id=2172797&APPID=' + api_key
# r = requests.get(url)
# print (r.json())



import urllib2
from bs4 import BeautifulSoup

# What year?
year = 2016

# htps://www.wunderground.com/history/airport/LEST/2017/10/24/DailyHistory.html

# Create a file with the data
file = open('santiago-data-' + str(year) + '.txt', 'w')
file.write('date,tmean,tmax,tmin,precipitation\n')

# Iterate through the months and days to have the daily data
for month in range(1, 2):
# for month in range(1, 13):
    for day in range(1, 32):

        # Check if data of month is retrieved
        if (month == 2 and day > 28):
            break
        elif (month in [4, 6, 9, 11] and day > 30):
            break

        # Open url
        datestamp = str(year) + '-' + str(month) + '-' + str(day)
        url = 'http://www.wunderground.com/history/airport/LEST/' + str(year) + '/' + str(month) + '/' + str(
            day) + '/DailyHistory.html'
        page = urllib2.urlopen(url)

        # Get history table
        soup = BeautifulSoup(page)
        historyTable = soup.find('table', id='historyTable')
        # spans = historyTable.find_all(attrs={'class': 'nobr'})
        spans = historyTable.find_all(attrs={'class': 'wx-data'})

        # Get mean temperatures from page
        tmean = spans[0].span.string
        tmax = spans[1].span.string
        tmin = spans[2].span.string

        # Get precip from page
        precip = spans[9].span.string

        # Get dewpoint from page
        dewpoint = spans[8].span.string

        # Format month for datestamp
        if len(str(month)) < 2:
            mStamp = '0' + str(month)
        else:
            mStamp = str(month)

        # Format day for datestamp
        if len(str(day)) < 2:
            dStamp = '0' + str(day)
        else:
            dStamp = str(day)

        # Build timestamp
        datestamp = str(year) + mStamp + dStamp

        # Write timestamp and temperature to file
        print
        tmean + ':' + tmax + ':' + tmax + ':' + precip + ':' + dewpoint
        file.write(datestamp + ',' + tmean + ',' + tmax + ',' + tmin + ',' + precip + ',' + dewpoint + '\n')

# Done getting data! Close file.
file.close()