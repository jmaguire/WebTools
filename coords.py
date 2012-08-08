import time
import csv
import json
from BeautifulSoup import BeautifulSoup
import mechanize

def getLatLong(m):
    lat = m['results'][0]['geometry']['location']['lat']
    lng = m['results'][0]['geometry']['location']['lng']
    return lat, lng


br = mechanize.Browser()
br.set_handle_robots(False)

city_doc = csv.reader(open('cities.csv', "r" ))
w = csv.writer(open('city_coords.csv', "wb" ))
cities = []

for city in city_doc:
    city = city[0]
    time.sleep(.5)
    name = city +', CA'
    url = "http://maps.googleapis.com/maps/api/geocode/json?address= " + name + "&sensor=true"
    url = url.replace(" ","%20")
    print url
    
    page = br.open(url)
    html = page.read()
    map = json.loads(html)
    lat, long = getLatLong(map)
    print city,lat,long
    w.writerow([city,lat,long])