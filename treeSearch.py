import numpy as np
from copy import copy as copy
import random
from collections import deque


def treeSearch(taskL,BFS=True,memory=False):
    sol_nodes = []
    sol_times = []
    for task in taskL:
        nitr = 0
        deq = deque()
        nodet = task.head_node
        deq.append(nodet)
        while len(deq):
            # print(sol_nodes)
            nitr += 1
            ## take candidate node
            if BFS:
                nodet = deq.popleft()
            else:
                nodet = deq.pop()  
            # print(np.where(nodet.obs))
            ## eval node
            if task.check_final(nodet):
                sol_nodes.append(nodet)
                sol_times.append(nitr)
                break
            ## check memory
            elif memory:
                sol_in_memory = 0
                for sol_node in sol_nodes:
                    ## consider recognition failure w.p.p                    
                    if sol_node in deq:
                        ## keep track of number of memory operations
                        sol_times.append(nitr+1)
                        sol_in_memory = 1
                        break # from memory for
                if sol_in_memory:
                    # print('memory sol')
                    break # from task while
            ## expand tree
            random.shuffle(nodet.children)
            deq.extend(nodet.children)
    return sol_times
