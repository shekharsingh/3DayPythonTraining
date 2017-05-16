# set
# -- hashed list = hash + list
# unordered - prints not in order
#       -- can't index or slice
items = set()
print items
print len(items)
print type(items)

items = set([2.2, 'pam', 2.2, 0.003, 5 + 2j])
print items
items.add('dell')
items.add('cv')
print items

# can't predict what pop will remove
value = items.pop()
items.remove('cv')
print value
print items

for item in items:
    print item,
print

# application of set
a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]
x = set(a)
y = set(b)
# common operation & their operator overloading options
print x.intersection(y)
print x & y
# typecast as list
print list(x.intersection(y))
print x.union(y)
print x | y
print x.difference(y)
print x - y
# unique elements of second list
print y - x
