dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
for char in input():
    dict[char] += 1
fixed = [s+str(t) for s, t in zip(list(dict.keys()), list(dict.values()))]
fixed.sort()
print(" ".join([c[1:] for c in fixed]))
