# -*- coding: utf-8 -*-
import swisseph as swe
import math
import datetime

global epsilon
epsilon = 23.45

def decdeg2dms(dd):
	is_positive = dd >= 0
	minutes,seconds = divmod(dd*3600,60)
	degrees,minutes = divmod(minutes,60)
	degrees = degrees if is_positive else -degrees
	return (int(degrees),int(minutes),round(seconds))

def decdeg2dm(dd, format=""):
	is_positive = dd >= 0
	minutes,seconds = divmod(dd*3600,60)
	degrees,minutes = divmod(minutes,60)
	degrees = degrees if is_positive else -degrees
	if (format == "gm"):
		return(degrees + '°' + minutes + '')
	else:
		return (int(degrees),round(minutes))

def hor(hor, polo):
#Formula 23 per l'oroscopo nell'emisfero ascendente
	h = math.radians( hor )
	e = math.radians( epsilon )
	p = math.radians( polo )
	d = math.cos( h ) * math.cos( e ) - math.sin( e ) * math.tan( p )   
	hor = math.atan( math.sin( h )/d ) 
	if d > 0:
		return math.degrees(hor)
	else:
		return math.degrees(hor) + 180
	
##  formula 23 emisfero ascendente
# tan(lambda) = sen(AOCH)/cos(AOCH)*(cos(epsilon) - sen(epsilon)*tan(Polo))
##  formula 24 emisfero discendente
# tan(lambda) = sen(DOCH)/cos(DOCH)*(cos(epsilon) + sen(epsilon)*tan(Polo))
# Differenza ascensionale mac
#sen (DAmax) = tan (e) tan (lat)
#  formila 22 poli case 11, 3, 5, 9	tan (P) = sen (1/3 DAmax) cot (e)
#formula  (23) poli case 12, 2, 6, 8	tan (P) = sen (2/3 DAmax) cot (e)

###### Data #################################
# uomo nato a Milano (longitudine 9°11' Est, latitudine +45°28') il 14 Aprile 1956 alle ore 10 e minuti 35, ora civile
## 14 Aprile 1956, ore 10:35 (9:35 TU) a Milano, +45°28', 9°11' Est.
#YYYY = 1956
#MM = 4
#DD = 14
#hh = 9
#mm = 35
#Lezione 7 Es.  20  Bologna (+44°30', Est 11°21'), 22 Febbraio 1940, 11h 20m TU.
giorno = datetime.datetime.now().date()
ora = datetime.datetime.now().time()

YYYY = giorno.year
MM = giorno.month
DD = giorno.day
hh = ora.hour
mm = ora.minute
ut = hh + mm/60
jut = swe.julday( YYYY, MM, DD, ut, swe.GREG_CAL)

house_nums = (10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#print(house_nums)

###### Luogo ################################
# Alessandria 44°54′48″N 8°37′12″E 95m
#top_long = 44.916; top_lat = 8.616; top_elev = 95;
# Milano 45°27′50.98″N 9°11′25.21″E 122m
#top_lat = 45.464; top_long = 9.19; top_elev = 122;
# Bologna (+44°30', Est 11°21')
top_lat = 44.5; top_long = 11.35; top_elev = 54;

swe.set_topo(top_long, top_lat, top_elev)

## CASE ##########################################
# Ascensione retta mediocelo
ARMC = (swe.sidtime(jut)+(top_long/15))*15;  
#print( "\nARMC")
#print(ARMC)

# Ascensioni oblique  delle case (corrispondono alle ascensioni rette, in quanto si misurano sull'equatore
case_aoch = [ARMC]
case_aoch_gm = []
for i in range(1,12):
	case_aoch.append((case_aoch[i-1] + 30)%360)
for i in range(1,12):
	case_aoch_gm.append(decdeg2dm(case_aoch[i],"dm"))
print( "\nAOCH case dalla 10°")
print(case_aoch)
#print(case_ar_gm)

#  Ascensioni oblique delle  case
(ZZ, AOHOR) = divmod((ARMC + 90) , 360)
print( "\nAOHOR")
print( AOHOR)

# Poli delle case
case_poli = []

# Cuspidi delle case sullo zodiaco
case_cuspidi = swe.houses(jut, top_lat, top_long, b'P')[0]
HOR = hor( AOHOR, top_lat)
#HOR = case_cuspidi[0]
print( "\nHOR")
print( HOR )
print(decdeg2dm(HOR))
print( "\ncuspidi case dalla 10° sullo zodiaco")
print(case_cuspidi)
swe_houses = swe.houses(jut, top_lat, top_long, b'P')



### CARTA Z #################################
#print( "\nCuspidi dei segni")
grado_z = 180 - AOHOR
cx = 350
cy = 350
z1 = 200
z2 = 300
#for i in range(0, 360, 30):
	##print (grado_z+i, math.cos(math.radians(grado_z+i))*80, math.sin(math.radians(grado_z+i))*80,math.cos(math.radians(grado_z+i))*100, math.sin(math.radians(grado_z+i))*100);
	#print ( "{ x1:", (math.cos(math.radians(grado_z+i)) * z1) + cx, ",")
	#print ( "  y1:", (math.sin(math.radians(grado_z+i)) * -z1) + cy, ",")
	#print ( "  x2:", (math.cos(math.radians(grado_z+i)) * z2) + cx, ",")
	#print ( "  y2:", (math.sin(math.radians(grado_z+i)) * -z2) + cy, "\n},")

#print(swe_houses)
print( "\nPIANETI - Eclittiche ed equatoriali")
for p in range( 0,7 ):
	print( "\n" + swe.get_planet_name( p ))
	print("lamda %.4f beta %4f" %  (swe.calc_ut( jut, p, swe.FLG_SPEED )[0],swe.calc_ut( jut, p, swe.FLG_SPEED )[1] ))
	print("alfa %.4f delta %4f" %  (swe.calc_ut( jut, p, swe.FLG_EQUATORIAL )[0],swe.calc_ut( jut, p, swe.FLG_EQUATORIAL )[1] ))


#print(swe.houses_ex(jut, top_lat, top_long, b'P'))
#        Calculate houses cusps (UT).
#       
#        Args: float julday, float lat, float lon, char hsys='P'
#        Return: 2 tuples of 12 and 8 float (cusps, ascmc) (except Gauquelin)
