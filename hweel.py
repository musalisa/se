import svgwrite
import math

global epsilon
epsilon = 23.45

### CARTA Z #################################
rz1 = 200
rz2 = 300
rz3 = 320
rdz1 = rz2 + (rz3 - rz2)/2
dwg = svgwrite.Drawing('images/case.svg', profile = 'tiny')
zodiac = dwg.add(dwg.g(id='zodiac', stroke='black',  stroke_width = 2, fill = "white"))
zodiac.add(dwg.circle(center=(0,0), r=rz3  ))
zodiac.add(dwg.circle(center=(0,0), r=rz2  ))
zodiac.add(dwg.circle(center=(0,0), r=rz1  ))

### confini segni #############
for i in range(0, 360, 30):
	zodiac.add(dwg.line( start=((math.cos(math.radians(i)) * rz1) , (math.sin(math.radians(i)) * rz1) ), end=((math.cos(math.radians(i)) * rz3) , (math.sin(math.radians(i)) * rz3) )))
### decani #############
for i in range(0, 360, 10):
	zodiac.add(dwg.line( start=((math.cos(math.radians(i)) * rz2) , (math.sin(math.radians(i)) * rz2) ), end=((math.cos(math.radians(i)) * rz3) , (math.sin(math.radians(i)) * rz3) )))
### gradi #############
for i in range(0, 360, 2):
	zodiac.add(dwg.line( start=((math.cos(math.radians(i)) * rz2) , (math.sin(math.radians(i)) * rz2) ), end=((math.cos(math.radians(i)) * rdz1) , (math.sin(math.radians(i)) * rdz1) )))
#### segni ########### 
for i in range(0, 45, 30):
	zodiac.add(dwg.circle(center=((math.cos(math.radians(i)) * rz3) , (math.sin(math.radians(i)) * rz3) ), r=30))
dwg.save()

