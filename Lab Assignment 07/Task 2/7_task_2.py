# -*- coding: utf-8 -*-
"""7_task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wJq_J_j0b-yKLHblJGLnHgHxPzZD6r3l
"""

inp=open('/content/drive/MyDrive/CSE221 Lab/Lab 07/input 2.txt','r')
out=open('/content/drive/MyDrive/CSE221 Lab/Lab 07/output 2.txt','w')
n,m=inp.readline().strip().split(' ')
n,m=int(n),int(m)
G=[]

for a in range(n):
    s,e=inp.readline().strip().split(' ')
    s,e=int(s),int(e)
    G.append((s, e))
G.sort(key=lambda x:x[1])

task=[0]*m
count=0

def assinged_activities(arr,m):
    global count
    for i in range(len(arr)):
        start,end=G[i]
        assign=float('inf')
        a_idx=-1
        for j in range(m):
            if task[j]<=start:
                if assign > start-task[j]:
                    assign=start-task[j]
                    a_idx=j

        if assign !=float('inf'):
            task[a_idx]=end
            count+=1

assinged_activities(G,m)
out.write(f'{count}')
inp.close()
out.close()