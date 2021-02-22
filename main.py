import env,plotting
import numpy as np
import math

def get_matrix(obstacles, ranges):
    major_adj = np.zeros([51,51])

    for i in range(ranges[0]):
        for j in range(ranges[1]):
            for elements in obstacles:
                if elements[0] == i and elements[1] == j:
                    major_adj[i,j] = 1
                    break
    
    print(major_adj)


def main():
    plot = plotting.Plotting()
    plot.plot_grid("Map")

    # adj_matrix_node, adj_matrix_sub_node = get_matrix(plot.ret_map(),plot.ret_range())
    # get_matrix(plot.ret_map(),plot.ret_range())

if __name__ == '__main__':
    main()
    