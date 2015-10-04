__author__ = 'WETpython'
import math
from WaterProperties import *

#Saturation pH calcite or calcium carbonate
def WATERCHEM_phscalcium(t,tds,ca,hco3):
    tk = WATER_temperature_c2k(t) # temperature: oC to K
    mca = ca*0.001/40.08 # Ca2+: mg/l to Mole/l
    mhco3= hco3*0.001/100 # Alkalinity, hco3- : mg/l to Mole/l
    i = 2.5*10**(-5)*tds # ionic strenght, Moles/l
    d = 1 #density
    e = 60954/(tk+116)-68.937 #dielectric constant
    a = 1.825*10**6*d**0.5*(e*tk)**(-1.5) #correction factor
    zca = 2 #ionic charge of C2+
    zhco3 = 1 #ionic charge of HCO3-
    if i <= 0.5:
        lghco3 = -a*zhco3**2*(i**0.5/(1+i**0.5)-0.3*i) # activity coefficient for HCO3-
    if i > 0.5:
        lghco3 = -a*zhco3**2*(i**0.5/(1+i**0.5)) # activity coefficient for HCO3-
    lgca = -a*zca**2*(i**0.5/(1+i**0.5)) # activity coefficient for Ca
    pk2 = 2902.39/tk + 0.02379*tk-6.498
    k2 = 10**(-pk2)
    gamma_d = 10**lgca
    kl2= k2/gamma_d
    pkl2 = math.log10(1/kl2)
    pks = 0.01183*t+8.03
    ks = 1/10**pks
    kls = ks/gamma_d**2
    pkls = math.log10(1/kls)
    pca=math.log10(1/mca)
    phs = pkl2 + pca - pkls - math.log10(2*mhco3)- lghco3
    return(phs);

# Langelier Saturation Index - LSI
def WATERCHEM_lsi(t,ph,tds,ca,hco3):
        phs = WATERCHEM_phscalcium(t,tds,ca,hco3)
        lsi = ph - phs
        return(lsi);

# Ryznar Stability Index - RSI
def WATERCHEM_rsi(t,ph,tds,ca,hco3):
    phs = WATERCHEM_phscalcium(t,tds,ca,hco3)
    ri = 2*phs - ph
    return(ri);