S = [input() for i in range(12)]
cnt = 0
for s in S:
    if 'r' in s:
        cnt += 1
print(cnt)
