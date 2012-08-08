

import time
import csv
import json
from BeautifulSoup import BeautifulSoup
import mechanize
import random
'''
magic = 60
magic2 = 15
radius = 5;

#http://stackoverflow.com/questions/8362255/get-type-of-terrain-by-coordinate

#extract elevation from json
def getCity(m):
    try:
        return m['results'][0]['formatted_address'].split(',')[1].strip()    
    except:
        return


br = mechanize.Browser()
br.set_handle_robots(False)

coords = csv.reader(open('weatherCoords.csv', "r" ))
w = csv.writer(open('weatherCities.csv', "wb" ))
cities = {}


for coord in coords:
    time.sleep(.25)
    lat, lng = coord[0],coord[1]
    url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+lat+','+lng+'&sensor=true'
    print lat,lng,url
    page = br.open(url)
    html = page.read()
    m = json.loads(html)
    city = getCity(m)
    print city,lat,lng,url
    key = (lat+lng).strip()
    cities[key] = city
    w.writerow([lat,lng,city])
'''
w = csv.reader(open('weatherCities.csv', "r" ))
cities = {}
for line in w:
    key = (line[0]+line[1]).strip()
    cities[key] = line[2]




data = csv.reader(open('weather_Data2.csv', "r" ))

w = csv.writer(open('weatherCityNames.csv', "wb" ))

for line in data:
    key = (line[2]+line[3]).strip()
    try:
        new_line = [cities[key]] + line
    except:
        new_line = ['unknown']+ line
    w.writerow(new_line)
print 'done'

