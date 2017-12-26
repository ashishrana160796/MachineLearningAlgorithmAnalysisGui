import math as m
#Bohachevsky Function

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -100   # Set Size Lower Bound
UB      = 100   # Set Size Upper Bound
#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	# limit on x'i' value not defined here
	result = result + x[0]*x[0]+2*x[1]*x[1]+0.7 - 0.3*m.cos(3*m.pi*x[0])+0.4*m.cos(4*m.pi*x[1])
	
	return result
