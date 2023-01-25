# -*- coding: utf-8 -*-

S = input()

list_a = S[0::2]
list_b = S[1::2]

# result_a: 010101 にする場合の回数
# result_b: 101010 にする場合の回数
result_a, result_b = 0, 0

for l in list_a:
    black = l.count("0")
    white = l.count("1")
    result_a += white
    result_b += black

for l in list_b:
    black = l.count("0")
    white = l.count("1")
    result_a += black
    result_b += white

result = min([result_a, result_b])
print(result)
