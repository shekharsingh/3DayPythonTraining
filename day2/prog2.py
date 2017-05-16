from pprint import pprint as pp

ul = [line.split(':')[0].upper() for line in open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
pp(ul)
pp(ul,width=3000)

ula = [line.split(':')[0].upper() for line in open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt') if line.startswith('a')]
pp(ula)

content = [line.rstrip().split(':') for line in
           open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
pp(content)

for item in content:
    for word in item:
        print word