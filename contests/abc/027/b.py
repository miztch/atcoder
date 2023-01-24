N = int(input())
a = list(map(int, input().split()))

ans = 0
if sum(a) % N != 0:
    print(-1)
else:
    for i in range(N):
        if sum(a[:i+1])/(i+1) != sum(a)/N:
            ans += 1
    print(ans)
