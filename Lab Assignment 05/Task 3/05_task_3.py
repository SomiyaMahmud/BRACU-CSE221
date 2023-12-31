# -*- coding: utf-8 -*-
"""05_Task 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pBJVM5_NU1yVmv6r5rvC84SehvN-Fpms
"""

inp = open('/content/drive/MyDrive/CSE221 Lab/Lab 05/input_3.txt', 'r')
out = open('/content/drive/MyDrive/CSE221 Lab/Lab 05/output_3.txt', 'w')
n, m =inp.readline().strip().split(' ')

G = [[] for g in range(int(n)+1)]
n_G = [[] for h in range(int(n)+1)]

for a in range(int(m)):
    cur_line = inp.readline().strip().split(' ')
    u, v = int(cur_line[0]), int(cur_line[1])
    G[u].append(v)
    n_G[v].append(u)

col = ['White']*(int(n)+1)
start = [0]*(int(n)+1)
finish = [0]*(int(n)+1)
time = 0

stack=[]
path=[]
store=[]

def DFS_visit(G):
    for v in range(1,int(n)+1):
        if col[v] == 'White':
            DFS(G, v)

def DFS(G, s):
    global time
    col[s] = 'Grey'
    time += 1
    start[s] = time
    for u in G[s]:
        if col[u] == 'White':
            DFS(G, u)
    col[s] = 'Black'
    time += 1
    finish[s] = time
    stack.append(s)

DFS_visit(G)

col=['White']*(int(n)+1)

def newDFS(G, u):
    col[u] = 'Grey'
    path.append(u)
    for v in G[u]:
        if col[v] == 'White':
            newDFS(G, v)
    col[u] = 'Black'

for u in range(1,int(n)+1):
    if col[u] == 'White':
        newDFS(n_G, u)
        path.sort()
        store.append(path)
        path = []

for t in store:
    out.write(f'{t} \n')
inp.close()
out.close()