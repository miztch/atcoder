word = []
cnt = 0

X = input()
X = X.replace('ch', 'oo')
X = X.replace('k', 'o')
X = X.replace('u', 'o')

for i in X:
    word.append(i)

for i in word:
    if i == 'o':
        pass
    else:
        cnt += 1

if cnt > 0:
    print('NO')
else:
    print('YES')
