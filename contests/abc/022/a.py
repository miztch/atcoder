N, S, T = map(int, input().split())
W = int(input())
bestdays = 0
if S <= W <= T:
    bestdays += 1
for i in range(N-1):
    A = int(input())
    W += A
    if W <= 0:
        W = 0
    if S <= W <= T:
        bestdays += 1
print(bestdays)
