from PIL import Image
import numpy as np

class ExplorationSimulator():

    def __init__(self):
        im = Image.open("src/exploration_gazebo/materials/hurricanes.png")
        self.map_image = im.convert('RGB')
        self.map_width, self.map_height = self.map_image.size

        self.curr_pos = ( int(self.map_width/2.0), int(self.map_height/2.0))

    def getLimits(self):
        return (self.map_width,self.map_height)

    def getPose(self,):
        return self.curr_pos

    def moveTo(self,x,y):
        vector = (x-self.curr_pos[0], y-self.curr_pos[1])
        new_x = self.curr_pos[0]
        new_y = self.curr_pos[1]
        seen_pixels = []

        while new_x != x:
            new_x = new_x + np.sign(x-new_x)
            y_targ = self.curr_pos[1] + vector[1]*(new_x-self.curr_pos[0])/vector[0]

            while new_y != y_targ:
                new_y = new_y + np.sign(y_targ-new_y)
                r, g, b = self.map_image.getpixel((new_x,new_y))
                seen_pixels.append([new_x,new_y,r])

        self.curr_pos = (x,y)
        return seen_pixels