# -*- coding: utf-8 -*-
# ABC229A

S1 = input()
S2 = input()

A = S1 + S2

if A.count('#') >= 3:
    print('Yes')
else:
    if S1[0] == '#' and S2[1] == '#' or S1[1] == '#' and S2[0] == '#':
        print('No')
    else:
        print('Yes')
