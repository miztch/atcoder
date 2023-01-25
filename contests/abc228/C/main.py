# -*- coding: utf-8 -*-
# C

N, K = map(int, input().split())
P = [sum(map(int, input().split())) for student in range(N)]

P_sorted = sorted(P, reverse=True)

for i in range(N):
    if P[i] + 300 >= P_sorted[K-1]:
        print("Yes")
    else:
        print("No")
