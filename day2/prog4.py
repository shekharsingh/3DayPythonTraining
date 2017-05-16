# lambda operator
# as a callable object
# part of python functional programming construct
# python is 1st class functional programming language
# syntax :
# lambda arg1, arg2,....: expression
from pprint import pprint as pp

# example
# default value to n
power = lambda x, n=0: x ** n
print power(4, 5)
print power(4)

# example with lambda
# removing the newline
content = [line.rstrip().split(':') for line in
           open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
content.sort(key=lambda record: int(record[2]))
pp(content)

for user in content:
    print "{}:{}:{}".format(user[2], user[0], user[-1])
