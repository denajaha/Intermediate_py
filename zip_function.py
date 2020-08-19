import json

# zip function takes elements from multiple iterables and aggregates them into one iterable where we share index value

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a, b, c in zip(x, y, z):
    print(a, b, c)

print(list(zip(x, y, z)))
print('dict')
print(dict(zip(x, y)))  # dict works only with 2 of course

for i in zip(x, y, z):
    print(i)
print('list comprehension')
[print(x, y, z) for x, y, z in zip(x, y, z)]  # zip and list comp,
# and also x, y, z are NOT STORED anywhere...if I want to use for loop, they ARE STORED (overwritten)
for x, y in zip(x, y):
    print(x, y)

print(x)  # --> x IS STORED, for loop has overwritten our x value
# (it was a list, now it is a last number from the x list (because of the last iteration in for loop))
########################################################################################################
print('JSON')

y = json.dumps(dict(zip(x, y)))
print(y)

x = json.loads(y)
print(x['1'])
