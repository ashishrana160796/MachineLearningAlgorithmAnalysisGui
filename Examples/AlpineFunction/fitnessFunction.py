import math as m
#Alpine Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 10    # Problem Dimension
LB      = -10   # Xi value Lower Bound
UB      = 10   # Xi value Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    result=0
    # limit on x in not applied here
    for i in range(D):
        result = result + abs(x[i]*m.sin(x[i])+0.1*x[i])    
    
        
    return round(result,2)













