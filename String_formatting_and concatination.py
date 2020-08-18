# String Concatenation and Formatting
names = ['Jeff', 'Gary', 'Jill', 'Samantha']
for name in names:
    print('Hello there, ' + name)
    # Hello there Jeff
    # Hello there Gary
    # Hello there Jill
    # Hello there Samantha

    print(' '.join(['Hello there', name]))
    # Hello there Jeff
    # Hello there Gary
    # Hello there Jill
    # Hello there Samantha

print(', '.join(names))     # join uses less processing
# Jeff, Gary, Jill, Samantha

import os
location_of_files = '/Users/denis/PycharmProjects/Intermediate_py'
file_name = 'example.rtf'

print(location_of_files + '/' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print('reading file: ')
    print(f.read())

# Gary bought 12 apples today!
who = 'Gary'
how_many = 12
print('{} bought {} apples today!'.format(who, how_many))       # correct way to do String formatting


