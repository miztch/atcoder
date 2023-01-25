import re
S = input()
if 'B' in S:
    A = re.split("01BB|10BB|11BB|00BB|0B|1B", S)
    A = "".join(A)
    if 'B' in A:
        C = re.split("01BB|10BB|11BB|00BB|0B|1B", A)
        C = "".join(C)
        C = C.split("B")
        print("".join(C))
    else:
        print(A)
else:
    print(S)
