import numpy as np
from copy import copy as copy
import random
from collections import deque


def treeSearch(task,BFS=True):
    nodet = task.head_node
    deq = deque(nodet)
    deq.extend(nodet.children)
    nitr = 0
    while deq:
        nitr += 1
        print(nodet.obs)
        ## eval node
        if task.check_final(nodet.obs):
            return nitr
        ## expand tree
        if BFS:
            nodet = deq.popleft()
        else:
            nodet = deq.pop()        
        ## extend with children
        deq.extend(nodet.children)
    return "no solution"


