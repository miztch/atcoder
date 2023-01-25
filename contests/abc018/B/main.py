S = input()
N = int(input())
for i in range(N):
    p, q = map(int, input().split())
    R = S[p-1:q]
    S = S[:p-1] + R[::-1] + S[q:]
print(S)
