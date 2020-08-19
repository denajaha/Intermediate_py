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
########################################################################################################################
input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
# 27 and 29-32 are doing the same thing (beside list vs generator)
# xyz = []
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)

for i in xyz:
    print(i)
# 34 and 37 are doing the same thing
[print(i) for i in xyz]

########################################################################################################################

[[print(i, ii) for ii in range(5)] for i in range(5)]
# 41 and 43-45 doing the same thing
for i in range(
        5):  # third thing to write in 41 ---> always doing stuff backwards if I want to write "oneliner for loop" aka 41
    for ii in range(5):  # second thing to write in 41
        print(i, ii)  # first thing to write in 41

xyz = [[(i, ii) for ii in range(5)] for i in range(5)]  # list of tuples
print(xyz)

xyz = [[[i, ii] for ii in range(5)] for i in range(5)]  # list of lists
print(xyz)

xyz = ([[i, ii] for ii in range(5)] for i in range(5))  # generator expression over which one I can iterate
print(xyz)

print([i for i in xyz])  # iterating over my generator
# with big list you will run out of memory
# with big generators you will run out of time

