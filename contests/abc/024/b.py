log = []
time = 0
N, T = map(int, input().split())
for i in range(N):
    log.append(int(input()))
for i in range(1, N):
    if log[i]-log[i-1] >= T:
        time += T
    else:
        time += log[i]-log[i-1]
time += T
print(time)
