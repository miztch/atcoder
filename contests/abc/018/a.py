A, B, C = [], [], []
a = int(input())
b = int(input())
c = int(input())

list = []
list.append(a)
list.append(b)
list.append(c)

if max(list) == a:
    A.append('1')
    if min(list) == b:
        B.append('3')
        C.append('2')
    else:
        B.append('2')
        C.append('3')
elif max(list) == b:
    B.append('1')
    if min(list) == a:
        A.append('3')
        C.append('2')
    else:
        A.append('2')
        C.append('3')
else:
    C.append('1')
    if min(list) == a:
        A.append('3')
        B.append('2')
    else:
        A.append('2')
        B.append('3')

print(int(A[0]))
print(int(B[0]))
print(int(C[0]))
