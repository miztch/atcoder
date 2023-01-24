A, B, C, D, E = map(int, input().split())
list, output = [A, B, C, D, E], []
K = sum(list)

for a in list:
    for b in list:
        output.append(K-(a+b))
        if K-2*a in output:
            output.remove(K-(a+a))
output.sort()
output = set(output)
for i in range(2):
    output.remove(max(output))
print(max(output))
