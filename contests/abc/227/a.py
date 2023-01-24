# -*- coding: utf-8 -*-
# ABC227A

N, K, A = map(int, input().split())

queue = [i for i in range(A, N+1)] + [i for i in range(1, A)]
if K > N:  # 1¿Í1Ëç°Ê¾å
    mod = K % N
    print(queue[mod-1])
elif K == N:
    print(queue[-1])
else:
    print(queue[K-1])
