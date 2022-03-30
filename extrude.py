
import bpy
'''
loc_y = 0.0
#for data in (1.0, 0.5, 0.25, 0.1, 0.01):
for data in (1,1):
    # Add the cube to the scene and get it
    bpy.ops.mesh.primitive_cube_add(location=(0.0, loc_y, 0.0))
    cube = bpy.context.object
    #select an edge
    
    # Add the bevel modifier
    bevel_mod = cube.modifiers.new(name="MY-Bevel", type='BEVEL')
    bevel_mod.width = 0.25 #ata
    bevel_mod.segments = 10
    # Offset the initial location
    loc_y += 3.0
import bpy
import math
import bmesh

bpy.ops.mesh.primitive_cube_add(location=(1,0,3), size = 1) # === create a cube
#Passer en mode édition.
bpy.ops.object.mode_set(mode='EDIT')
#Désélectionner tous les maillages.
bpy.ops.mesh.select_all(action='DESELECT'
#Passer en mode visage,Un côté...oshidashi
#Mettre en mode visage.
bpy.ops.mesh.select_mode(type="EDGE")

#Instanciation d'objet Bmesh.
b_mesh = bmesh.from_edit_mesh(bpy.context.object.data)
b_mesh.faces.ensure_lookup_table()
b_mesh.faces[1].select = True # ===  face number (3) south face 

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":[ -1.0 , 1.0 , -
'''
'''
bevel_amounts = [1.0, 0.5]
loc_x = 0.0
loc_y = 0.0
offset = 3.0
items_row = 7

'''

import bpy
import math
import bmesh
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0,0,0), scale=(1,1,1))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_mode(type="FACE")
b_mesh = bmesh.from_edit_mesh(bpy.context.object.data)
b_mesh.faces.ensure_lookup_table()
b_mesh.faces[3].select = True 
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":[ 0 , -1.0, 0.0]} )


'''
    cube = bpy.context.object
    # Add the bevel modifier
    bevel_mod = cube.modifiers.new(name="MY-Bevel", type='BEVEL')
    bevel_mod.width = data
    # Offset the initial location
    loc_y += offset
    # Add a new row 
    if i % items_row == 0:
        loc_x += offset
        # Reset y
        loc_y = 0.01.0]} )
'''
'''
bevel = obj.modifiers.new('Bevel', 'BEVEL')
bevel.segments = 10
bevel.width = roundness / 10
'''

#select edge make edge active not just selected
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
#bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_mode(type="EDGE")
#bpy.ops.mesh.select_mode(type="FACE")

bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
#obj.data.vertices[2].select = True
obj.data.edges[6].select = True
#obj.data.polygons[0].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 

me = bpy.context.object.data
bm = bmesh.from_edit_mesh(me)

edge = bm.edges[1]

edge.select = True  # select the element before making it active

bm.select_history.clear()  # optionally clear previous elements
bm.select_history.add(edge)

bmesh.update_edit_mesh(me)

bpy.ops.object.modifier_set_active(modifier="Bevel")
bpy.ops.object.modifier_add(type='BEVEL')

'''
bpy.context.object.modifiers["Bevel"].segments = 10
'''
'''
#clear scene, make mesh
bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 2), rotation=(1.5708, 1.5708, 0))
#obj = bpy.data.objects["Plane"]
obj = bpy.data.objects["Cube"]

#select vertex
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
#bpy.ops.mesh.select_mode(type="VERT")
#bpy.ops.mesh.select_mode(type="EDGE")
bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
#obj.data.vertices[3].select = True
#obj.data.edges[3].select = True
obj.data.faces[0].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 
'''

'''
#select vertex
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
#bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_mode(type="EDGE")
#bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
#obj.data.vertices[2].select = True
#obj.data.edges[9].select = True
obj.data.polygons[2].select = True
bpy.ops.object.mode_set(mode = 'EDIT') 
'''

bpy.context.object.scale[0] = 1
bpy.context.object.scale[1] = 1
bpy.context.object.scale[2] = 1

bpy.context.active_object.rotation_euler[0] = math.radians(45)

