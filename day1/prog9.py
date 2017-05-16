n = 15
print bin(n)
print hex(n)
print oct(n)

print int('1111', 2)
print int('f', 16)
print int('17', 8)

print 017
print 0b1111
print 0xf

print 2 ** 30
print type(2 ** 30)

print 2 ** 31
print type(2 ** 31)

# float
print 0.003
print 3e-3
print 3E-3

# complex
n = 4 + 3j
print n
print n.real
print n.imag
print n.conjugate()
print type(n)
print n ** n

#string

s = 'python'
print s.index('t')
# s[2] = 'T' -> not permitted, strings are immutable

#regular vs raw string
file_path = 'C:\temp'
print file_path

file_path = r'C:\temp'      # raw string to avoid escape char
print file_path

# doc string
#   create multi line formatted content
content = ''' 
      #                #
   #     #          #     #
#          #######           #
   #     #          #     #
      #                #
'''

print content

# indexing

s = 'perl'
print s[0]
print s[-3]
print s[1]
print s[-1]

# slicing
s = 'perlandpython'
print s[:4], s[3:7], s[-6:], s[:], s[1:-1]

print ord('A') # return ascii
print chr(65) # return char