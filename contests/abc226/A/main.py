# -*- coding: utf-8 -*-
# ABC228A

X = input()

left, right = X.split(".")

left = int(left)

if int(right[0]) >= 5:
    ans = left + 1
else:
    ans = left
print(ans)
