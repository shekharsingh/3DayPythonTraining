# functions

# variable number of arguments in a function
# goes in as tuple
def demon(*args):
    print args


demon()
demon(4, 5)
demon('arya', 13, 'feb')
demon(*'arya')


def compute(a, b, c):
    return a + b + c


i = [34, 28, 24]
print compute(i[0], i[1], i[2])
# instead of above, below can be used
print compute(*i)

# keyword argument function
# this case keywords are required
# displays as dict
def tunner(**kwargs):
    print kwargs
# function with arguments - value only
# tunner(0.6, 0.78, 0.89)
# pass a keyword with a value as argument
# keywords are optional
tunner(contrast=0.6, brightness=0.78, hue=0.89)

def allinone(a,b,*args,**kwargs):
    print a
    print b
    print args
    print kwargs
allinone(1,2,3,4,5,6)
allinone(1,2,3,4,5,6,lang='perl',author='larry')
print

def allinone(*args,**kwargs):
    print args
    print kwargs
allinone(contrast=0.6, brightness=0.78, hue=0.89)
print
