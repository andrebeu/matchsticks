import numpy as np
from copy import copy as copy
import random

from shared import Node,Task

class MCTSNode(Node):
    def __init__(self,obs,moves_remain):
        super(MCTSNode,self).__init__(obs,moves_remain)

      #need to reconstruct tree, because children should be MCTSNode, rather than Node
        self.children=[]
        for action in self.valid_actions:
            obs_child = copy(obs)
            obs_child[action] = 0
            child_moves_remain = self.moves_remain-1
            if child_moves_remain >= 0:
                child_node = MCTSNode(obs_child,child_moves_remain)
                self.children.append(child_node)
            else:
                continue

        self.v=0 #estimated value of node
        self.N=0 #number of times node has been visited
class MCTSTask(Task):
      def __init__(self,obs,nsquares,nmoves):
            super(MCTSTask,self).__init__(obs,nsquares,nmoves)
            self.head_node=MCTSNode(obs,nmoves)


def MCTS_backup(value,path):
      #updates the estimated values and state counts of nodes aong te path
      for n in path:
            n.v+=value
            n.N+=1

def UCB_value(v,N,N_parent,C=np.sqrt(2)):
    #v, estimated value
    #n, number of times current node has been visited
    #N_parent, number of times parent has been visited
    return v/N+C*np.sqrt(2*np.log(N_parent)/N)

def MCTS_Step(task):
      #performs one iteration of MCTS, and updates the task.head_node in place
      #returns 1 if the search led to a solution state (with no simulation), else 0

      #step 1: selection. proceed down the tree until we find either a leaf node, or a node with an unvisited child
      cur=task.head_node
      path=[cur]
      unvisited_children=[x for x in cur.children if x.N==0]
      while len(unvisited_children)==0 and len(cur.children)>0:
            ucb_vals=[UCB_value(x.v,x.N,cur.N) for x in cur.children]
            cur=ucb_vals[np.argmax(ucb_vals)]
            path.append(cur)
            unvisited_children=[x for x in cur.children if x.N==0]

       #step 1.5. current node either is a terminal state (no children), or else it has an unvisited child
      if len(cur.children)==0:
            #value is based on whether the node is a valid end state or not
            v=1.0*task.check_final(cur.obs)
            MCTS_backup(v,path)
            #return value indicates that we found a solution path
            return 1

      #if we get here, then cur has >=1 child node that has not been visited yet

      #step 2: expansion. choose an unvisited child and add it to the tree (mark as visited)
      new_child=random.choice(unvisited_children)
      new_child.N=1

      #step 3: simulation. make random moves from new_child until there are no moves left
      #record whether it is a valid goal state or not
      end_state=new_child
      while end_state.children:
            end_state=random.choice(end_state.children)
      v=1.0*task.check_final(end_state)

      #step 4: backup. update the values and visit couts of nodes along the path
      MCTS_backup(v,path)

      return 0

def MCTS(task, max_iters=1000):
      #performs MCTS iterations until a valid solution path is obtained (or reaches timeout)
      #returns the number of iterations needed to find the solution (or -99 if timeout)

      for n_iters in range(1,max_iters+1):
            found_path=MCTS_Step(task)
            if found_path>0:
                  return n_iters
      return -99