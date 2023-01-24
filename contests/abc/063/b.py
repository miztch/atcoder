s = input()
Chars = [l for l in s]
Depre = set(Chars)

if len(Chars) == len(Depre):
    print('yes')
else:
    print('no')
