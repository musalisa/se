import os
import math
AOHOR = 322.9624
ARMC = 232.9624
DHSORTE = 4.3956

file = open("stelle_esercizio_20.txt","r")
#os.rename("prova.txt", "prova1.txt")
new_file = open( "res.txt", "w")
for line in file:
	lineSplit = line.split()
	alfa = float( lineSplit[1] )
	delta = float( lineSplit[3] )
	deltaRad = math.radians( delta )
	latitRad = math.radians( 45.467 )
	deltaTan = math.tan( deltaRad ) * math.tan( latitRad )
	deltaTanRad = math.radians( deltaTan )
	#DARad = math.asin( math.radians( math.tan( deltaTan ) * math.tan( latitRad ) ) )
	DA = abs( math.degrees( math.asin( deltaTan ) ) )
	#DA = 0
	#new_file.write( str(delta) + ' - ' + str(deltaRad) + ' - ' + str( DARad ) + '\n' )
	if ( alfa < ARMC ):
		alfa_1 = 360 + alfa
	else:
		alfa_1 = alfa
	if ( delta > 0 ):
		if ( alfa_1 > AOHOR + DA):
			quadrante = 4
		else:
			quadrante = 1
		HTD = 15 + ( DA / 6 )
	if ( delta < 0 ):
		if ( alfa_1 > AOHOR - DA):
			quadrante = 4
		else:
			quadrante = 1
		HTD = 15 - ( DA / 6 )
	if ( quadrante == 1 ):
		if ( 0 < alfa_1 < 52.9624 ):
			DR = 360 - ARMC + alfa
		else:
			DR = alfa_1 - ARMC
		DH = DR / HTD
		DISTANZA = abs( DH - DHSORTE)
		if ( DISTANZA < 0.5 ):
			print( lineSplit[0] + '...' + str( alfa ) + ' ... ' + str( alfa_1 ) + ' ... '+ str( DA ) + ' ... ' + 'quadrante: ' + str(quadrante) +  ' ... ' + str( DH ) +   ' ... ' + str( DISTANZA ) + '\n' )
