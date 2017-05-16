# open a file, replace : throughout with ,
# inplace replacement
# save in the same file
# filename :- passwdprob3
# sed
import re
import fileinput


# with inplace always use backup option to keep a backup
# with inplace print will not display on the stdout
# ^S -> blank line
# ^\n
for line in fileinput.input('passwd.txt', inplace=True, backup='.bak'):
    print re.sub(':', ',', line),

#for line in fileinput.input('passwd.txt', inplace=True, backup='.bak'):
#    print re.sub('^\n', ',', line)