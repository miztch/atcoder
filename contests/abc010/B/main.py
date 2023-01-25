N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(len(A)):
    k = 0
    while k < A[i]:
        if (A[i]-k) % 2 != 0 and (A[i]-k) % 3 != 2:
            ans += k
            break
        else:
            k += 1
print(ans)
