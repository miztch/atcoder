# -*- coding: utf-8 -*-
# B

N, X = map(int, input().split())
A = [int(i) for i in input().split()]

count = 0
target = X
for i in range(N):
    if A[target-1] != 0:
        count += 1
        next_target = A[target-1]
    else:
        break
    A[target-1] = 0
    target = next_target
print(count)
