# generator --> range() in for loop
# generator vs list : generator is slower but it is not using any memory in RAM, list is faster but it is using RAM

# producing the same output --> xyz and xyz2
xyz = [i for i in range(5)]
print(xyz)
xyz2 = []
for i in range(5):
    xyz2.append(i)
print(xyz2)

# generator vs list comprehension is in the parentheses
xyz = (i for i in range(5))  # generator
print('printing generator')
print(xyz)




