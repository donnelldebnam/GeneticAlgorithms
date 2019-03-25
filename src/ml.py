from random import *

import genalgorithmlib as ga
import matplotlib.pyplot as plt

''' In this class we will run our entire genetic algorithm, leveraging 
    each of the genetic operators in order to find the pareto front of 
    the dataset after a set amount of generations '''


d = ga.des_space(100)   # Creates decision space
o = ga.obj_space(d)     # Creates initial objective space

GENERATIONS = 100       # Number of generations 

pareto_front = []       # Will store points in pareto front
points = []             # Plotted points will be stored here


# Solve algorithm using multiple generations
for i in range(GENERATIONS):

    new_obj = {} # Will be the new objective space

    # Create 100 new offspring
    for j in range(100):

        # Generate new offspring
        point = ga.new_offspring(o)

        # If x1, x2 pair is already in objective space, find new pair
        while (point in new_obj):
            point = ga.new_offspring(o)

        # Apply fitness function 
        x1, x2 = point[0], point[1]
        f1, f2 = randint(0, 100) + x1, randint(0, 100) + x2
        
        # Map this decision space point to the objective space
        new_obj[point] = [f1, f2]

    # This objective space should be used as basis for next gen.
    o = new_obj

    # Add all points from this objective space
    for i in o:
        points.append(o[i])

# Using theory of exploration, we can now calculate pareto front of
# the entire dataset of points throughout all generations.
pareto_front = ga.get_pareto(points)

# Plot pareto front
for p in pareto_front:
        plt.plot(p[0], p[1], 'bo')

plt.show()
