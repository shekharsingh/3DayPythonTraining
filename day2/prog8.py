# regex in python
# match - subs - split
# regex - case sensitive
#       - matches only once in a single line
#       - match even with sub-string
# module for regex in python is re
import re

# Operation 1
# match operation
s = 'the python and the perl scripting'
# starts with P followed by one or more occurrence & end with N
pattern = 'P.+N'
# to match for least size
patt = 'P.+?N'
# fails as it is case sensitive
m = re.search(pattern, s)
print m

# single time match
m = re.search(pattern, s, re.I)
ml = re.search(patt, s, re.I)
if m:
    print m
    # greediness - matches for at most
    print "matched string :", m.group()
    # how to match for the least
    print "matched string :", ml.group()
    print m.start(),
    print m.end(),
    # span -> (start, end)
    print m.span()
    before = s[:ml.start()]
    after = s[ml.end():]
    print 'before : |{}|'.format(before)
    print 'after : |{}|'.format(after)
else:
    print 'failed to match'
print

# match multiple times
for m in re.finditer(patt, s, re.I):
    print m.group(),
    print m.span()
print

# list of matched strings
print re.findall(patt, s, re.I)
print

# Operation 2
# subs operation
s = 'root:x:0:0:root:/root:/bin/bash'
patt = ':'
replace = ','
f = re.sub(patt, replace, s)
print f
print re.sub('[AEIOU]', '*', s, flags=re.I)
print re.sub('root', '****', s)
print

# Operation 3
# split operation
s = 'root :x  :0        :0:root    :/root:/bin/bash'
print re.split('[:,;]|\s+', s)
# match will also work with \s+ -> one or more space
# print re.search('[:,;]|\s+',s)
print
