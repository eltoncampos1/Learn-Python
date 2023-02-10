myset={"a", "b", "c", "a"}
set2 = set([1,2,3])
empt = set()
set2.remove(2)
print(myset)
print(set2)

empt.add(1)
empt.clear()
print(empt)

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens)
print(u)

i = odds.intersection(evens)