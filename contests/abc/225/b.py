# -*- coding: utf-8 -*-
# ABC225B

N = int(input())
edges = [0]*N

for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1] += 1
    edges[b-1] += 1

if max(edges) == N-1:
    print("Yes")
else:
    print("No")
