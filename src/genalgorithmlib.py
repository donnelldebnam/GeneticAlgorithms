from operator import itemgetter
from random import *


# Creates an initial decision space to begin genetic
# algorithm.
def des_space():
    space = []
    for i in range(100):
        space.append(randint(0, 20))
    return space


# Returns an objective space of 1000 values,
# based on a given decision space
def obj_space(values):
    map = {}
    for i in range(1000):
        x1 = values[randint(0, 99)]
        x2 = values[randint(0, 19)]
        #f1 = (x1 ** 2) + (x2 ** 2)
        #f2 = x1 + (3 * (x2 ** 2))
        f1 = randint(0, 100)
        f2 = randint(0, 100)
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
    pset.append(x_min)
    pset.append(y_min)
    # possibilities.append(x_min)
    # possibilities.append(y_min)
    # Loop through all values in pset to determine fitness of
    # this new point.
    for v in values:
        x = v[0]
        y = v[1]
        if x_min[0] <= x <= y_min[0] and x_min[1] >= y >= y_min[1]:
            possibilities.append(v)
    # Loop trough all possibilities and determine which dominate each
    # other, resulting in final pareto set
    for i in possibilities:
        x = i[0]
        y = i[1]
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
    for p in pset:
        if p not in s:
            s.append(p)
    return s
