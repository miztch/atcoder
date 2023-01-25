import math
s = input()
n = int(input())
print(s[math.ceil(n/5-1)]+s[n % 5-1])
