A, B, C, D = map(int, input().split())
TK, AO = B/A, D/C
if TK > AO:
    print("TAKAHASHI")
elif TK < AO:
    print("AOKI")
else:
    print("DRAW")
