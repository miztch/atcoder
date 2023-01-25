# -*- coding: utf-8 -*-
# ABC227B

n = int(input())
S = list(map(int, input().split()))

all_patterns = set()

for a in range(1, 142+1):
    for b in range(1, 142+1):
        s = 4*a*b + 3*a + 3*b
        if s <= 1000:
            all_patterns.add(4*a*b+3*a+3*b)

count = 0
for s in S:
    if s not in all_patterns:
        count += 1
print(count)
