# -*- coding: utf-8 -*-
# ABC225A

S = input()

chars = set([c for c in S])

if len(chars) == 3:
    print(3*2*1)
elif len(chars) == 2:
    print(int(3*2*1/2))
else:
    print(1)
