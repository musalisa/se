import swisseph as swe
#swe.set_ephe_path('/usr/share/ephe') # set path to ephemeris files
now = swe.julday(2007,3,3) # get Julian day number
res = swe.lun_eclipse_when(now) # find next lunar eclipse (from now on)
ecltime = swe.revjul(res[1][0]) # get date UTC
print (ecltime)
