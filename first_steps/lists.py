friends=["jhon", "doe", "mary", "moon"]
lk_numbs= [4,61,9,2,37,0,13, 4]
friends.extend(lk_numbs)
friends.append("Chris")
friends.insert(1, "Diana")
friends.remove("doe")
# friends.clear()
friends.pop()
lk_numbs.sort()
lk_numbs.reverse()
f2= friends.copy()
print(friends.index(61))
print(friends.count(4))
print(friends)
print(lk_numbs)
print(f2)

