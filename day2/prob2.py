# implement grep command
# example :- grep -n root /etc/passwd /etc/group
# print matched line, line number, file name
import re
from fileinput import input, filename, filelineno
from glob import glob


def grepMe(pattern, *args):
    for line in input(args):
        if re.search(pattern, line, re.I):
            print"{}:{}:{}".format(filename(), filelineno(), line)

# grepMe('print', 'prog1.py', 'prog2.py', 'prog3.py', 'prog4.py')
# this is wrong as it passes list
# grepMe('print', glob('prog*'))
# pass content of a list
# * can be used with any of the sequences like - list, string, tuple
grepMe('print', *glob('prog*'))

# grep redefined in a simpler way -> from prog12.py
patt = 'root'
print filter(lambda line: re.search(patt, line, re.I), open('passwd.txt'))
