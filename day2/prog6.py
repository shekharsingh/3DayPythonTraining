# tuple - readonly list
# immutable object
t = tuple()
print t
print len(t)
print type(t)

# can be created by following as well
l = ()
print l

items = (2.2, 'pam', 1, 3, 'iii', 4.4, 'five')
print items
print items[-1]
print items[:-1],
print
for item in items:
    print item,
print

# this will create an int not as single element tuple
n = (1000)
print type(n)
# to define single element tuple
m = (1000,)
print type(m)

# this is also a way to create tuple
items = 12, 3.3, 'pam', 'kim'
print items

# application of tuple
# 1. Parallel assignment
# this creates tuple in memory
name, age, gender = t = 'pam', 23, 'female'
print t
print name
print gender
print age

# 2. to return more than 1 value from a Python function
print divmod(5.0, 2)
q, r = divmod(5.0, 2)
print q, r

def sq_and_cube(value):
    return value ** 2, value ** 3
print sq_and_cube(5)
