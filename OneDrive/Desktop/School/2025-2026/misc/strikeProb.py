from random import random as r
from collections import Counter
import numpy as np


k = 6
# NOTES! Permuation Invariant, Also Memoize whoooooo!
memo = {}



def tran (i):
    global k
    mat = np.identity(k)
    mat[:,i] *= 0
    mat[:,i] += 1
    mat[:,i] *= 1/k
    return mat

def newMat (state):
    global k
    global memo
    if str(state) in memo:
        return memo[str(state)]
    assert(len(state) == k)
    if sum(state) == 1:
        return tran(state.index(1))
    x = []
    for i in range(k):
        if state[i] == 0:
            x.append([int(j == i) for j in range(k)])
        else:
            newState = state[:]
            newState[i] -= 1
            x.append(newMat(newState) @ [1/k for i in range(k)])
    memo[str(state)] = np.array(x).T
    return memo[str(state)]



n = [0 for i in range(k)]
probs = np.identity(k)
while True:
        n2 = n[:]
        while True:
            select = int(r()*k)
            if n2[select] != 0:
                n2[select] -= 1
            else:
                n[select] += 1
                break
        for j in n:
            if not j:
                o = newMat(n) @ np.array([1/k for i in range(k)])
                print(o*k**(sum(n)+1))
                break
        else:  
            break