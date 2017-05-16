name = 'dell'
city = 'bangalore'

print 'name :', name
print 'city :', city

try:
    name = raw_input('enter the name : ')
    city = raw_input('enter the city : ')
    zip_code = int(raw_input('enter the postal zip : '))
    temp = float(raw_input('enter current temp : '))

    print 'name :', name
    print 'city :', city
    print 'zipcode :', zip_code
    print type(zip_code)
    print type(str(zip_code))
    # string formatting
    # {:fmt str}
    print "current temp : {:.5f}".format(temp)
except ValueError, err_obj:
    print err_obj
