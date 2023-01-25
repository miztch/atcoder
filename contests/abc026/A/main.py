# -*- coding:utf-8 -*-

A = int(input())
list = []
for i in range(A):
    x = i
    y = A - i
    list.append(x*y)
print(max(list))
