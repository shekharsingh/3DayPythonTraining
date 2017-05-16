# string formatting
name, age, gender = 'sarah', 3, 'female'    # parallel assignment
print "{}{}{}".format(name, age, gender)
print "|{}|{}|{}|".format(name, age, gender)
print "|{:+>22}|{:0>9}|{:-<16}".format(name, age, gender)   # padding with zero or other characters
print "|{:^22}|{:^9}|{:^16}|".format(name, age, gender)
print "|{:22}|{:9.2f}|{:16}|".format(name, age, gender)