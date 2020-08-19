# enumerate returns a tuple containing the count along the way and object(item) itself that I am iterating over

example = ['left', 'right', 'up', 'down']

# for i in range(len(example)):     #WRONG WAY TO DO
#     print(i, example[i])

for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))  # creating dict from enumerate -> very useful in practice
print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]  # iterating over dict using list comprehension
