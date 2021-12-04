import numpy as np
import shared
import utils
import random

#remove 1 piece and 0 squares
#1 target square
LOOSE_END_BOARD=np.zeros(24)
LOOSE_END_BOARD[[5,8,11,12,15]]=1

#remove 1 piece and 0 squares
#1 target square
JOIN_BOARD=np.zeros(24)
JOIN_BOARD[[7,8,9,10,11,12,13,14,16]]=1

#remove 1 piece and 1 square
#2 target squares
OUTER_BOARD=np.zeros(24)
OUTER_BOARD[[7,8,9,10,11,12,13,14,15,16]]=1

#remove 1 piece and 2 squares
#1 target square
MIDDLE_BOARD=np.zeros(24)
MIDDLE_BOARD[[7,8,9,10,11,12,13,14,15,16]]=1

def generate_board(tactic_name,n_extra_sticks,contiguous=True):
    #tactic name should be one of loose_end,join,outer,middle
    #n_extra_sticks: number of randomly=placed sticks to add to board
    #contiguous: whether the new sticks are connectd to remaining sticks

    #returns instance of shared.Task class

    #for now, all rules involve removing only 1 square
    #so the number of moves allowed in the generated problem is 1+number of extra


    if tactic_name=='loose_end':
        obs0,n_squares,n_moves=LOOSE_END_BOARD,1,n_extra_sticks+1
    elif tactic_name=='join':
        obs0,n_squares,n_moves=JOIN_BOARD,1,n_extra_sticks+1
    elif tactic_name=='outer':
        obs0,n_squares,n_moves=OUTER_BOARD,2,n_extra_sticks+1
    elif tactic_name=='middle':
        obs0,n_squares,n_moves=MIDDLE_BOARD,1,n_extra_sticks+1
    else:
        raise ValueError('invalid tactic name')
    obs=np.copy(obs0)
    if contiguous:
        occupied_vertices=[]
        for i in np.where(obs0)[0]:
            occupied_vertices=occupied_vertices+utils.STICK_TO_VERTEX_IDS[i]
        #correct for 1-indexing in STICK_TO_VERTEX_IDS
        occupied_vertices=np.unique(occupied_vertices)-1

        available_sticks=[]#sticks not already in the board with >=1 occupied endpoint
        for stick_id in range(24):
            if obs0[stick_id]>0:
                continue
            v0,v1=utils.STICK_TO_VERTEX_IDS[stick_id]
            v0,v1=v0-1,v1-1
            if v0 in occupied_vertices or v1 in occupied_vertices:
                available_sticks.append(stick_id)

        for _ in range(n_extra_sticks):
            new_stick=random.choice(available_sticks)
            obs[new_stick]=1
            available_sticks=[x for x in available_sticks if x!=new_stick]
            new_vertices=utils.STICK_TO_VERTEX_IDS[new_stick]
            new_vertices=np.array(new_vertices)-1
            occupied_vertices=np.unique(np.concatenate((occupied_vertices,new_vertices)))
    else:
        available_sticks = np.where(obs0<1)[0]
        np.random.shuffle(available_sticks)
        new_sticks=available_sticks[:n_extra_sticks]
        obs[new_sticks]=1

    return shared.Task(obs,n_squares,n_moves)



