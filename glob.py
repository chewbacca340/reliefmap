# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#This file is to glob.  I will come back later.

import pickle



number = 00195
path = 'D:\\Code\\reliefmap\\pickle_files'
i = 0

loaded_list = []
file_name = path + '\\gapi_' + str(number) + '.pkl'

#while number <= 303523:
#    open_file = open(file_name, 'rb')
#    loaded_list.extend(pickle.load(open_file))
#    open_file.close()
#    number += 1

open_file = open(file_name, 'rb')
loaded_list.extend(pickle.load(open_file))
open_file.close()

print(loaded_list)