# -------------------------------------------------------------
#               Particle Swarm Optimization (PSO)
# -------------------------------------------------------------
# To solve optimization problem (minimization) using PSO.
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

# 2.1 PSO Parameters
algoName = "PSOBasic"  # Algo Name
c1 = 1.5  # Acceleration constant
c2 = 1.5  # Acceleration constant
w = 0.8  # Inertia weight
vLB = -1  # Velocity Lower Bound
vUB = 1  # Velocity Upper Bound

# 2.2 Global Parameters
iterations = 20000  # Number of iterations
popSize = 100  # Population Size(i.e Number of Chromosomes)
pop = []  # Store Population with Fitness
gBest = []  # Rember Global Best chromosome
gBestFitness = []  # Rember fitness of Global Best chromosome

# 2.3 Result Saving Parameters
resultFileName = "result" + algoName + ".csv"


# 2.4 Stores Particle, ParticleFitness, Velocity, PBest,PBestFitness collectively;
class Individual:
    def __init__(self, P, PF, V, PB, PBF):
        self.particle = P
        self.particleFitness = PF
        self.velocity = V
        self.pBest = PB
        self.pBestFitness = PBF


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
        particle = []
        velocity = []
        for j in range(0, ff.D):
            particle.append(round(random.uniform(ff.LB, ff.UB), 2))
            velocity.append(round(random.uniform(vLB, vUB), 2))

        particleFitness = round(ff.FitnessFunction(particle), 2)
        newIndividual = Individual(particle, particleFitness, velocity, deepcopy(particle), particleFitness)
        pop.append(newIndividual)


# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest():
    global gBest, gBestFitness
    for p in pop:
        if p.pBestFitness < gBestFitness:
            gBest = deepcopy(p.pBest)
            gBestFitness = p.pBestFitness


# Function 4: Perform PSO Operation
def PSOOperation():
    for i in range(0, popSize):
        for j in range(0, ff.D):

            # Choose two random numbers
            r1 = random.random()
            r2 = random.random()

            # Velocity update
            pop[i].velocity[j] = w * pop[i].velocity[j] + \
                                 c1 * r1 * (pop[i].pBest[j] - pop[i].particle[j]) + \
                                 c2 * r2 * (gBest[j] - pop[i].particle[j])

            if pop[i].velocity[j] < vLB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)

            if pop[i].velocity[j] > vUB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)

            # Particle update
            pop[i].particle[j] = round(pop[i].particle[j] + pop[i].velocity[j], 2)

            if pop[i].particle[j] < ff.LB:
                pop[i].particle[j] = round(random.uniform(ff.LB, ff.UB), 2)

            if pop[i].particle[j] > ff.UB:
                pop[i].particle[j] = round(random.uniform(ff.LB, ff.UB), 2)

        pop[i].particleFitness = round(ff.FitnessFunction(pop[i].particle), 2)

        # Select between particle and pBest
        if pop[i].particleFitness <= pop[i].pBestFitness:
            pop[i].pBest = pop[i].particle
            pop[i].pBestFitness = pop[i].particleFitness


# -------------------------------------------------------------
# Step 4: Start Program
# -------------------------------------------------------------
Init()
gBest = pop[0].pBest
gBestFitness = pop[0].pBestFitness
MemoriseGlobalBest()

# Saving Result
fp = open(resultFileName, "w");
fp.write("Iteration,Fitness,Chromosomes\n")
count=0
a=[]

# Running till number of iterations
for i in range(0, iterations):
    PSOOperation()
    MemoriseGlobalBest()

    if i % 100 == 0:
        print("I:", i, "\t Fitness:", gBestFitness)
        fp.write(str(i) + "," + str(gBestFitness) + "," + str(gBest) + "\n")
        count=count+1
        a.append(gBestFitness)
print("I:", i + 1, "\t Fitness:", gBestFitness)
fp.write(str(i + 1) + "," + str(gBestFitness) + "," + str(gBest))
fp.close()

print("Done")
print("\nBestFitness:", gBestFitness)
print("Best particle:", gBest)
print("Result is saved in", resultFileName)
print("Total Time Taken: ", round(time.time() - startTime, 2), " sec\n")

plt.plot(range(count),a)
plt.show()

