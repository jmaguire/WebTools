import time
import csv
import json
from BeautifulSoup import BeautifulSoup
import mechanize
import random

magic = 60
magic2 = 15
radius = 5;

#http://stackoverflow.com/questions/8362255/get-type-of-terrain-by-coordinate

#extract elevation from json
def getElevation(m):
    elevation = []
    for i in range(len(m['results'])):
        elevation.append(m['results'][i]['elevation'])
    return elevation

def randomPoints(lat,lng):
    string = str(lat)+ ',' + str(lng)
    for i in range(magic):
        #random displacement by -5 to +5 miles
        dx = (random.random()*2-1)*.02*radius
        dy = (random.random()*2-1)*.0145*radius
        lat_new = dx+lat
        lng_new = dy+lng
        string += '|'+str(lat_new)+','+ str(lng_new) #format for google api
    return string

def makeMetric(elevations):
    metric = 0;
    adjusted = [] #grab points above sea level
    for point in elevations:
        if len(adjusted) >= magic2:
            break
        if point > 0:
            adjusted.append(point)
    if len(adjusted) < magic2:
            print 'FUCKING SEA'
    for i in range(len(adjusted)):
        for j in range(i+1,len(adjusted)):   
            metric += abs(adjusted[i]-adjusted[j])
    return metric

br = mechanize.Browser()
br.set_handle_robots(False)

city_doc = csv.reader(open('city_coords.csv', "r" ))
w = csv.writer(open('elevation2.csv', "wb" ))
cities = []
titles = ['city']

for i in range(magic):
    titles.append('height '+str(i+1))
titles.append('metric')
w.writerow(titles)

for city in city_doc:
    time.sleep(.25)
    city, lat, lng = city[0],city[1],city[2]
    coords = randomPoints(float(lat),float(lng))
    url = 'http://maps.googleapis.com/maps/api/elevation/json?locations=' + coords+ '&sensor=true'
    print city,url
    page = br.open(url)
    html = page.read()
    m = json.loads(html)
    elevations = getElevation(m)
    w.writerow([city] + elevations + [makeMetric(elevations)])
