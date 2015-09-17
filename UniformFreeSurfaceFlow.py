__author__ = 'WETpython'
# Module: UniformFreeSurfaceFlow.py
# version 0.1, September 2015

from Geometry import *

# uniform surface flow heigh for prismatic sections
# by: WETpython
# August, 2015
def UFSF_prismatic_y(q, n, s, b, ml, mr, maxerror, maxloop):
    dy = 0.1
    y0 = 0.01
    y = y0
    err = 100.0
    loop = 0
    while err >= maxerror and loop <= maxloop:
        loop += 1

        if y > 1000:
            y += y0 + dy
        r = GEO_geometry_hrprism(y, b, ml, mr)
        wlprism = GEO_geometry_wlprism(y, b, ml, mr)
        y1 = ((q * n)/(r**(2.0/3.0)*(s)**0.5))*(2/(b + wlprism))

        err = ((y-y1)**2.0)**0.5

        if err >= maxerror:
            y = y1

    return(y,err,loop);

# uniform surface flow for a given slope and water height in prismatic channels
# by: WETpython
# August, 2015
def UFSF_prismatic_q(y, n, s, b, ml, mr):
    a = y *(b + ml*y*0.5 + mr*y*0.5)
    r = GEO_geometry_hrprism(y, b, ml, mr)
    q = a*r**(2/3)*s**(0.5)/n
    return(q);