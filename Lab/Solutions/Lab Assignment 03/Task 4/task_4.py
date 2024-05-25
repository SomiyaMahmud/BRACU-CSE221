# -*- coding: utf-8 -*-
"""task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iyLSigYJr8M-0EXL7AOUxUvg5O71ofjz
"""



#4
inp = open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 03/input 4.txt', 'r')
out = open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 03/output 4.txt', 'w')

N = int(inp.readline())
arr = [int(i) for i in inp.readline().split()]

def get_max(arr):
    n=len(arr)
    mid=n//2
    if n==1:
        return  -999999
    elif n==2:
        return arr[0]+((arr[1])**2)
    else:
      left_max=get_max(arr[:mid])
      right_max=get_max(arr[mid:])

    maxl=max(arr[:mid])
    right=arr[mid:]
    maxr=right[0]
    for i in range(len(right)):
        if abs(right[i])>maxr:
            maxr=abs(right[i])
    cross_max=maxl+(maxr**2)

    return max(left_max,right_max,cross_max)
out.write(f"{get_max(arr)}")
inp.close()
out.close()

"""
Firstly, check the length of the array. If the length is 1 then return a big unrealistic number which doesn't
affect the output of the code. If the length is 2 then return the value of the expression 'A[i] + A[j]^2'.
If the length is more than 2 then first find the mid and then divide the array and find the maximum value of the left
side along with the right side recursively. For the cross max, we find the left max using the built-in
max function and the right max using the loop and abs function because we need the absolute
value and return the value of the expression. Lastly using the built-in max function find the max
value of the expression from left max, right max, and cross max.
"""