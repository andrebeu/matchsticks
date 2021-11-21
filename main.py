import numpy as np
from copy import copy as copy

def form_obs(sticks):
    x = np.zeros(24)
    x[sticks] = 1
    return x

class Task():
    def __init__(self,init_state,final_states,max_depth=2):
        self.s0 = init_state
        self.sfL = final_states # list 
        self.max_depth = max_depth

class State():
    def __init__(self,obs,depth,is_final=False):
        self.is_final = is_final # check if final
        self.obs = obs
        self.depth = depth
        self.va = np.where(obs)[0] # valid actions

    def get_stp(self,action):
        """ action is index
        indicates what board entry to zero out
        """
        if action not in self.va:
            assert False, 'A=%i not in %s'%(action,str(self.va))
        obs_stp = copy(self.obs)
        obs_stp[action] = 0
        stp = State(obs=obs_stp,depth=self.depth+1)
        return stp


def BFSPlay(task):
    s0 = task.s0
    st = s0 
    depth = st.depth
    nsteps = 0
    wsteps = 0
    while depth<=task.max_depth:
        wsteps +=1
        va = st.va
        # check all nodes in current depth
        for at in va:
            print('a%i'%nsteps,at)
            stp = st.get_stp(va)
            nsteps +=1
            if stp.is_final:
                return nsteps
        # if nothing found, step down
        st = stp
        depth = st.depth
        # safety
        if wsteps > 5:
            assert False, 'possible infinite while'



