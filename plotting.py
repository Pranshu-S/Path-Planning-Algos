import os
import sys
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import env

class Plotting:
    def __init__(self, start):
        self.env = env.env()
        self.obs = self.env.obs_map()
        self.start = start

    def plot_grid(self,name):
        obs_x = [x[0] for x in self.obs]
        obs_y = [x[1] for x in self.obs]

        plt.plot(obs_x,obs_y,"sk")
        plt.title(name)
        plt.axis("equal")
        
        ax = subplot(111)

        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
        ax.xaxis.set_minor_locator(MultipleLocator(2.5))

        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_minor_locator(MultipleLocator(2.5))

        ax.xaxis.grid(True,'minor')
        ax.yaxis.grid(True,'minor')
        ax.xaxis.grid(True,'major',linewidth=2)
        ax.yaxis.grid(True,'major',linewidth=2)
    
    def ret_map(self):
        return self.obs

    def ret_range(self):
        return self.env.x_range, self.env.y_range
    
    def animation(self, visited, name):
        self.plot_grid(name)
        self.plot_visited(visited)
        # self.plot_path(path)
        plt.show()
    def plot_visited(self, visited, cl='gray'):
        # if self.start in visited:
        #     visited.remove(self.start)
            
        count = 0

        for cells in visited:
            count += 1
            plt.plot(cells[0], cells[1], color=cl, marker='o')
            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40
            
            length = 15

            if count % length == 0:
                plt.pause(0.0000001)
        plt.pause(0.01)


    @staticmethod
    def color_list():
        cl_v = ['silver',
                'wheat',
                'lightskyblue',
                'royalblue',
                'slategray']
        cl_p = ['gray',
                'orange',
                'deepskyblue',
                'red',
                'm']
        return cl_v, cl_p

    @staticmethod
    def color_list_2():
        cl = ['silver',
              'steelblue',
              'dimgray',
              'cornflowerblue',
              'dodgerblue',
              'royalblue',
              'plum',
              'mediumslateblue',
              'mediumpurple',
              'blueviolet',
              ]
        return cl
        