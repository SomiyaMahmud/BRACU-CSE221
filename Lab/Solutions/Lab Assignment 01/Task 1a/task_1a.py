# -*- coding: utf-8 -*-
"""Task_1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GllCwx-7Pspq-DcTeJZEaDbYXOJ9b_4j
"""

inp = open("/content/drive/MyDrive/CSE221 Lab(Spring 24)/Lab 01/input 1a.txt","r")
out = open("/content/drive/MyDrive/CSE221 Lab(Spring 24)/Lab 01/output 1a.txt","w")
T = int(inp.readline())

for i in range(T):
    N = int(inp.readline())
    if N % 2 == 0:
        out.write(f'{N} is an Even number.\n')
    else:
        out.write(f'{N} is an Odd number.\n')

inp.close()
out.close()


#Using a conditional statement checked if the number is divisible by 2(means even) or not(means odd).