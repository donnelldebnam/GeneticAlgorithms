import genalgorithmlib as ga
import matplotlib.pyplot as plt
from random import *

# Creates decision space, size 1000 
d = ga.des_space(1000)
# Creates initial objective space
o = ga.obj_space(d)
# Plotted points will be stored here
points = [] 

GENERATIONS = 100

pareto_front = []
new_obj = {}  # will be the new objective space

# Solve algorithm using multiple generations
for i in range(GENERATIONS):

    new_obj.clear()

    # Create 100 new offspring
    for j in range(100):

        # Get random x1 and x2 pair
        p1 = choice(list(o.keys()))
        p2 = choice(list(o.keys()))

        # Cast tuple to make data indexable
        list(p1), list(p2)

        # Complete genetic crossover
        offspring = ga.crossover(p1, p2)

        # Compute f1 and f2 of the new x1 and x2 values
        x1, x2 = offspring[0], offspring[1]

        # Fitness functions
        f1, f2 = randint(0, 100) + x1, randint(0, 100) + x2

        # Map these decision space values to the objective space
        new_obj[(x1, x2)] = [f1, f2]

    # Combine population and pareto set
    for point in new_obj:
        pareto_front.append(new_obj[point])
    # Get updated pareto set
    pareto_front = ga.get_pareto(pareto_front)
