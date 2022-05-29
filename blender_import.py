import bpy
import csv
import bmesh
from operator import itemgetter

csvfile_path = 'D:\\Code\\reliefmap\\pickle_files\\relief_map_xyz.csv'
base = 2000.0
#csvfile = open(csvfile_path)

with open(csvfile_path, newline='\r\n') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    vertices_import = list(reader)

max_x = max([float(i[1]) for i in vertices_import])
max_x_next = max([float(i[1]) for i in vertices_import if float(i[1]) != max_x])
print(max_x)
print(max_x_next)
max_y = max([float(i[2]) for i in vertices_import])
print(len(vertices_import))
vertices_import = [i for i in vertices_import if float(i[1]) != max_x]
print(len(vertices_import))
max_x = max_x_next
vertices_import = vertices_import.copy()

#print(len(vertices_import))
#print(vertices_import[0])


#csvfile.seek(0)
#inFile = csv.reader(csvfile, delimiter=',', quotechar='"')

#Read and sort the vertices coordinates (sort by x and y)
#vertices = sorted( [(float(r[0]), float(r[1]), float(r[2])) for r in inFile], key = itemgetter(0,1) )

vertices = sorted( [(float(r[1])/1000, float(r[2])/1000, float(r[0])/1000) for r in vertices_import], key = itemgetter(0,1) )
vertices_grid = vertices.copy()
#********* Assuming we have a rectangular grid *************
xSize = next( i for i in range( len(vertices) ) if vertices[i][0] != vertices[i+1][0] ) + 1 #Find the first change in X
ySize = len(vertices) // xSize

#Generate the polygons (four vertices linked in a face)
polygons = [(i, i - 1, i - 1 + xSize, i + xSize) for i in range( 1, len(vertices) - xSize ) if i % xSize != 0]

name = "grid_main"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object

obj.data.from_pydata( vertices, [], polygons ) #Associate vertices and polygons

#obj.scale = (1, 5, 0.2) #Scale it (if needed)
for p in obj.data.polygons: #Set smooth shading (if needed)
    p.use_smooth = True

bpy.context.collection.objects.link( obj )



"""    
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.rotation_euler[0] = 1.5708
bpy.context.object.location[1] = -0.24
bpy.context.object.location[2] = 0.12 
bpy.context.object.location[0] = 30.577
bpy.context.object.scale[0] = 30.837

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.rotation_euler[0] = 1.5708
bpy.context.object.location[1] = 145.07
bpy.context.object.location[2] = 0.12 
bpy.context.object.location[0] = 30.577
bpy.context.object.scale[0] = 30.837

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.rotation_euler[0] = 1.5708
bpy.context.object.rotation_euler[1] = 1.5708
bpy.context.object.rotation_euler[2] = 1.5708
bpy.context.object.scale[1] = 72.68
bpy.context.object.location[1] = 72.42
bpy.context.object.location[2] = 0.12 
bpy.context.object.location[0] = -0.29

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.rotation_euler[0] = 1.5708
bpy.context.object.rotation_euler[1] = 1.5708
bpy.context.object.rotation_euler[2] = 1.5708
bpy.context.object.scale[1] = 72.68
bpy.context.object.location[1] = 72.42
bpy.context.object.location[2] = 0.12 
bpy.context.object.location[0] = 61.41

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.scale[0] = 30.577
bpy.context.object.scale[1] = 72.68
bpy.context.object.location[0] = 30.577
bpy.context.object.location[1] = 72.42
bpy.context.object.location[2] = -0.8

bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'OBJECT'
bpy.context.object.scale[0] = 30.577
bpy.context.object.scale[1] = 72.68
bpy.context.object.location[0] = 30.577
bpy.context.object.location[1] = 72.42
bpy.context.object.location[2] = 1.1
"""




# create plane floor
vertices = [(0.0,  0.0,  -base/1000), 
            (max_x/1000, 0.0,  -base/1000),
            (max_x/1000, max_y/1000,  -base/1000),
            (0.0,  max_y/1000,  -base/1000),
           ]
edges = []
faces = [[0,1,2,3]]

print(len(vertices))
print(faces)
print(type(vertices))
name = "plane_floor"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )


# create one side
top_edge = [i for i in vertices_import if round(float(i[1]),5) ==  round(max_x,5)]

#top_edge.append([944.544921875,max_x,max_y])
#top_edge.extend([i for i in vertices_import if round(float(i[1]),5) ==  round(max_x,5)])


vertices = sorted( [(float(r[1])/1000, float(r[2])/1000, float(r[0])/1000) for r in top_edge], key = itemgetter(1,2,0) )
print('vertices should be 550.  actual : ' + str(len(vertices)))

vertices.append([max_x/1000, max_y/1000, -base/1000])
vertices.append([max_x/1000, 0.0, -base/1000])

edges = []
faces = [[i for i, _ in enumerate(vertices)]]
name = "side1"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )

# create another side
top_edge = [i for i in vertices_import if round(float(i[1]),5) ==  round(0,5)]



vertices = sorted( [(float(r[1])/1000, float(r[2])/1000, float(r[0])/1000) for r in top_edge], key = itemgetter(0,1,2) )
print('vertices should be 550.  actual : ' + str(len(vertices)))

vertices.append([0.0, max_y/1000, -base/1000])
vertices.append([0.0, 0.0, -base/1000])

edges = []
faces = [[i for i, _ in enumerate(vertices)]]
name = "side2"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )

# create a third side
top_edge = [i for i in vertices_import if round(float(i[2]),5) ==  round(max_y,5)]


vertices = sorted( [(float(r[1])/1000, float(r[2])/1000, float(r[0])/1000) for r in top_edge], key = itemgetter(0,1,2) )
print('vertices should be 550.  actual : ' + str(len(vertices)))

vertices.append([max_x/1000,max_y/1000,-base/1000])
vertices.append([0.0,max_y/1000,-base/1000])

edges = []
faces = [[i for i, _ in enumerate(vertices)]]
name = "side3"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )

print(vertices[len(vertices)-2])

# create a fourth side
top_edge = [i for i in vertices_import if round(float(i[2]),5) ==  round(0,5)]


vertices = sorted( [(float(r[1])/1000, float(r[2])/1000, float(r[0])/1000) for r in top_edge], key = itemgetter(0,1,2) )
print('vertices should be 550.  actual : ' + str(len(vertices)))

vertices.append([max_x/1000,0.0,-base/1000])
vertices.append([0.0,0.0,-base/1000])

edges = []
faces = [[i for i, _ in enumerate(vertices)]]
name = "side4"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )


"""
vertices = [(0.0,  0.0,  -base/1000), 
            (0.0, 0.0,  .56),
            (max_x/1000, 0.0,  0.77),
            (max_x/1000,  0.0,  -base/1000),
           ]
edges = []
faces = [[i for i, _ in enumerate(vertices)]]
name = "side4_v2"
mesh = bpy.data.meshes.new( name ) #Create the mesh (inner data)
obj = bpy.data.objects.new( name, mesh ) #Create an object
obj.data.from_pydata(vertices, edges, faces)
bpy.context.collection.objects.link( obj )
"""


"""
bpy.context.space_data.context = 'MATERIAL'

bpy.ops.material.new()

bpy.context.object.active_material.diffuse_color = (0, 0, 1, 1)
"""
