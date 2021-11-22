import numpy as np
from copy import copy as copy
import random
from collections import deque


def treeSearch(task,BFS=True):
    nodet = task.head_node
    deq = deque()
    deq.append(nodet)
    # deq.append(nodet)
    # deq.extend(nodet.children)
    nitr = 0
    while len(deq):
        nitr += 1
        ## expand tree
        if BFS:
            nodet = deq.popleft()
        else:
            nodet = deq.pop()  
        # print(np.where(nodet.obs))
        ## eval node
        if task.check_final(nodet):
            return nitr
        ## extend with children
        random.shuffle(nodet.children)
        deq.extend(nodet.children)
    return -99


