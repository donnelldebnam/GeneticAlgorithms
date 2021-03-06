from operator import itemgetter
from random import *


''' Class contains mathematic models to create decision space, 
    objective space, and finds pareto front of given dataset. '''


# Creates an initial decision space to begin genetic
# algorithm.
def des_space(size):
    values = []
    space = []
    for i in range(100):
        values.append(randint(0, 20))
    for i in range(size):
        x1 = values[randint(0, 99)]
        x2 = values[randint(0, 19)]
        # If pair already in decision space, create new point
        while [x1, x2] in space:
            x1 = values[randint(0, 99)]
            x2 = values[randint(0, 19)]
        space.append([x1, x2])
    return space


# Returns an objective space of 100 values, based
# on a given decision space
def obj_space(decision_space):
    map = {}
    for i in decision_space:
        x1, x2 = i[0], i[1]
        f1 = randint(0, 100) + x1
        f2 = randint(0, 100) + x2
        map[(x1, x2)] = [f1, f2]
    return map


# Returns a pareto set of values based on a given set of coordinates
# on a graph.
def get_pareto(values):
    pset = []
    possibilities = []
    # Grabs the point with smallest x-value
    x_min = sorted(values, key=itemgetter(0))[0]
    # Grabs the point with smallest y-value
    y_min = sorted(values, key=itemgetter(1))[0]
    # If this optimal point exists in dataset,
    # return this point
    if [x_min[0], y_min[1]] in values:
        return [x_min[0], y_min[1]]
    # Add these values to pareto set
    pset.append(x_min), pset.append(y_min)
    # Loop through all values in pset to determine fitness of
    # this new point.
    for v in values:
        x, y = v[0], v[1]
        if x_min[0] <= x <= y_min[0] and x_min[1] >= y >= y_min[1]:
            possibilities.append(v)
    # Loop trough all possibilities and determine which dominate each
    # other, resulting in final pareto set
    for i in possibilities:
        x, y = i[0], i[1]
        added = False
        pareto = True
        for p in pset:
            if pareto and not added:
                if x > p[0] and y > p[1]:
                    pareto = False
                elif x < p[0] and y < p[1]:
                    pset.remove(p)
                    pset.append(i)
            if not pareto:
                for a in pset:
                    if a is i:
                        pset.remove(i)

        if pareto and not added:
            pset.append(i)

    return clean_pareto(update_pareto(pset))


# Returns pareto set after making another round of
# finding fittest points.
def update_pareto(pset):
    for i in pset:
        for j in pset:
            if j[0] < i[0] and j[1] < i[1]:
                if i in pset:
                    pset.remove(i)
                    pset.append(j)
            elif j[0] > i[0] and j[1] > i[1]:
                pset.remove(j)
                pset.append(i)
    return pset


# Returns set without duplicates
def clean_pareto(pset):
    s = []
    [s.append(p) for p in pset if p not in s]

    return s


''' These will be methods associated with genetic operators. '''


# Returns offspring of two points in dataset
def crossover(p1, p2):
    alpha = round(uniform(0, 1), 1)
    beta = round(uniform(0, 1), 1)
    x = ((alpha * p1[0])) + ((1 - alpha) * p2[0])
    y = ((beta * p1[1])) + ((1 - beta) * p2[1])
    return [round(x, 1000), round(y, 1000)]


def new_offspring(o):
    p1 = choice(list(o.keys()))
    p2 = choice(list(o.keys()))

    list(p1), list(p2)

    offspring = crossover(p1, p2)
    x1, x2 = offspring[0], offspring[1]

    return tuple([x1, x2])
