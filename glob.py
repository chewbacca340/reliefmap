# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#This file is to glob.  I will come back later.

import pickle
import glob, os




path = 'D:\\Code\\reliefmap\\pickle_files'
i = 0


loaded_list = []
#file_name = path + '\\gapi_' + str(number) + '.pkl'

os.chdir(path)
for file in glob.glob('*.pkl'):
    print(file)


for file in glob.glob('*.pkl'):
    print(file)
    open_file = open(file, 'rb')
    loaded_list.extend(pickle.load(open_file))
    open_file.close()

#open_file = open(file_name, 'rb')
#loaded_list.extend(pickle.load(open_file))
#open_file.close()

print(len(loaded_list))

#iterate through list of lists that have elevation, locationlat, locationlong, 
#converting lat and long to meters by subracting initiallat from currentlat and
# adding initiallong to currentlong, then dividing by conversion factor

print([loaded_list[0]['elevation'],loaded_list[0]['location']['lat'],loaded_list[0]['location']['lng']])