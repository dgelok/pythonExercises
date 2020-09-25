# map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# list comprehension syntax
c = [x*2 for x in a]
print(c)

