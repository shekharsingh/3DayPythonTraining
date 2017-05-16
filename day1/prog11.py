print bool('peter')
'''
while 'peter':  # since it taes as bool & bool is true so it is while 1
    print '@'   # infinite times
'''
print bool('')
print bool('-12.24')
print bool('$')
# int, long, float, complex, dict, list, tuple, none --> all return false
print bool(0), bool(0L), bool(0.0), bool(0+0j), bool({}), bool([]), bool(()), bool(set()), bool(None)
print type(None)