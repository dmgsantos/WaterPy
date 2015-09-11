__author__ = 'WETpython'

#from Equipment import*
#from Hydrology import*
from WaterProperties import *


zr1 = 10
zr2 = 50
zpump = 12
ppump = 500000.
ypump = 0.75
rho = 1000.0

ds = .75
ns = 0.013333
sumks = 5.0
ls = 10.0

dc = .5
nc = 0.01
sumkc = 10.0
lc = 2000.0

q = 0.25

patm = 101625
z0 = 10
ze = 15


#p = EQ_pumpstation_p(zr1,zr2,q,ypump,rho,ds,ns,sumks,ls,dc,nc,sumkc,lc)
#npshr = EQ_pumpstation_npshr(z0,ze,q,rho,ds,ns,sumks,ls, patm, t)

#print("p:",p/1000.0,"kW", )
#print("npshr:",npshr,"m", )

p = 100.0
cn = 70.0
area = 500.0
l = 75.0
s = 0.5
#(qmax, pe, tc) = HYD_scs_qmax(p, cn, area, l, s)

#print("qmax:",qmax,"m3/s", )
#ce = pe/p
#print (qmax, pe, tc, ce)
t = 60.0
s = 0.0
rho = WATER_density_rho(t,s)
dvisc = WATER_dviscosity_dvisc(t)
kvisc = WATER_kviscosity_kvisc(t,s)
print(t,s, rho, dvisc, kvisc)

