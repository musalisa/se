import swisseph as swe

YYYY = 1964
MM = 11
DD = 8
hh = 23
mm = 3
ut = hh + mm/60
print(swe.julday( YYYY, MM, DD, ut, swe.GREG_CAL))
