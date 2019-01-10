# -*- coding: utf-8 -*-
#import swisseph as swe
import math
import datetime

def DR_min( alfa1, alfa2 ):
    DR1 = abs( alfa2 - alfa1 )
    DR = DR1 if DR1 <= 180 else 360 - DR1
    return( DR )

def DR_( alfa1, alfa2 ):
    DR1 = abs( alfa2 - alfa1 )
    DR = DR1 if DR1 <= 180 else 360 - DR1
    return( DR )

alfa1 = 330
alfa2 = -10
print (alfa1, alfa2, DR_min( alfa1, alfa2 ))
