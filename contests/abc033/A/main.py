# -*- coding:utf-8 -*-

N = input()
L = [n for n in N]
L = set(L)
if len(list(L)) == 1:
    print('SAME')
else:
    print('DIFFERENT')
