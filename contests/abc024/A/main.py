A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
Fee = A * S + B * T
if S + T >= K:
    Fee -= C * (S + T)
print(Fee)
