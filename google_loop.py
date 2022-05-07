# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:28:03 2022

@author: brayd
"""
import os
import requests
import pickle

api_key = os.environ["gapi"]
url_start = "https://maps.googleapis.com/maps/api/elevation/json?locations="
url_end = "&key=" + api_key

lat = 29.186784154260742
long = -102.93127864997342
long_initial = -102.93127864997342

final_lat = 29.713857422799144
final_long = -104.43158817157901

lat_inc = 0.000958315
long_inc = -0.002727835
i = 0
i_apicalls = 0
url_pairs = url_start + ""

print((final_lat-lat)/lat_inc)
print((final_long-long)/long_inc)

def getUrlPairs(url_pairs):
    url = url_pairs[:-1] + url_end
    print(len(url))
    print(i)

    filename = 'D:/Code/reliefmap/pickle_files\gapi_' + str(i).zfill(5) + '.pkl'
    outfile = open(filename,'wb')
    #saves to dictionary
    r = requests.get(url_pairs[:-1] + url_end)
    
    #prints only the results as dictionary
    #r.json()["results"]
    pickle.dump(r.json()["results"],outfile)
    outfile.close()


    
    
while lat < final_lat:

    while long > final_long:

        
        i = i + 1
        
        if len(url_pairs + str(lat) + "%2C" + str(long) + url_end) >= 8192-130:
            getUrlPairs(url_pairs)

            i_apicalls = i_apicalls + 1
            url_pairs = url_start + ""

        url_pairs = url_pairs + str(lat) + "%2C" + str(long) + "|"
        long = long + long_inc
    lat = lat + lat_inc
    long = long_initial
print(lat)
print(long)
print(i_apicalls)
