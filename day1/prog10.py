s = 'This is a sample string in python'

for temp in s:
    print temp,

for temp in s:
    if temp not in 'aeiou ':  # if char is a,e,i,o,u & space
        print "{} : {}".format(temp, ord(temp))
    else:
        print '*'

for temp in s:
    if temp not in 'aeiou ' and temp.isupper():
        print temp,
    else:
        print '*',
    print

n = 5.75
print not 3 <= n <= 7
print 3 <= n <= 7

print 'sam' in s
print 's a' in s
print 'zee' not in s

# array implemented by list
print range(10)
print range(1, 10)
print range(1, 10, 2)
items = range(1, 115)
print items
print
print 13 in items

n  = 4
print n ** 2 if n > 5 else n ** 3