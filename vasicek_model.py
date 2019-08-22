# Atheesh Krishnan
# Date: 18th Aug, 2019
# Vasicek Model

import math
from scipy.stats import norm
import numpy as np

# interest rate parameters

rzero = 0.04
rbar = 0.05
a = 1.5
sigma = 0.01

# Option parameters: European Call

OM = 2  # Option Maturity in years
OBM = 6  # Option's Bond Maturity in years
K = 0.73

# Bond parameters:

BM = 2 # Bond Maturity in years

def PDB(r,M):
    P = np.exp(-r*M)
    return P

def Pbond(a,M,sigma,rbar):
    Bts = (1/a)*(1-PDB(a,M))
    Rinf = rbar - 0.5*((sigma**2)/(a**2))
    lnA = (Rinf/a)*(1-PDB(a,M)) - M*Rinf - ((sigma**2)/(4*a**3))*(1-PDB(a,M))**2

    P = (PDB(-lnA,1))*(PDB(rbar,Bts))  # Price of the bond
    return P

print('Price of the bond =',Pbond(a,BM,sigma,rbar))

# Pricing the option

sigmaR = (sigma/(a*(OM)))*(1-PDB(a,OM)) # Spot rate volatility
POB = Pbond(a,OBM,sigma,rbar)
PO = Pbond(a,OM,sigma,rbar)
v = np.sqrt(((sigma**2)*(1-PDB(2*a,OM)))/(2*a))
sigmaP =(v*(1-PDB(a, OBM-OM)))/(a)

d1 = ((np.log(POB/(K*PO)))/(sigmaP))+(sigmaP/2)
d2 = d1 - sigmaP

c = POB*norm.cdf(d1) - K*PO*norm.cdf(d2)
print('Price of the European Call =',c)