''' 
File exploration_node.py:

This is a very simple example of how to explore using 
the Assignment 3 simulator. 

Author: David Meger
Date: November, 2017
'''

import simulate_exploration
import random
import numpy as np
import matplotlib.pyplot as plt
import copy

sim = simulate_exploration.ExplorationSimulator()

limits = sim.getLimits()
p = sim.getPose()
print "Random start position was: ", p

res_img = np.zeros((limits[0],limits[1]))
max = [0,0,0]
max_pos = []

for i in range(0,1000):
    if i % 100 == 0: 
        print "Exploration iteration: ", i
    targ_x = random.randint(0,limits[0]-1)
    targ_y = random.randint(0,limits[1]-1)
    res = sim.moveTo(targ_x,targ_y)

    # Note the loop through the path followed by the robot.
    # Each r holds x, y, value for one pixel along the path.
    # This would be your data to learn from (GP or other).
    for r in res:
        res_img[r[0], r[1]] = r[2]
        if r[2] > max[2]:
            max = copy.deepcopy(r)
            max_pos = [ r[0], r[1] ]

    sim.reportMaximum( max_pos[0], max_pos[1] )
    sim.reportReconstruction( res_img )

print "The maximum value I found was at pos: (",max[0],",",max[1],") val: ", max[2]
print "See the images for more details: max_plot.png, reconst_plot.png, path_plot.png, final_reconstruction.png"
        
sim.saveMaximumGraph( 'max_plot.png' )
sim.saveReconstructionGraph( 'reconst_plot.png')
sim.saveExplorationPath('path_plot.png')

plt.figure()
plt.title("Final reconstruction result")
plt.imshow(255-res_img.transpose(), cmap="Greys", interpolation='nearest' )
plt.savefig('final_reconstruction.png')