# functional programming
# map
items = [3, 2, 4, 5, 6, 1, 8, 10]
print items
print map(hex, items)
print map(bin, items)
print map(oct, items)
# list ot ascii
print map(ord, 'shekhar singh')
print

ascii = [115, 104, 101, 107, 104, 97, 114, 32, 115, 105, 110, 103, 104]
# transform ascii to xml tags
'''
112
<ascii char="p">112</ascii>
'''


def tag_it(av):
    print 'ascii char="{}">{}</ascii>'.format(chr(av), av)


map(tag_it, ascii)
print
# using lambda in functional programming
print map(lambda av: 'ascii char="{}">{}</ascii>'.format(chr(av), av), [115, 126])
