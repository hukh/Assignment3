import simulate_exploration
import random
import numpy as np
import matplotlib.pyplot as plt

sim = simulate_exploration.ExplorationSimulator()

limits = sim.getLimits()
print limits

p = sim.getPose()
print p
res_img = np.zeros((limits[0],limits[1]))

for i in range(0,10000):
    targ_x = random.randint(0,limits[0]-1)
    targ_y = random.randint(0,limits[1]-1)
    res = sim.moveTo(targ_x,targ_y)
    for r in res:
        res_img[r[0], r[1]] = r[2]
        
plt.imshow(res_img,cmap="Greys", interpolation='nearest')
plt.show()
