import numpy as np


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
    def __init__(self,obs):
        self.is_final = None # check if final
        self.obs = obs
        self.va = np.where(obs)[0] # valid actions

    def get_stp(self,action):
        """ action is index
        indicates what board entry to zero out
        """
        if action not in self.va:
            assert False, 'A=%i not in %s'%(action,str(self.va))
        obs = state.obs
        obs[action] = 0
        return State(obs)


def BFSPlay(task):
    s0 = task.init_state
    st = s0
    depth = st.depth
    while depth<=task.max_depth:
        depth = st.depth
        va = st.valid_actions
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



