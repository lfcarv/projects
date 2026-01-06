from random import random as r
from matplotlib import pyplot as mpl
from collections import Counter
import numpy as np
from time import sleep


print('players tests')

# k,t = map(int, list(input().split()))
save = False
k,t,o = 7, 1000000, 10
print(k,t)
results = [[] for i in range(o)]


x3 = []
h3 = []

for i in range(t): # Loop for *t* tests
    if i % 10**5 == 0:
        print(i)
    plays = 0
    n = [1 for _ in range(k)]

    for res in range(o): # Loop for every replay after reset
     while True: # Loop until every player has been chosen at least once 
        plays += 1
        n2 = n[:]
        while True: # Loop until a player has been chosen (that is, they are selected and have no additional strikes)
            select = int(r()*k)
            if n2[select] != 1:
                n2[select] -= 1
            else:
                n[select] += 1
                break

        for j in n: # Check if a player hasn't been chosen yet
            if not j:
                break
        else:
            results[res].append(plays)
            h3.append(max(n))
            for bl in range(k): # Reset strikes by subtracting one
                n[bl] -= 1
            plays = 0
            break

        
print('STRIKE DONE')
c = [dict(Counter(results[al])) for al in range(o)]
x1 = [[] for al in range(o)]
h1 = [[] for al in range(o)]
for al in range(o):
    for i in c[al]:
        x1[al].append(i)
        h1[al].append(c[al][i])
print('PLOTTING')
mpl.figure(0)
for al in range(o):
    mpl.bar(x1[al],h1[al],alpha=1/o,label=al)
    mpl.legend()
print('BAR A')
"""
mpl.figure(1)
mpl.hist(h3,100)
print('FIGURE 2, SHOWING!')
"""
mpl.show()

        




    



