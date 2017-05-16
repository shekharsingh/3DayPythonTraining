import math
import os
import sys

class Demon(object):
    pass    # to define a dummy code block

d = Demon()
print d
print Demon
print __name__  # to get the default namespace of a script as well as module
print math.__name__
print os.__name__
print sys.__name__