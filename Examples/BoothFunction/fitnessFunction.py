import math as m
#Booth Function
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
	result = result + (x[0]+2*x[1]-7)**2 + (2*x[0]+x[1]-5)**2
	
	return result
