T = int(input())
A = [list(map(int, input().split())) for i in range(T*2)]

for i in range(T):
    test_case = A[i*2+1]

    for i in range(len(test_case)):
        if test_case[i] % 2 == 0:
            test_case[i] = 0

    print(len(test_case) - test_case.count(0))
