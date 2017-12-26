#-------------------------------------------------------------
#                       Randomization
#-------------------------------------------------------------
# To solve optimization problem (minimization) using randomly.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
import fitnessFunction as ff # Fitness Function and Parameters
import matplotlib.pyplot as plt
startTime = time.time()

#-------------------------------------------------------------
# Step 2: Random Algorithm  Parameters
#-------------------------------------------------------------
AlgoName    = "RandomBasic"	# Algo Name
Iterations  = 20000       # Number of Iterations
BestFitness = 9999999   # Store Best Fitness Value
BestChromosome = []     # Store Best Chromosome


#-------------------------------------------------------------
# Step 3: Problem parameters
#-------------------------------------------------------------
# FitnessFunction is defined in fitnessFunction.py file



#-------------------------------------------------------------
# Step 4: Fitness Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in fitnessFunction.py file



#-------------------------------------------------------------
# Step 5: Start Program
#-------------------------------------------------------------

# Saving Result
fp=open(AlgoName+"Result.csv","w")
fp.write("Iteration,Fitness,Chromosome\n")

# for plotting the graph


count=0
a=[]


for i in range(0,Iterations):
	
        Chromosome = []
        for j in range(0,ff.D):
                Chromosome.append(round(random.uniform(ff.LB,ff.UB),2))
        Fitness = ff.FitnessFunction(Chromosome)
        if Fitness < BestFitness:
                BestFitness=Fitness
                BestChromosome=Chromosome
        if i%100==0:
                print "I:",i,"\t Fitness:",BestFitness
                fp.write(str(i) + "," + str(BestFitness)+ "," + str(BestChromosome) + "\n")
                #plotting with y-axis
                count=count+1
                #plotting with x-axis
                a.append(BestFitness)

fp.close()

print "Done"
print "\nBest Chromosome:", BestChromosome, "\tFitness:", BestFitness
print "Result is saved in", AlgoName+"Result.csv"
print "Total Time Taken: ", round(time.time() - startTime,2), " sec\n"
plt.plot(range(count), a)
plt.show()

