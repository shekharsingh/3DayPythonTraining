class Demon(object):
    def __init__(self):
        print 'am in constructor ', self
        print 'am in constructor '

    def __del__(self):
        print 'am being destroyed', self


d = Demon()  # only init is called
e = Demon()
print 10
print d, id(d)  # id() for address
print e, id(e)
print 20
# no more code so d object terminates
