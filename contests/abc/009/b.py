N = int(input())
A = [int(input()) for i in range(N)]
A = list(set(A))
A.sort()
print(A[-2])
