N = int(input())

h = N // 3600
m = (N // 60) % 60
s = N % 60

a = '0' + str(h) if h < 10 else str(h)
b = '0' + str(m) if m < 10 else str(m)
c = '0' + str(s) if s < 10 else str(s)

print(a+':'+b+':'+c)
