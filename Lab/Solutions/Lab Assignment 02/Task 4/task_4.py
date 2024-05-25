# -*- coding: utf-8 -*-
"""task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iyLSigYJr8M-0EXL7AOUxUvg5O71ofjz
"""

inp=open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 02/input 4.txt','r')
out=open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 02/output 4.txt','w')
n , m = inp.readline().split()
n , m=int(n) ,int(m)
G=[]

for a in range(n):
    s , e = inp.readline().split(' ')
    s , e = int(s),int(e)
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

"""
The solution of this task is similar to task 3 but there is a little change needed. Firstly, I take a list
of the length of the assigned person. Each time I compare the difference between the starting
time and the finish time of the number of assigned persons and select who has the less amount of
difference.
"""