import svgwrite
import math

global epsilon
epsilon = 23.45

### CARTA Z #################################
grado_z = 180
rz1 = 200
rz2 = 300
rz3 = 320
dz1 = rz3 - rz2
grado_z = 0 
dwg = svgwrite.Drawing('zweel.svg', profile = 'tiny')
zodiac = dwg.add(dwg.g(id='zodiac', stroke='black',  stroke_width = 2, fill = "white"))
zodiac.add(dwg.circle(center=(0,0), r=rz3  ))
zodiac.add(dwg.circle(center=(0,0), r=rz2  ))
zodiac.add(dwg.circle(center=(0,0), r=rz1  ))

### segni #############
for i in range(0, 360, 30):
	zodiac.add(dwg.line( start=((math.cos(math.radians(i)) * rz1) , (math.sin(math.radians(i)) * rz1) ), end=((math.cos(math.radians(i)) * rz3) , (math.sin(math.radians(i)) * rz3) )))
### decani #############
for i in range(0, 360, 10):
	zodiac.add(dwg.line( start=((math.cos(math.radians(i)) * rz2) , (math.sin(math.radians(i)) * rz2) ), end=((math.cos(math.radians(i)) * rz3) , (math.sin(math.radians(i)) * rz3) )))
#for i in range(0, 360, 2):
#		zlines.add(dwg.line( start=((math.cos(math.radians(grado_z+i)) * r4) , (math.sin(math.radians(grado_z+i)) * r4) ), end=((math.cos(math.radians(grado_z+i)) * r1) , (math.sin(math.radians(grado_z+i)) * r1) )))
#
### gradi #############
#signs = dwg.add(dwg.g(id='signs', stroke='black',  stroke_width = 2, fill = 'white'))
#grado_z = 15 
#for i in range(0, 30, 30):
#		signs.add(dwg.circle(center=((math.cos(math.radians(grado_z+i)) * r0) , (math.sin(math.radians(grado_z+i)) * r0) ), r=20))
#



dwg.save()

