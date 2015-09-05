__author__ = 'Davide Manuel dos Santos'
# Module: UniformFreeSurfaceFlow.py
# version 0.1, September 2015


# uniform surface flow heigh for prismatic sections
# by: Davide Manuel dos santos
# August, 2015
def UFSF_prismatic_y(q, n, s, b, ml, mr, maxerror, maxiter):
    y = 1.0
    err = 100.0
    iter = 0
    while err >= maxerror and iter <= maxiter:
            iter = iter + 1
            a = y *(b + ml*y*0.5 + mr*y*0.5)
            p = b + y*((1 + ml*ml)**0.5 + (1 + mr*mr)**0.5)
            r = a / p
            y1 = ((q * n)/(r**(2.0/3.0)*(s)**0.5))/(b + ml*y*0.5 + mr*y*0.5)
            err = ((y-y1)**2.0)**0.5

            if err >= maxerror:
                y = y1
    return(y,err,iter);

# uniform surface flow for a given slope and water height in prismatic channels
# by: Davide Manuel dos santos
# August, 2015
def UFSF_prismatic_q(y, n, s, b, ml, mr):
    a = y *(b + ml*y*0.5 + mr*y*0.5)
    p = b + y*((1 + ml*ml)**0.5 + (1 + mr*mr)**0.5)
    r = a / p
    q = a*r**(2/3)*s**(0.5)/n
    return(q);