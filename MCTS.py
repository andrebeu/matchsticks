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
    def expand_path(self):
        #expands optimal path for as long as possible (i.e. until no children have N>0)

        visited_children=[c for c in self.children if c.N>0]
        if len(visited_children)==0:
            return [self]
        argmax_ucb=np.argmax([UCB_value(c.v,c.N,self.N) for c in visited_children])
        return [self]+visited_children[argmax_ucb].expand_path()



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

            cur=cur.children[np.argmax(ucb_vals)]
            path.append(cur)
            unvisited_children=[x for x in cur.children if x.N==0]

       #step 1.5. current node either is a terminal state (no children), or else it has an unvisited child
      if len(cur.children)==0:
            #value is based on whether the node is a valid end state or not
            v=1.0*task.check_final(cur)
            MCTS_backup(v,path)
            return len(path),v

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

      return len(path),v

def MCTS(task, max_iters=1000,memory=None):
      #performs MCTS iterations until a valid solution path is obtained (or reaches timeout)
      #returns the number of iterations needed to find the solution (or -99 if timeout)

      #Memory is a list of MCTSNodes (or None, in which case pure MCTS is done) from previous tasks
      #whenever we expand a new node in the current task tree, we initialize the v,N fields using
      #the copy of that node in memory (if it exists)

      #does NOT update the memory vector after running the algorithm
      if memory:
          #use the values of the nodes stored in memory to initialize all fields of nodes in the tree
          #dfs traversal of all nodes in tree
          stack=[task.head_node]
          while stack:
              cur,stack=stack[-1],stack[:-1]
              for m in memory:
                  if cur==m:
                      cur.N=m.N
                      cur.v=m.v
                      break
              stack=stack+cur.children

      for n_iters in range(1,max_iters+1):
            found_path_len,v=MCTS_Step(task)
            if task.check_final(task.head_node.expand_path()[-1]):
                  return n_iters

      return -99
def update_memory(task,memory):
    #for each node on the optimal path from head_node,
    #add those nodes to memory, or update their values if they are already there
    #mean to be run after doing tree search on given task

    opt_path=task.head_node.expand_path()
    #if no optimal path was found, then do not update memory values
    if not task.check_final(opt_path[-1]):
        return
    for n in opt_path:
        found_match=False
        for m in memory:
            if n==m:
                found_match=True
                m.N,m.v=n.N,n.v
                break
        if not found_match:
            new_node=MCTSNode(n.obs,n.moves_remain)
            #for memory queries, we only need to know the board statd/number of remaining moves
            new_node.children=[]
            new_node.N=n.N
            new_node.v=n.v
            memory.append(new_node)

