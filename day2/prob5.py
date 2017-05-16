# list the content of a directory
from os import listdir
from sys import argv

dirname = argv[1] if len(argv) == 2 else '.'
for items in listdir(dirname):
    print items
