# -*- coding: utf-8 -*-
"""8_task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OfiwfsBXm-Mqkjji2AaRkqi2HaCttfL4
"""

inp=open('/content/drive/MyDrive/CSE221 Lab/Lab 08/input 1.txt','r')
out=open('/content/drive/MyDrive/CSE221 Lab/Lab 08/output 1.txt','w')
n,m=inp.readline().strip().split(' ')
n,m=int(n),int(m)
mst=[]
for a in range(m):
    u,v,w =inp.readline().strip().split(' ')
    u,v,w=int(u),int(v),int(w)
    mst.append((u, v, w))
mst.sort(key=lambda x:x[2])

par=list(range(n+1))
edges=[]

def kruskal(mst):
    cost=0
    for u, v, w in mst:
        par_u = find_par(u)
        par_v = find_par(v)

        if par_u != par_v:
            par[par_u]=v
            edges.append((u, v, w))
            cost+= w

    return cost

def find_par(s):
    if par[s]==s:
        return s
    par[s]=find_par(par[s])
    return par[s]
min_cost=kruskal(mst)
out.write(f'{min_cost}')

inp.close()
out.close()