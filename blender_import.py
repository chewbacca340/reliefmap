# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:28:46 2022

@author: brayd
"""

import bpy
import csv
from operator import itemgetter

csvfile_path = 'D:\\Code\\reliefmap\\pickle_files\\relief_map_xyz.csv'
#csvfile = open(csvfile_path)

with open(csvfile_path, newline='\r\n') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    vertices_import = list(reader)

print(len(vertices_import))
print(vertices_import[0])


#csvfile.seek(0)
#inFile = csv.reader(csvfile, delimiter=',', quotechar='"')

#Read and sort the vertices coordinates (sort by x and y)
#vertices = sorted( [(float(r[0]), float(r[1]), float(r[2])) for r in inFile], key = itemgetter(0,1) )

vertices = sorted( [(float(r[0]), float(r[1]), float(r[2])) for r in vertices_import], key = itemgetter(0,1) )

#********* Assuming we have a rectangular grid *************
xSize = next( i for i in range( len(vertices) ) if vertices[i][0] != vertices[i+1][0] ) + 1 #Find the first change in X
ySize = len(vertices) // xSize

#Generate the polygons (four vertices linked in a face)
polygons = [(i, i - 1, i - 1 + xSize, i + xSize) for i in range( 1, len(vertices) - xSize ) if i % xSize != 0]

name = "grid"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object

obj.data.from_pydata( vertices, [], polygons ) #Associate vertices and polygons

#obj.scale = (1, 5, 0.2) #Scale it (if needed)
for p in obj.data.polygons: #Set smooth shading (if needed)
    p.use_smooth = True

#bpy.context.scene.objects.link( obj ) #Link the object to the scene

bpy.context.collection.objects.link( obj )


#newCol = bpy.data.collections.new('relief_map')
#bpy.context.scene.collections.children.link(newCol)
#newCol.objects.link(obj)

