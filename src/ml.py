import matplotlib.pyplot as plt
import genalgorithmlib as ga


d = ga.des_space()
o = ga.obj_space(d)

points = []

for i in o:
    points.append(o[i])

pset = ga.get_pareto(points)

for p in points:
    if p in pset:
        plt.plot(p[0], p[1], 'bo')
    else:
        plt.plot(p[0], p[1], 'ro')

print (pset)


plt.title('Objective Space for Vehicle Optimization')
plt.xlabel('Vehicle Price')
plt.ylabel('Vehicle Milage')
plt.show()
