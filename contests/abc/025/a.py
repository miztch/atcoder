# -*- coding:utf-8 -*-

S = []
D = []

N, A, B = map(int, input().split())

i = 0
while i < N:
    s, d = map(str, input().split())
    S.append(s)
    D.append(int(d))
    i += 1

# A,B�˹�碌����ư��Υ��Ĵ��
Dnew = []
for dst in D:
    if dst < A:
        Dnew.append(A)
    elif B < dst:
        Dnew.append(B)
    else:
        Dnew.append(dst)

# �ºݤ˰�ư
cnt = 0
for dir, dst in zip(S, Dnew):
    if dir == 'East':
        cnt += int(dst)
    else:
        cnt -= int(dst)

if cnt > 0:
    print('East', cnt)
elif cnt < 0:
    print('West', -cnt)
else:
    print(0)
