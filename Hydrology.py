__author__ = 'WaterPython'

import sys
import math
# River concentration time according to Z.P. KIRPICH
# Tc, minutes
# l, m
# s, m/m
# tc, min
def HYD_kirpich_tc(l,s):
    tc = 0.00032*(l**0.77/s**0.385)
    return(tc);

#CN transformation according to AMC I,II or III
def HYD_scs_cn(cn2,amc):
    if amc == 1:
        cn = cn2/(2.3-0.013*cn2)
    elif amc == 2:
        cn = cn2
    elif amc == 3:
        cn = cn2/(0.43+0.0057*cn2)
    else:
        print("Inputted AMC:", amc)
        sys.exit("Incorrect AMC, should be: 1, 2 or 3!")
    return (cn);

# determina)on of potential storage according to SCS
def HYD_scs_s(cn2,amc):
    cn = HYD_scs_cn(cn2,amc)
    s = 25400/cn - 254
    return (s);

# determination of initial abstraction according to SCS
def HYD_scs_ia(cn2,amc):
    s = HYD_scs_s(cn2,amc)
    ia = 1.33*(0.2*s)**1.15
    return (ia);

# determination of efective rain according to SCS
def HYD_scs_q(p,cn2,amc):
    ia = HYD_scs_ia(cn2,amc)
    s = HYD_scs_s(cn2,amc)
    if (p-ia) <=0.0:
        q = 0-0
    else:
        q = (p-ia)**2/(p-ia+s)
    return (q);

# determination of Infiltration
def HYD_scs_inf(p,cn2,amc):
    q = HYD_scs_q(p,cn2,amc)
    inf = p - q
    return (inf);

# Synthetic Dimensionless Unit Hydrograph of SCS
def HYD_scs_duh(l,s,area):
    tc = HYD_kirpich_tc(l,s)
    d = 0.133*tc #unit excess rainfall, h
    tl = 0.6*tc #time lag, h
    tp = d/2.0 + tl #time to peak of the hydrogram, h
    tr = 1.67*tp #recession limb time of the hydrogram, h
    tb = tr + tp #base time of the hydrogram, h
    qp = 2.08*area*10**(-6)/tp #peak flow, h
    n = math.ceil(tb/d)+1
    duh = [] #Dimensionless Unit Hydrograph
    tbj = 0.0
    for i in range(0,n):
        duh[i] =  duh.append(i)
        if tbj == 0.0:
            duh[i] =  0.0
            tbj += d
        elif tbj <= tp:
            duh[i] = tbj*qp/tp
            tbj += d
        elif tbj > tp and tbj <= tb:
            duh[i] = (tb-tbj)*qp/tr
            tbj += d
        elif tbj > tb:
            duh[i] = 0.0
            tbj += d
    return(tc, d,tp,tr,qp, duh);


# Flood hydrogram (SCS)
def HYD_scs_hydrograph(l,s,area,p):

    (tc, d,tp,tr,qp, duh)= HYD_scs_duh(l,s,area)
    matrix = [[0 for i in range(len(duh)+len(p)-1)] for j in range (len(p))]
    hydrogram = [0 for i in range(len(duh)+len(p)-1)]
    volume = 0.0
    for i in range(len(p)):
        for j in range(len(duh)):
            matrix[i][j+i] = p[i]*duh[j]/10.0 #matrix of the DUH for each rain period (d = unit excess rainfall)
    for i in range(len(duh)+len(p)-1):
        for j in range (len(p)):
            hydrogram[i] += matrix[j][i] #hydrograph
            volume += hydrogram[i]*d*3600 # volume of the hydrograph

    return(d,hydrogram,volume);






