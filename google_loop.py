# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:28:03 2022

@author: brayd
"""
api_key = ""
url_start = "https://maps.googleapis.com/maps/api/elevation/json?locations="
url_end = "=" + api_key

lat = 29.186784154260742
long = -102.93127864997342

final_lat = 29.713857422799144
final_long = -104.43158817157901

lat_inc = 0.000958315
long_inc = -0.002727835

url_pairs = url_start + ""
def getUrlPairs(url_pairs):
    url = url_pairs + url_end
    print(url)

while lat < final_lat:
    lat = lat + lat_inc
    
    while long > final_long:
        long = long + long_inc
         
        if len(url_pairs + str(lat) + "%2c" + str(long) + url_end) >= 8192-100:
            getUrlPairs(url_pairs)
            url_pairs = url_start + ""

        url_pairs = url_pairs + str(lat) + "%2c" + str(long) + "|"
  