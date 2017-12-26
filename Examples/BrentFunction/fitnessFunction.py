import math as m
# Brent Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -10   # Set Size Lower Bound
UB      = 10   # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	result = result + ((x[0]+10)**2) + ((x[1]+10)**2) + m.exp((-1*x[0]**2)-(1*x[1]**2))
	return result
