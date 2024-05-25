# -*- coding: utf-8 -*-
"""Task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GllCwx-7Pspq-DcTeJZEaDbYXOJ9b_4j
"""

inp = open("/content/drive/MyDrive/CSE221 Lab(Spring 24)/Lab 01/input 3.txt", "r")
out = open("/content/drive/MyDrive/CSE221 Lab(Spring 24)/Lab 01/output 3.txt", "w")
N = int(inp.readline())
Si = [int(i) for i in inp.readline().split()]
Sm = [int(i) for i in inp.readline().split()]


for i in range(N):
    idx=i
    for j in range(i+1,N):
        if Sm[j]>Sm[idx]:
            idx=j
    Sm[i], Sm[idx] = Sm[idx], Sm[i]
    Si[i], Si[idx] = Si[idx], Si[i]

dic={}
for k in range(N):
    if Sm[k] in dic:
        dic[Sm[k]].append(Si[k])
    else:
        dic[Sm[k]] = [Si[k]]


for key, value in dic.items():
    for val in sorted(value):
        out.write(f'ID: {val} Marks: {key}\n')

inp.close()
out.close()

#For the minimum swap use the selection sort to sort the marks and id
#In a dictionary marks are the keys and list of the ids are the values.
#sort the values of the id list and print the id based on their marks.