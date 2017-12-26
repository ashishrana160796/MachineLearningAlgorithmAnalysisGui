import math as m
#Bartels Conn Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2   # Problem Dimension
LB      = -500   # Set Size Lower Bound
UB      = 500   # Set Size Upper Bound
#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	# limit on x in not applied here
	result = result + abs((x[0]*x[0])+(x[1]*x[1])+(x[0]*x[1]))+abs(m.sin(x[0]))+abs(m.cos(x[1]))
	
	return result
	









