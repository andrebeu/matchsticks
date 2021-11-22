import numpy as np
import matplotlib.pyplot as plt


#order vertices from left to right (e.g. top row is 1,2,3,4, etc.)
#ith row of this list gives the ids of the two vertices that the ith matchstick connects
STICK_TO_VERTEX_IDS=[
    [1,2],
    [2,3],
    [3,4],
    [1,5],
    [2,6],
    [3,7],
    [4,8],
    [5,6],
    [6,7],
    [7,8],
    [5,9],
    [6,10],
    [7,11],
    [8,12],
    [9,10],
    [10,11],
    [11,12],
    [9,13],
    [10,14],
    [11,15],
    [12,16],
    [13,14],
    [14,15],
    [15,16]
]

#xy position of each vertex
vertex_positions=np.vstack((list(range(4))*4,[3]*4+[2]*4+[1]*4+[0]*4)).T


def draw_board(obs):
    #first draw all verticies
    plt.scatter(*vertex_positions.T,c='black')
    for i in np.where(obs)[0]:
        #indices of vertices connected by the stick, *ordered starting from 1*
        a,b=STICK_TO_VERTEX_IDS[i]
        X=np.vstack((vertex_positions[a-1],vertex_positions[b-1]))
        plt.plot(*X.T,c='black')


