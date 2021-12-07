import numpy as np
from copy import copy as copy
import random
from collections import deque

V = True

def treeSearch(taskL,BFS=True,memory_flag=False):
    if V: print('\nBFS=',BFS,'mem=',memory)
    memory = []
    sol_times = []
    sol_mode = []
    sol_nodes = []

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
                memory.append(nodet)
                if type(nodet.parent) != type(None):
                    memory.append(nodet.parent)
                # record RT
                sol_times.append(nitr)
                sol_nodes.append(nodet)
                # solution mode no memory
                sol_mode.append(0)
                if V: print('sol by search')
                break
            ## check memory
            elif memory_flag:
                sol_in_memory = 0
                for sol_node in memory:
                    # check tree against memory solutions
                    # if sol_node in deq:
                    # print(memory)
                    if sol_node == nodet:
                        # record RT
                        sol_times.append(nitr+1)
                        sol_nodes.append(nodet)
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
    return {'rt':sol_times,'smode':sol_mode,'solution_nodes':sol_nodes}

