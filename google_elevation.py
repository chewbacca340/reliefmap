#!/usr/bin/python

import sys
print(sys.argv[1:])

api_key = sys.argv[1]

#URLs must be properly encoded to be valid and are limited to 8192
#(e.g. "40.714728,-73.998672") or multiple latitude/longitude pairs passed as an array or as an encoded polyline. There is a 512 point limit for this specific parameter
#An array of coordinates separated using the pipe ('|') character: locations=40.714728,-73.998672|-34.397,150.644


#bottom right = 29.186784154260742, -102.93127864997342
#top 29.713857422799144, -103.05486403175581
#left 29.57391378812287, -104.43158817157901

#overall latitude from 29.186784154260742 to 29.713857422799144
#overall longitude from -102.93127864997342 to -104.43158817157901

#90.3 miles bottom left to bottom right
#36.46 miles top to bottom

#0.527073269
#-1.500309522




# how many points should we get left to right
# what is the size of the bed
#220mm
#nozzle is 0.4mm
#means we have approx 550 elements of resolution
#each latitude step:
#0.000958315
#each longitude step:
#-0.002727835



# is the left-right distance the same as the bottom-top distance?

#cost is $5.00 per thousand requests

#looks like we can do about 198 locations per request to stay under the 8192 character limit
#that would mean about 1,500 requests


"""
var rad = function(x) {
  return x * Math.PI / 180;
};

var getDistance = function(p1, p2) {
  var R = 6378137; // Earth’s mean radius in meter
  var dLat = rad(p2.lat() - p1.lat());
  var dLong = rad(p2.lng() - p1.lng());
  var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(rad(p1.lat())) * Math.cos(rad(p2.lat())) *
    Math.sin(dLong / 2) * Math.sin(dLong / 2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var d = R * c;
  return d; // returns the distance in meter
};
"""


import requests

url = "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536%2C-104.9847034&key=" + api_key


url = "https://maps.googleapis.com/maps/api/elevation/json?locations=29.186784154260742%2C-102.93127864997342|40.7391536%2C-103.9847034&key=" + api_key

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


