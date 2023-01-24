n, x = map(int, input().split())
a = list(map(int, input().split()))

price = 0
b = str(bin(x))[2:]

if len(b) < n:
    b = '0' * (n - len(b)) + b

for i, j in zip(range(n)[::-1], b):
    if j == '1':
        price += a[i]

print(price)
