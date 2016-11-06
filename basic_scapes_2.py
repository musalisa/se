import svgwrite
import math

#grado_z = 180 - AOHOR
grado_z = 180
cx = 350
cy = 350
z1 = 200
z2 = 300

from svgwrite import cm, mm   
    
def basic_shapes(name):
	dwg = svgwrite.Drawing(filename=name, debug=True)
	zlines = dwg.add(dwg.g(id='zlines', stroke='green'))
	for i in range(0, 360, 30):
		zlines.add(dwg.line( start=((math.cos(math.radians(grado_z+i)) * z1) + cx, (math.sin(math.radians(grado_z+i)) * -z1) + cy), end=((math.cos(math.radians(grado_z+i)) * z2) + cx, (math.sin(math.radians(grado_z+i)) * -z2) + cy)))
	dwg.save()

if __name__ == '__main__':
    basic_shapes('basic_shapes.svg')
