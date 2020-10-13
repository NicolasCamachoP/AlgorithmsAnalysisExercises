import itertools
S = [1, 2, 3]
print("Permutations")
for p in itertools.permutations(S):
    print(p)
print("Combinations")
for r in range(1, len(S) + 1):
    for c in itertools.combinations(S, r):
        print(c)