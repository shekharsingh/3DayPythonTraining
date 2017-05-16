from pprint import pprint as pp


def sort_by_3rd_col(record):
    return int(record[2])


'''
# converting to list of a list
content = [line.split(':') for line in
           open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
pp(content)
'''

# removing the newline
content = [line.rstrip().split(':') for line in
           open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
content.sort(key=sort_by_3rd_col)
# can also use foloowing
# content = sorted(content, key=sort_by_3rd_col)
pp(content)

for user in content:
    print "{}:{}:{}".format(user[2], user[0], user[-1])
