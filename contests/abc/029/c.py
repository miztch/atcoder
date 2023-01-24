n = int(input())
S = ["a", "b", "c"]

T = [s for s in S]

for i in range(n-1):
    for t in range(len(T)):
        for s in S:
            u = T[t] + s
            T.append(u)

Ans = [t for t in T[-3**n:]]
for a in Ans:
    print(a)
