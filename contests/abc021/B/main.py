N = int(input())
a, b = map(str, input().split())
K = int(input())
p = input().split()
for i in range(K):
    p[i] = int(p[i])

p.reverse()
p.append(int(a))
p.reverse()
p.append(int(b))
p.sort()

cnt = 0
for i in range(K+2):
    if p[i-1] == p[i]:
        cnt += 1
if cnt == 0:
    print('YES')
else:
    print('NO')
