import genalgorithmlib as ga
from random import *


d = ga.des_space()
o = ga.obj_space(d)
points = []
for i in o:
    points.append(o[i])

# Create Offspring
for i in range(100):

    # Get random x1 and x2 pair
    p1 = choice(list(o.keys()))
    p2 = choice(list(o.keys()))

    # Cast tuple to make data indexable
    list(p1)
    list(p2)

    # Complete genetic crossover
    offspring = ga.crossover(p1, p2)

    print(offspring)
