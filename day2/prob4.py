# unix cat like command implementation
# reverse flag should work like tac command (reverse of cat)
# rev -> mirror image of file
# rev file | tac -> both mirror & reverse
# to reverse -> 'peter pan'[::-1]
#            -> output -> 'nap retep'
def cat(filen, **kwargs):
    print filen,
    print kwargs
    rev = kwargs.get('reverse')
    mir = kwargs.get('mirror')
    cont = open(filen).readlines()

    if rev:
        cont.reverse()

    if mir:
        # rstrip to remove newline char while mirroring
        cont = [line.rstrip()[::-1] + "\n" for line in cont]

    print ''.join(cont)


# join example -> requires list of strings only
# items = ['wal', '127.0.0.1, 'on']
# print ','.join(items)
# output => wal,127.0.0.1,on

cat('test.txt')
print
cat('test.txt', reverse=True)
print
cat('test.txt', mirror=True)
print
cat('passwd.txt', reverse=True, mirror=True)
print
