def gene():
    comp.append(list[0])
    comp.append(1)
    list.pop(0)


list = []
comp = []

s = input()
for i in range(len(s)):
    list.append(s[i])

gene()
for i in range(len(s)-1):
    if comp[-2] == list[0]:
        comp[-1] += 1
        list.pop(0)
    else:
        gene()

comp = [str(i) for i in comp]
print(''.join(comp))
