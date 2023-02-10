def my_gen():
    yield 1
    yield 2
    yield 3
    
g = my_gen()

value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)



