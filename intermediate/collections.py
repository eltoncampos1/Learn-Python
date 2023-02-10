from collections import  Counter, OrderedDict, defaultdict

# Counter
a = "aaasdvcvasdaop"
m_counter= Counter(a)
print(m_counter)
print(m_counter.most_common(1))

# Ordered

or_dict = OrderedDict()
or_dict["b"] = 2
or_dict["c"] = 3
or_dict["d"] = 4
or_dict["a"] = 1
print(or_dict)

# Default

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)