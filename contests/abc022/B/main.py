N = int(input())
list = []
for i in range(N):
    A = int(input())
    list.append(A)
list.sort()
cnt = 0
for i in range(N):
    if list[i-1] == list[i]:
        cnt += 1
print(cnt)
