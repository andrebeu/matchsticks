import numpy as np
from copy import copy as copy
import random


def form_obs(sticks):
    x = np.zeros(24)
    x[sticks] = 1
    return x


class Node():
    def __init__(self,obs,moves_remain,parent=None):
        self.moves_remain = moves_remain
        self.obs = obs
        self.valid_actions = self.get_valid_actions()
        self.children = []
        self.parent = parent
        for action in self.valid_actions:
            obs_child = copy(obs)
            obs_child[action] = 0
            child_moves_remain = self.moves_remain-1
            if child_moves_remain >= 0:
                child_node = Node(obs_child,child_moves_remain,parent=self)
                self.children.append(child_node)
            else:
                continue

    def __eq__(self,other):
        """ modify to take equivalent set into account
        """
        obs_eq=np.any(
            [np.all(self.obs == np.dot(t,other.obs)
                ) for t in transformation_matrices]
        )
        mr_eq = self.moves_remain == other.moves_remain
        return obs_eq & mr_eq

    def get_valid_actions(self):
        return np.where(self.obs)[0]


class Task():
    def __init__(self,init_obs,nsquares,nmoves):
        self.nsquares = nsquares
        self.nmoves = nmoves
        self.head_node = Node(init_obs,nmoves)
        # self.depth = len(np.where(init_obs)[0]) - len(np.where(final_obs)[0])

    def check_final(self,node):
        if node.moves_remain != 0:
            return False
        ## count squares
        squares = self.count_squares(node)
        if squares == self.nsquares:
            return True
        else:
            return False

    def count_squares(self,node):
        nsquares = np.sum(Smat@node.obs==4)
        return nsquares

COUNT_SQUARE_IDX = [
    [1,4,5,8],
    [2,5,6,9],
    [3,6,7,10],
    [8,11,12,15],
    [9,12,13,16],
    [10,13,14,17],
    [15,18,19,22],
    [16,19,20,23],
    [17,20,21,24]
]
Smat = COUNT_SQUARE_MATRIX = np.zeros([9,24])
for idx_row,idx_col in enumerate(COUNT_SQUARE_IDX):
    COUNT_SQUARE_MATRIX[idx_row,np.array(idx_col)-1] = 1

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
    rotation_matrix[i,j-1]=1

reflection_matrix=np.zeros((24,24))
for i,j in enumerate(REFLECTION_MATRIX_IDX):
    reflection_matrix[i,j-1]=1

R=rotation_matrix
T=reflection_matrix
transformation_matrices=[np.eye(24),R,R@R,R@R@R,T,R@T,R@R@T,R@R@R@T]
