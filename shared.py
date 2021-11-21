import numpy as np
from copy import copy as copy
import random


def form_obs(sticks):
    x = np.zeros(24)
    x[sticks] = 1
    return x


class Node()
    def __init__(self,obs,moves_remain):
        self.moves_remain = moves_remain
        self.obs = obs
        self.valid_actions = self.get_valid_actions()
        self.children = []
        for action in valid_actions:
            obs_child = obs
            obs_child[action] = 0
            child_moves_remain = self.moves_remain-1
            if child_moves_remain >= 0:
                child_node = Node(obs_child,child_moves_remain)
                self.children.append(child_node)
            else:
                continue

    def __eq__(self,other):
        obs_eq = np.all(self.obs == other.obs)
        mr_eq = self.moves_remain == other.moves_remain
        return obs_eq & mr_eq

    def get_valid_actions(self):
        if self.moves_remain==0:
            return []
        else:
            return np.where(obs)[0]


class Task():
    def __init__(self,init_obs,nsquares,nmoves):
        self.nsquares = nsquares
        self.nmoves = nmoves
        self.head_node = Node(init_obs)
        self.depth = len(np.where(init_obs)[0]) - len(np.where(final_obs)[0])

    def check_final(self,node_obs):
        if self.nmoves != 0:
            return False
        ##
        squares = self.count_squares(node_obs)
        if squares == self.nsquares:
            return True
        else:
            return False


COUNT_SQUARE_IDX = [
    [1,4,5,8], # ones in first row
    [2,5,6,9], # ones in second row
    [3,6,7,10],
    [8,11,12,15],
    [9,12,13,16],
    [10,13,14,17],
    [15,18,19,22],
    [16,19,20,23],
    [17,20,21,24]
]
ROTATION_MATRIX_IDX = [
    18,11,4, # ones in first,second,third
    22,15,8,1,
    19,12,5,
    23,16,9,2,
    20,13,6,
    24,17,10,3,
    21,14,7
]
REFLECTION_MATRIX_IDX = [
    21,14,7,
    24,17,10,3,
    20,13,6,
    23,16,9,2,
    19,12,5,
    22,15,8,1,
    18,11,4
]

rotation_matrix=np.zeros((24,24))
for i,j in enumerate(ROTATION_MATRIX_IDX):
    rotation_matrix[i,j]=1

reflection_matrix=np.zeros((24,24))
for i,j in enumerate(REFLECTION_MATRIX_IDX):
    reflection_matrix[i,j]=1

R=rotation_matrix
T=reflection_matrix
transformation_matrices=[np.eye(24),R,R@R,R@R@R,T,R@T,R@R@T,R@R@R@T]
