a, b, c = map(int, input().split())
sum, dif = a + b, a - b

if sum == c and dif == c:
    print('?')
elif sum == c:
    print('+')
elif dif == c:
    print('-')
else:
    print('!')
