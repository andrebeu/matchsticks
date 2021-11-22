import numpy as np
from copy import copy as copy
import random


TreeSearch(task)


def BFSplay(task,max_wsteps=5):
    """ 
    BFS with no memory implementation
    max_wsteps (max while steps) is just a safety break
    """
    s0 = st = task.s0
    nsteps = 0
    wsteps = 0
    depth = 0
    while wsteps < max_wsteps: 
        wsteps +=1
        # check all nodes in current depth
        va = copy(st.va)
        random.shuffle(va) 
        # loop over possible next states
        for at in va:
            # print('a%i'%nsteps,at)
            stp = task.get_stp(st,at)
            nsteps +=1
            if stp.is_final:
                return nsteps
        # if nothing found, step down
        st = stp
        depth += 1
    return "no solution found"
