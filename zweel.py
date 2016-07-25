import svgwrite
import math

global epsilon
epsilon = 23.45

### CARTA Z #################################
grado_z = 180
cx = 350
cy = 350
r0 = 320
r1 = 300
r2 = 200
r4 = 310
grado_z = 180 
dwg = svgwrite.Drawing('zweel.svg', profile = 'tiny')
w0 = svgwrite.shapes.Circle(center=(cx,cy), r=r0, stroke_width = 2, stroke = "black", fill = "white")
w1 = svgwrite.shapes.Circle(center=(cx,cy), r=r1, stroke_width = 2, stroke = "black", fill = "white")
w2 = svgwrite.shapes.Circle(center=(cx,cy), r=r2, stroke_width = 2, stroke = "black", fill = "white")
dwg.add(w0)
dwg.add(w1)
dwg.add(w2)

### gradi #############
zlines = dwg.add(dwg.g(id='zlines', stroke='black',  stroke_width = 2))
for i in range(0, 360, 30):
		zlines.add(dwg.line( start=((math.cos(math.radians(grado_z+i)) * r0) + cx, (math.sin(math.radians(grado_z+i)) * -r0) + cy), end=((math.cos(math.radians(grado_z+i)) * r2) + cx, (math.sin(math.radians(grado_z+i)) * -r2) + cy)))
for i in range(0, 360, 10):
		zlines.add(dwg.line( start=((math.cos(math.radians(grado_z+i)) * r0) + cx, (math.sin(math.radians(grado_z+i)) * -r0) + cy), end=((math.cos(math.radians(grado_z+i)) * r1) + cx, (math.sin(math.radians(grado_z+i)) * -r1) + cy)))
for i in range(0, 360, 2):
		zlines.add(dwg.line( start=((math.cos(math.radians(grado_z+i)) * r4) + cx, (math.sin(math.radians(grado_z+i)) * -r4) + cy), end=((math.cos(math.radians(grado_z+i)) * r1) + cx, (math.sin(math.radians(grado_z+i)) * -r1) + cy)))

### gradi #############
signs = dwg.add(dwg.g(id='signs', stroke='black',  stroke_width = 2, fill = 'white'))
grado_z = 195 
for i in range(0, 360, 30):
		signs.add(dwg.circle(center=((math.cos(math.radians(grado_z+i)) * r0) + cx, (math.sin(math.radians(grado_z+i)) * -r0) + cy), r=20))




dwg.save()

