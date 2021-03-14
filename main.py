import env,plotting
import numpy as np
import math

def get_matrix(obstacles):

    node_adj = np.zeros([10,10])

    for obs in obstacles:
        z_x = math.floor(math.floor(obs[0])/5)
        z_y = math.floor(math.floor(obs[1])/5)
        if z_x < 0:
            z_x = 0
        elif z_y < 0:
            z_y = 0
        node_adj[9-z_y,z_x] = 1

    sub_node_adj = np.zeros([20,20])

    for obs in obstacles:
        z_x = math.floor(math.floor(obs[0])/2.5)
        z_y = math.floor(math.floor(obs[1])/2.5)
        if z_x < 0:
            z_x = 0
        elif z_y < 0:
            z_y = 0
        sub_node_adj[19-z_y,z_x] = 1

    return node_adj,sub_node_adj

def get_visited(start, node_matrix,sub_node_matrix):
    visit = []
    visit.append(start)

    
    return visit


def main():
    start = [12.5,7.5]
    plot = plotting.Plotting(start)
    plot.plot_grid("Map")


    # adj_matrix_node, adj_matrix_sub_node = get_matrix(plot.ret_map(),plot.ret_range())
    node_matrix, sub_node_matrix = get_matrix(plot.ret_map())
    print(node_matrix)
    print(sub_node_matrix)

    visited = get_visited(start, node_matrix, sub_node_matrix)
    print(visited)
    # visited = [[2,3],[2,4],[2,5]]
    # print(visited)
    plot.animation(visited,"Map")

if __name__ == '__main__':
    main()
    