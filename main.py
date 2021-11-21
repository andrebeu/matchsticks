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

class Agent():

    def __init__(self):
        None

    def act(self,st):
        valid_actions = st.valid_actions
        ## use memory
        ## randomly act
        return st,stp

    def get_stp(self,st,at,step_down):
        """ """



class BFSAgent(Agent):
    def __init__(self):
        None

    def get_stp(self,st,at):
        """ 
        next state is same as current state
        unless exhausted current layer
        """
        return get_stp

class DFSAgent():
    def __init__(self):
        None

    def get_stp(self,st,at):
        """ 
        next state is one layer down
        and depends on action
        """
        stp = None # stp is one node down

    



