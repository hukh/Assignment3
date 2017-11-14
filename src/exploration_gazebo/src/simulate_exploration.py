''' 
File simulate_exploration.py:

Provides a simple simulation interface for a robot exploring
a 2D world with realistic data about the windspeed 
of hurricanes.

An exmample of the client code that properly interfaces
with this simulator can be found in exploration_node.py
in the same folder.

Author: David Meger
Date: November, 2017
'''

import sys
from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt
import copy

class ExplorationSimulator():

    def __init__(self):
        im = Image.open("src/exploration_gazebo/materials/hurricanes.png")
        self.map_image = im.convert('RGB')
        self.np_map = np.array(self.map_image)[:,:,0]
        self.map_width, self.map_height = self.map_image.size

        self.curr_pos = ( random.randint(0,self.map_width-1), random.randint(0,self.map_height-1))
        self.distance_traveled = 0
        self.path = []

        self.reconstruction_result = []
        self.maximization_result = []

    def getLimits(self):
        return (self.map_width,self.map_height)

    def getPose(self,):
        return self.curr_pos

    ''' This is the most important function that you must call 
        repeatedly to explore the environment. 

        Ensure that you pass in (x,y) values that fall within
        (0,0) and (width,height) as returned by getLimits.abs
        
        The return value of this function is information about
        the straight line path that the robot follows, represented
        as a  list of lists. There is one entry in the outer
        list for each pixel visited. Each inner list has 
        3 elements: x-coord, y-coord, and the value of the image
        at that x,y. 
    ''' 
    def moveTo(self,x,y):
        vector = (x-self.curr_pos[0], y-self.curr_pos[1])
        new_x = self.curr_pos[0]
        new_y = self.curr_pos[1]
        observation = []
        r, g, b = self.map_image.getpixel((new_x,new_y))
        observation.append([new_x,new_y,r])

        while new_x != x:
            new_x = new_x + np.sign(x-new_x)
            y_targ = self.curr_pos[1] + vector[1]*(new_x-self.curr_pos[0])/vector[0]

            r, g, b = self.map_image.getpixel((new_x,new_y))
            self.path.append([new_x,new_y])
            self.distance_traveled = self.distance_traveled + 1
            observation.append([new_x,new_y,r])
            while new_y != y_targ:
                new_y = new_y + np.sign(y_targ-new_y)
                r, g, b = self.map_image.getpixel((new_x,new_y))
                self.path.append([new_x,new_y])
                self.distance_traveled = self.distance_traveled + 1 
                observation.append([new_x,new_y,r])

        self.curr_pos = (x,y)
        return observation

    def getPath(self):
        return self.path

    def getDistance(self):
        return self.distance_traveled

    def reportMaximum( self, x, y ): 
        self.maximization_result.append( [self.distance_traveled, self.np_map[y,x]] )

    def reportReconstruction( self, im ):
        diff = np.sum( np.abs( self.np_map.transpose() - im ) )
        self.reconstruction_result.append( ( self.distance_traveled, diff) )

    def saveMaximumGraph(self, fname):
        plt.figure()
        plt.plot( [ res[0] for res in self.maximization_result ], [ res[1] for res in self.maximization_result ], 'r-' )
        plt.plot( [ min([ res[0] for res in self.maximization_result ]), max([ res[0] for res in self.maximization_result ])], [183,183], 'b--' )
        axes = plt.gca()
        axes.set_ylim([-10,200])
        plt.xlabel( "Distance traveled")
        plt.ylabel( "Value of maximum guess")
        plt.title("Maximum guess vs Distance (optimal is 183, but over 160 is awesome!)")
        plt.savefig( fname )

    def saveReconstructionGraph(self, fname):
        plt.figure()
        plt.plot( [ res[0] for res in self.reconstruction_result ], [ res[1] for res in self.reconstruction_result ] )
        plt.xlabel( "Distance traveled")
        plt.ylabel( "Reconstruction error")
        plt.title("Reconstruction error vs Distance (can you hit 0?)")
        plt.savefig( fname )

    def saveExplorationPath(self,fname):
        im_path = copy.deepcopy(self.map_image)

        for p in self.path:
            im_path.putpixel((p[0],p[1]),(255,0,0))

        plt.figure()
        plt.title("The exploration path travelled")
        plt.imshow(im_path)
        plt.savefig(fname)
