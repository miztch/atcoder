from math import sqrt

bx, by, ax, ay, T, V = map(int, input().split())
N = int(input())
Gs = [list(map(int, input().split())) for i in range(N)]

cnt = 0
for i in range(len(Gs)):
    dist = sqrt((ax-Gs[i][0])**2+(ay-Gs[i][1])**2)\
        + sqrt((bx-Gs[i][0])**2+(by-Gs[i][1])**2)
    if T*V >= dist:
        cnt += 1
        break
if cnt == 0:
    print('NO')
else:
    print('YES')
