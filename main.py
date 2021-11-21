import numpy as np
from copy import copy as copy

def form_obs(sticks):
    x = np.zeros(24)
    x[sticks] = 1
    return x

class State():
    """ 
    currently only implements valid action
    """
    def __init__(self,obs,is_final):
        self.obs = obs
        self.va = np.where(obs)[0] # valid actions
        self.is_final = is_final

class Task():
    """ 
    current implementation constructs states on the go
    maybe for more complex task might need to construct 
    task space at initialization
    """
    def __init__(self,init_state_obs,final_states_obs,max_depth=2):
        self.x0 = init_state_obs
        self.xfL = final_states_obs
        # construct state from obs
        self.s0 = State(init_state_obs,is_final=False)
        # self.sfL = [State(xf,is_final=True) for xf in final_states_obs] 
        self.max_depth = max_depth

    def check_final(self,xt):
        return np.any([np.all(xt == x) for x in self.xfL])

    def get_stp(self,state_t,action):
        """ get next state
        """
        st = state_t
        # check valid action
        va = st.va
        if action not in va:
            assert False, 'A=%i not in vA %s'%(action,str(va))
        # make xtp, and stp
        xtp = copy(st.obs)
        xtp[action] = 0
        xtp_is_final = self.check_final(xtp)
        stp = State(xtp,is_final=xtp_is_final)
        return stp


def BFSPlay(task,max_wsteps=5):
    """ no memory implementation
    """
    s0 = st = task.s0
    nsteps = 0
    wsteps = 0
    depth = 0
    while wsteps < max_wsteps: 
        wsteps +=1
        # check all nodes in current depth
        for at in st.va:
            print('a%i'%nsteps,at)
            stp = task.get_stp(st,at)
            nsteps +=1
            if stp.is_final:
                return nsteps
        # if nothing found, step down
        st = stp
        depth += 1
        # safety against 
    return "no solution found"

def DFSPlay(task):

    return None

