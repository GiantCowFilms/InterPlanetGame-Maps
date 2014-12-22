import bpy
import json

'''

Chage dimensions of object 'size' to chage the map size. Edit the text of object 'name' to change the map name.

Duplicate circles, which are currently valid sizes, and position them inside the rectangle. The custom property 'startValue' for each circle is the start value. A circle's x and y location is its x and y coordinate while its scale is its radius. A circle's material, which is converted to hexadecimal, is its color.

If a circle is ouside the rectangle has an invalid color, radius, or startValue, it will not be included in the map. It does not check if circles overlap, since that is not in the specification.

Select the circles to include in the map and run the script to put the json on the clipboard.
'''

acceptedColors = {
    'Green':'#8ed16c',
    'Blue': '#3fa6f3',
    'Red': '#e25f5f',
    'Magenta': '#ef6ab8',
    'Neutral Grey': '#bbbbbb'
}
acceptedSizes = [10, 15, 20, 40, 50, 75, 100, 125, 150, 175, 200]
acceptedStartValues = [5, 10, 15, 20, 25, 30, 35, 45, 50, 60, 70, 75, 80, 90, 100, 125]

size = bpy.data.objects['size']

width = round(size.dimensions.x)
height = round(size.dimensions.y)

map = {
    'name': bpy.data.objects['name'].data.body,
    'size': {
        'x': str(width),
        'y': str(height)
    },
    'planets': []
}

for object in bpy.context.selected_objects:
	startValue = object['startValue']
	
	# round all numbers to integers
	color = object.active_material.name
	radius = round(object.scale.x)
	x = round(object.location.x)
	y = height - round(object.location.y)
	
	# skip unaccepted colors
	if color not in acceptedColors:
	    continue
	
	color = acceptedColors[color]
	
	# skip if the circle is outside the size
	if x < radius or x > width - radius or y < radius or y > height - radius:
	   continue
	
	# skip unaccepted start values
	if (startValue not in acceptedStartValues):
		continue;
	
	map['planets'].append({
	    'color': color,
	    'radius': str(radius),
	    'x': str(x),
	    'y': str(y),
	    'startValue': str(startValue)
	})
	
bpy.context.window_manager.clipboard = json.dumps(map)
