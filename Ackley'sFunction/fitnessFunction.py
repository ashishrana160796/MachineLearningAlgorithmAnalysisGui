from __future__ import division
import math as m
# Ackley's Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 10    # Problem Dimension
LB      = -35   # Xi value Lower Bound
UB      = 35   # Xi value Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    term1 = 0
    term2 =0
    for i in range(D+1):
        #associated with ft1
        term1 =term1+ x[i]*x[i]
        #associated with ft2
        term2 =term2+  m.cos(2*3.14*x[i])
        
    
    ft1 = 20*m.exp(-0.02*m.sqrt(term1/D))
    ft2 = m.exp(term2/D)
    
    result = 20 + m.exp(1) - ft1 - ft2
        
    return round(result,2)













