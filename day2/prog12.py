import re


# create a list which has multiple of 7 in given range
items = range(1, 256)
print items
# it will return only false or true
print map(lambda sev: sev % 7 == 0, items)
# instead of map, filter can be used for this purpose
print filter(lambda sev: sev % 7 == 0, items)

# grep redefined in a simpler way- refer prob2.py
patt = 'root'
print filter(lambda line: re.search(patt, line, re.I), open('passwd.txt'))
