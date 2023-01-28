S = input()

result = 0
for i in range(len(S)):
    b = (ord(S[::-1][i])-64)*(26**i)
    result += b

print(result)
