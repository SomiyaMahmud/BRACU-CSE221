# -*- coding: utf-8 -*-
"""task_1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iyLSigYJr8M-0EXL7AOUxUvg5O71ofjz
"""

inp = open("/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 02/input 1b.txt", "r")
out = open("/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 02/output 1b.txt", "w")
temp = inp.readline().split()
N, S =int(temp[0]) , int(temp[1])
num = inp.readline().split()

l = 0
r = N-1
flag= False

while (l < r):
    if int(num[l]) + int(num[r]) == S:
        out.write(f'{l+1} {r+1}')
        flag = True
        break
    elif int(num[l]) + int(num[r]) > S:
        r = r - 1
    elif int(num[l]) + int(num[r]) < S:
        l = l + 1
if flag == False:
    out.write("IMPOSSIBLE")
inp.close()
out.close()

"""
Use 2 pointer method here. One is the leftmost element and another one is rightmost element. Add the pointers and check if they are equal to the target.
If sum is greater then the tanget then decrease the right pointer by 1 and sum is less then the tanget then increase the left pointer by 1 and if equal then print.
"""