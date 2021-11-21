import numpy as np


def play(agent,task):
    st = stp = task.s0
    nsteps = 0
    while not stp.is_final:
        st,stp = agent.act(st)
        nsteps +=1
    return nsteps

class Task():
    def __init__(self,init_state):
        s0 = self.init_state

class State():
    def __init__(self):
        self.is_final = None



def BFSPlay(task):
    s0 = task.init_state
    st = stp = s0
    va = st.valid_actions
    depth = st.depth
    while depth<=task.max_depth:
        depth = st.depth
        # check all nodes in current depth
        for at in va:
            stp = st.get_stp(va)
            nsteps +=1
            if stp.is_final:
                return nsteps
        # if nothing found, step down
        st = stp
        # safety
        if nsteps > 1000:
            assert False



