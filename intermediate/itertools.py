from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby

# Product

a = [1,3]
b = [7,5]

prod = product(a,b)
print(list(prod))

# Permutations

c = [1,2,3]
perm = permutations(c)
print(list(perm))

# Combinations

d = [1,2,3,4]
comb = combinations(d, 2)
print(list(comb))

# Combinations whith replacments

comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))

# Accumulate

def smaller_than_3(x):
    return x < 3

acc = accumulate(d)
print(list(acc))

# Group by

group = groupby(d, key=lambda x: x < 3)
for key, value in group:
    print(key, list(value))