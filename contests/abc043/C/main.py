n = int(input())
A = list(map(int, input().split()))

S = [sum((i-a)**2 for a in A) for i in range(min(A), max(A)+1)]
print(min(S))
