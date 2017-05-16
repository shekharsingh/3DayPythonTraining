# compound data types
# list -> ordered collection, similar to array in other language
items = list()  # empty list
print items
print len(items)
print type(items)

items = [2.2, 'pam', 3.4, 'eva', 'allen', 'nick', 0.003, 'wait', 7]
items[-3] += 3.3
items.append('dell')
items.insert(0, 'bangalore')
print items

value1 = items.pop()
value2 = items.pop(-4)
print value1
print value2

items = [2.2, 'pam', 3.4, 'eva', 'pam', 'allen', 'nick', 'pam', 0.003, 'pam', 'waltpam', 7]
print items
item = 'pam'
items.remove(item)
print items

while item in items:
    items.remove(item)
print items

print items + items
print items * 2

others = items * 2
print list(set(others))  # application of set type -> combination of hash table & array

print list(sorted(others))
print list(reversed(others))
others.reverse()
print others
others.sort(reverse=True)  # descending order
print others

old = items * 2
new = sorted(old)  # keeps the orig content intact
newr = sorted(old, reverse=True)
print old
print new
print newr

s = 'root:x:0:0:root:/root:/bin/bash'
delimiter = ':'
content = s.split(delimiter)
print content
print s.split(delimiter)[0]
print s.split(delimiter)[1:]

for c in content:
    print c,

# iterate over index & value of a list
print enumerate(content)
for i, c in enumerate(content):
    print "[{}] --> {}".format(i, c)
