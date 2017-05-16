# Scopes in Python
# Global scope
n = 13


def demon():
    # Local scope
    n = 'pypi'
    print n
    print locals()


# updating global from function
def dem():
    global n
    n = 'oops'
    print n


print n
demon()
print n
dem()
print n

print globals()
