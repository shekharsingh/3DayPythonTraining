# part 1 - write a python script to get a word occurrence from a text file
# {word : num_of_occurrence)
# part 2 - group based on the occurrences
# ( occurrences : [list of words])
# (num_of_occurrence : [word1, word2, word3, ....])
from pprint import pprint as pp


def grp_by_occ(wd_occ):
    grp_by = dict()

    for word, cnt in wd_occ.iteritems():
        if cnt not in grp_by:
            grp_by[cnt] = list()

        grp_by[cnt].append(word)

    return grp_by


'''
def get_word_occ(tfile):
    wordcnt = dict()

    for line in open(tfile):
        for word in line.rstrip().split():
            wordcnt[word] = wordcnt.get(word, 0) + 1

    return wordcnt


wc = get_word_occ(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\message.txt')
grp = grp_by_occ(wc)
pp(grp)
'''


def getwc(tf):
    wdc = dict()

    for item in tf:
        for w in item:
            wdc[w] = wdc.get(w, 0) + 1

    return wdc


content = [line.rstrip().split(':') for line in
           open(r'C:\Users\ravi_shekhar_singh\Documents\Personal\coding\python\dell_training\passwd.txt')]
wcont = getwc(content)
grp = grp_by_occ(wcont)
pp(grp)

# top 2 most widely used words
for count in sorted(grp)[-2:]:
    print count, ':',
    for word in grp[count]:
        print "\t", word
    print

for count in sorted(grp, reverse=True)[:2]:
    print count, ':',
    for word in grp[count]:
        print "\t", word
    print
