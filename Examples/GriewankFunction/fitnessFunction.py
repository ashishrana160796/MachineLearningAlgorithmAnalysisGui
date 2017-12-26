from __future__ import division
import math as m


#Griewank Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 10    # Problem Dimension
LB      = -100   # Xi value Lower Bound
UB      = 100   # Xi value Size Upper Bound

def FitnessFunction(x):
	trm1 = 0
	trm2 = 1
	for i in range(0,D):
		trm1 = trm1 + (x[i]*x[i])
		trm2 = trm2*m.cos(x[i]/m.sqrt(i+1))
		
		trm1 = trm1/4000
	result = trm1 - trm2 + 1
	
	
	return round(result,2)	 
