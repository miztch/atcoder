# -*- coding:utf-8 -*-

from math import pi
from math import fabs
from decimal import Decimal
list = []
radius = []
N = int(input())
for i in range(N):
    radius.append(int(input()))
radius.sort()

for i in radius:
    list.append((i**2)*float(pi))
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += list[i]
    else:
        ans -= list[i]
print(fabs(ans))
