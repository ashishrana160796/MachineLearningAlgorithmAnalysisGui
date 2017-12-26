from __future__ import division
import math as m
# Branin RCOS Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -5   # Set Size Lower Bound
UB      = 15   # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	result = result + (x[1]-((5.1*x[0]*x[0])/(4*m.pi*m.pi))+((5*x[0])/6)-6)**2 + 10*(1-(1/(8*m.pi)))*m.cos(x[0])+10
	
	return result 
