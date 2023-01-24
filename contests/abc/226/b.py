# -*- coding: utf-8 -*-
# ABC228B

N = int(input())
L = [[]] * N

for i in range(N):
    L[i] = str(list(map(int, input().split())))

s = set(L)

print(len(s))
