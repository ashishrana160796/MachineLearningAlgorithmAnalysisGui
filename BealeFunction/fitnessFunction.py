import math as m
# Beale Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -4.5   # Xi Value Lower Bound
UB      = 4.5   # Xi Value Upper Bound
#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	result = result + (1.5-x[0]+x[0]*x[1])**2 + (2.25 -x[0]+x[0]*x[1]*x[1])**2 + (2.625 - x[0] +x[0]*(x[1]**3))**2
	
	return result
