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

print(swe.calc_ut( jut, 1, swe.FLG_SPEED) )
#  /*
#   * we have day, month and year and convert to Julian day number
#   */
#  tjd = swe_julday(jyear,jmon,jday,jut,SE_GREG_CAL);
#  /*
#   * compute Ephemeris time from Universal time by adding delta_t
#   */
#   te = tjd + swe_deltat(tjd);
#   printf("date: %02d.%02d.%d at %02d:%02d Universal time\n", jday, jmon, jyear, ora, min);
#   printf("planet     \tlongitude\tlatitude\tdistance\tspeed long.\n");
#            /*
#             * a loop over all planets
#             */
#    for (p = SE_SUN; p <= SE_SATURN; p++) {
#      if (p == SE_EARTH) continue;
#                /*
#                 * do the coordinate calculation for this planet p
#                 */
#      iflgret = swe_calc(te, p, iflag, x2, serr);
#              /*
#               * if there is a problem, a negative value is returned and an
#               * errpr message is in serr.
#               */
#      if (iflgret < 0)
#        printf("error: %s\n", serr);
#      else if (iflgret != iflag)
#        printf("warning: iflgret != iflag. %s\n", serr);
#              /*
#               * get the name of the planet p
#               */
#      swe_get_planet_name(p, snam);
#              /*
#               * print the coordinates
#               */
#      printf("%10s\t%11.7f\t%10.7f\t%10.7f\t%10.7f\n",
#             snam, x2[0], x2[1], x2[2], x2[3]);
#
