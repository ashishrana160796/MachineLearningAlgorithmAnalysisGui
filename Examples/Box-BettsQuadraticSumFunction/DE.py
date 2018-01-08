# -------------------------------------------------------------
#               Differential Evolution (DE)
# -------------------------------------------------------------
# To solve optimization problem (minimization) using DE.
# -------------------------------------------------------------
# Python version used: 2.7
# -------------------------------------------------------------


# -------------------------------------------------------------
# Step 1: Library Inclusion
# -------------------------------------------------------------
import random
import time
from copy import deepcopy
import fitnessFunction as ff  # Fitness Function and Parameters
import matplotlib.pyplot as plt

startTime = time.time()

# -------------------------------------------------------------
# Step 2: Parameters
# -------------------------------------------------------------

# 2.1 DE Parameters
algoName = "DEBasic"  # Algo Name
CR = 0.5  # Crossover Rate
F = 0.5  # Inertiea

# 2.2 Global Parameters
iterations = 20000  # Number of iterations
popSize = 100  # Population Size(i.e Number of Chromosomes)
pop = []  # Store Population with Fitness
bestFitness = 99999999  # Store Best Fitness Value
bestChromosome = []  # Store Best Chromosome

# 2.3 Result Saving Parameters
resultFileName = "result" + algoName + ".csv"


# 2.4 Stores Chromosome and its fitness collectively
class Individual:
    def __init__(self, C, F):
        self.chromosome = C
        self.fitness = F


# 2.5 Problem parameters
# Problem Parameters are defined in in fitnessFunction.py file



# -------------------------------------------------------------
# Step 3: Functions Definitions
# -------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in fitnessFunction.py file


# Function 2: Generate Random Initial Population
def Init():
    for i in range(0, popSize):
        chromosome = []
        for j in range(0, ff.D):
            chromosome.append(round(random.uniform(ff.LB, ff.UB), 2))
        fitness = ff.FitnessFunction(chromosome)

        newIndividual = Individual(chromosome, fitness)
        pop.append(newIndividual)


# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest():
    global bestFitness, bestChromosome
    for p in pop:
        if p.fitness < bestFitness:
            bestFitness = p.fitness
            bestChromosome = deepcopy(p.chromosome)


# Function 4: Perform DE Operation
def DEOperation():
    for i in range(0, popSize):

        # Choose three random indices
        i1, i2, i3 = random.sample(range(0, popSize), 3)

        # Iterate for every Dimension
        newChild = []
        for j in range(ff.D):
            if (random.random() <= CR):
                k = pop[i1].chromosome[j] + \
                    F * (pop[i2].chromosome[j] - pop[i3].chromosome[j])

                # If new dimention cross LB
                if k < ff.LB:
                    k = random.uniform(ff.LB, ff.UB)

                # If new dimention cross LB
                if k > ff.UB:
                    k = random.uniform(ff.LB, ff.UB)

                newChild.append(round(k, 2))

            else:
                newChild.append(pop[i].chromosome[j])

        # Child Fitness
        newChildFitness = ff.FitnessFunction(newChild)

        # Select between parent and child
        if newChildFitness < pop[i].fitness:
            pop[i].fitness = newChildFitness
            pop[i].chromosome = newChild


# -------------------------------------------------------------
# Step 4: Start Program
# -------------------------------------------------------------
Init()
globalBest = pop[0].chromosome
globalBestFitness = pop[0].fitness
MemoriseGlobalBest()

# Saving Result
fp = open(resultFileName, "w");
fp.write("Iteration,Fitness,Chromosomes\n")
count=0
a=[]
# Running till number of iterations

for i in range(0, iterations):
    DEOperation()
    MemoriseGlobalBest()

    if i % 100 == 0:
        print("I:", i, "\t Fitness:", bestFitness)
        fp.write(str(i) + "," + str(bestFitness) + "," + str(bestChromosome) + "\n")
        count=count+1
        a.append(bestFitness)
print("I:", i + 1, "\t Fitness:", bestFitness)
fp.write(str(i + 1) + "," + str(bestFitness) + "," + str(bestChromosome))
fp.close()

print("Done")
print("\nBestFitness:", bestFitness)
print("Best chromosome:", bestChromosome)
print("Result is saved in", resultFileName)
print("Total Time Taken: ", round(time.time() - startTime, 2), " sec\n")

plt.plot(range(count),a)
plt.show()




