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
lat_initial = 29.18678415426074
long_initial = -102.9312786499734

lat_con = 116027.360237003
long_con = -96540.479090579




loaded_list = []


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
# adding initiallong to currentlong, then multiplying by conversion factor

print([loaded_list[0]['elevation'],loaded_list[0]['location']['lat'],loaded_list[0]['location']['lng']])

transformed_list = [[i['elevation'],i['location']['lat'],i['location']['lng']] for i in loaded_list]



    
export_list = [[i[0],(i[1] - lat_initial) * lat_con,(i[2] - long_initial) * long_con] for i in transformed_list]
    
    
    
    
    
    
    
    

