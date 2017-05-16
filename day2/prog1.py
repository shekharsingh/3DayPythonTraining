# parallel iteration
from pprint import pprint as pp

names = ['pam', 'jim', 'tim', 'tom']
ages = [3, 2, 4, 1]
gender = ['female', 'male', 'male', 'male']

pp(zip(names, ages, gender))

print
print
for n, a, g in zip(names, ages, gender):
    print "{:>22} {:>7} {}".format(n, a, g)

# convert content of a list to binary
items = [3, 2, 1, 4, 5, 6, 7, 9]
temp = list()

for item in items:
    temp.append(bin(item))

print temp

# list comprehension - always returns a list
temp2 = [bin(item) for item in items]
print temp2

# power of each element in list
temp3 = [bin(item ** item) for item in items]
print temp3

# prints only odd number
temp4 = [bin(item) for item in items if item % 2]
print temp4
