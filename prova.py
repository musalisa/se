import swisseph as swe


###### Data #################################
YYYY = 1964
MM = 11
DD = 8
hh = 23
mm = 3
ut = hh + mm/60
jut = swe.julday( YYYY, MM, DD, ut, swe.GREG_CAL)

###### Luogo ################################
# Alessandria 44°54′48″N 8°37′12″E 95m
top_long = 44.916; top_lat = 8.616; top_elev = 95;
# Milano 45°27′50.98″N 9°11′25.21″E 122m
# top_long = 45.464; top_lat = 9.19; top_elev = 122;
swe.set_topo(top_long, top_lat, top_elev)
for p in range( 0,7 ):
	print( swe.get_planet_name( p ))
	print( swe.calc_ut( jut, p, swe.FLG_SPEED ))
	print( swe.calc_ut( jut, p, swe.FLG_EQUATORIAL ))
