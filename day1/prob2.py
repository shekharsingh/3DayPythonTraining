# read the passwd file
# extract the ordered list of username
# print alphabetical ordered name & the line number

name = list()
delimiter = ':'


def readfile():
    fp = open(r'/mnt/blackhat/python/3DayPythonTraining/passwd.txt')
    for line in fp:
        user = line.split(delimiter)
        name.append(user[0])
    fp.close()


def sort_and_print():
    name.sort()
    print enumerate(name)
    for i, c in enumerate(name):
        print "[{}] --> {}".format(i, c)


readfile()
sort_and_print()

