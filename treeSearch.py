import numpy as np
from copy import copy as copy
import random
from collections import deque

V = False

def treeSearch(taskL,BFS=True,memory=False):
    if V: print('\nBFS=',BFS,'mem=',memory)
    sol_nodes = []
    sol_times = []
    sol_mode = []
    for task in taskL:
        if V: print('task:')
        nitr = 0
        deq = deque([task.head_node])
        while len(deq):
            nitr += 1
            ## pop candidate node
            if BFS:
                nodet = deq.popleft()
            else:
                nodet = deq.pop()  
            if V: print(nodet.valid_actions)
            ## eval if node is final
            if task.check_final(nodet):
                sol_nodes.append(nodet)
                if type(nodet.parent) != type(None):
                    sol_nodes.append(nodet.parent)
                # record RT
                sol_times.append(nitr)
                # solution mode no memory
                sol_mode.append(0)
                if V: print('sol by search')
                break
            ## check memory
            elif memory:
                sol_in_memory = 0
                for sol_node in sol_nodes:
                    # check tree against memory solutions
                    # if sol_node in deq:
                    # print(sol_nodes)
                    if sol_node == nodet:
                        # record RT
                        sol_times.append(nitr+1)
                        sol_in_memory = True
                        break # from memory for
                if sol_in_memory:
                    if V: print('sol by memory')
                    # solution mode = memory
                    sol_mode.append(1)
                    break # from task while
            ## expand tree
            random.shuffle(nodet.children)
            deq.extend(nodet.children)
    if V: print('cost=',sol_times)
    return sol_times,sol_mode

