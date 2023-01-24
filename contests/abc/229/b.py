# -*- coding: utf-8 -*-
# ABC229B

A, B = input().split()

A, B = A[::-1], B[::-1]
EH = 'Easy'

for a, b in zip(A, B):
    S = int(a) + int(b)
    if S > 9:
        EH = 'Hard'
        break

print(EH)
