N, P, Q, R, S = map(int, list(input().split()))
A = [i for i in input().split()]

x = A[P-1:Q]
y = A[R-1:S]

l = A[:P-1] + y + A[Q:R-1] + x + A[S:]
print(" ".join(l))
