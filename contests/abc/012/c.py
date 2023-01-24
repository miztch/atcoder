N = int(input())
Multi = [0] + [k*l for k in range(1, 10) for l in range(1, 10)]
D = sum(Multi) - N

X, Y = [], []
for i in range(len(Multi)):
    if Multi[i] == D:
        if i % 9 == 0:
            X.append(i//9)
            Y.append(9)
        else:
            X.append(i//9+1)
            Y.append(i % 9)

for x, y in zip(X, Y):
    print(x, 'x', y)
N = int(input())
Multi = [0] + [k*l for k in range(1, 10) for l in range(1, 10)]
D = sum(Multi) - N

X, Y = [], []
for i in range(len(Multi)):
    if Multi[i] == D:
        if i % 9 == 0:
            X.append(i//9)
            Y.append(9)
        else:
            X.append(i//9+1)
            Y.append(i % 9)

for x, y in zip(X, Y):
    print(x, 'x', y)
