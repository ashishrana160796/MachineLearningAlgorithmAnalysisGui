import math as m
#Bird Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -2*m.pi   # Set Size Lower Bound
UB      = 2*m.pi   # Set Size Upper Bound
#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	# limit on x in not applied here
	result = result + (m.sin(x[0])*m.exp((1-m.cos(x[1]))**2)) + (m.cos(x[1])*m.exp((1-m.sin(x[0]))**2)) + ((x[0]-x[1])**2)
	
	return result

