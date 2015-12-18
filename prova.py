import swisseph as swe

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
# uomo nato a Milano (longitudine 9°11' Est, latitudine +45°28') il 14 Aprile 1956 alle ore 10 e minuti 35, ora civile

###### Data #################################
YYYY = 1956
MM = 4
DD = 14
hh = 9
mm = 35
ut = hh + mm/60
jut = swe.julday( YYYY, MM, DD, ut, swe.GREG_CAL)

house_nums = (10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#print(house_nums)

###### Luogo ################################
# Alessandria 44°54′48″N 8°37′12″E 95m
#top_long = 44.916; top_lat = 8.616; top_elev = 95;
# Milano 45°27′50.98″N 9°11′25.21″E 122m
top_lat = 45.464; top_long = 9.19; top_elev = 122;
swe.set_topo(top_long, top_lat, top_elev)

## CASE ##########################################
ARMC = (swe.sidtime(jut)+(top_long/15))*15;  
case_ar = [ARMC]
case_ar_gm = []
case_poli = []
case_cuspidi = swe.houses(jut, top_lat, top_long, b'P')[0]
for i in range(0,12):
	case_ar.append((case_ar[i-1] + 30)%360)
for i in range(1,12):
	case_ar_gm.append(decdeg2dm(case_ar[i],"dm"))
print( "AR case dalla 10°")
print(case_ar)
print(case_ar_gm)
print( "cuspidi case dalla 10°")
print(case_cuspidi)
swe_houses = swe.houses(jut, top_lat, top_long, b'P')
#print(swe_houses)

#for p in range( 0,7 ):
#	print( swe.get_planet_name( p ))
#	print( swe.calc_ut( jut, p, swe.FLG_SPEED ))
#	print( swe.calc_ut( jut, p, swe.FLG_EQUATORIAL ))


#print(swe.houses_ex(jut, top_lat, top_long, b'P'))
#        Calculate houses cusps (UT).
#       
#        Args: float julday, float lat, float lon, char hsys='P'
#        Return: 2 tuples of 12 and 8 float (cusps, ascmc) (except Gauquelin)
