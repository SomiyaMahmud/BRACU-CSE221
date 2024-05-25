# -*- coding: utf-8 -*-
"""Task_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UYH5GWe3r9r5IWAHT7_BgQ95RwSH_MX4
"""

inp = open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 07/input 4.txt','r')
out = open('/content/drive/MyDrive/CSE221 Lab(Sp-24)/Lab 07/output 4.txt','w')
N, X = inp.readline().split()
N, X = int(N),int(X)

coins=[int(i) for i in inp.readline().split() ]
dp = [[-1 for i in range(N)] for j in range(X + 1)]

def coin_count(amount,idx,coins):
    if amount == 0:
        return 0
    if idx >= N:
        return float('inf')
    if dp[amount][idx] != -1:
        return dp[amount][idx]

    taken = float('inf')
    not_taken = float('inf')
    if coins[idx] <= amount:
        taken = 1 + coin_count(amount-coins[idx], idx, coins)
    not_taken = coin_count(amount, idx+1, coins)
    dp[amount][idx] = min(taken, not_taken)
    return dp[amount][idx]

res=coin_count(X, 0, coins)

if res==float('inf'):
    out.write(f'{-1}')
else:
    out.write(f'{res}')

inp.close()
out.close()

'''
Firstly a table has been created where rows are the number of coins and columns are target+1.
Then we iterate throuth the matrix by using the formula: if target<coin , then previous column value.
Otherwise, min(previous column value, same row[target - coin]+1). The last box of the table gives the answer
of the number of coins need to make the target.
'''