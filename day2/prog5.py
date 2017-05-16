# to learn following for dict
# update
# add
# delete
# lookup
# iteration

info = {
    'host': 'wsl',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print info

# update - wrong key will be added
item = 'verson'
info[item] = 3.4
print info

# validate the key
item = 'version'
if item in info:
    info[item] = 3.4
print info

# add
info['ipaddr'] = '127.0.0.1'
print info

# del
value = info.pop('verson')
print value
print info

# lookup / read
# if inappropriate key then KeyError
# graceful lookup by using get() - if no key then None is returned
# if None is not required, we can return a default-value
print info['desc']
print info['version']
print info.get('apps')
print info.get('apps', 'default-value')

# list of keys only
print info.keys()
# list of values only
print info.values()
# list of key, value pairs - returns as tuple
print info.items()

# iterate over dict content - key base - default behaviour
for item in info:
    print item, '-->', info[item]

# iterate over key & value together
print info.iteritems()
for k, v in info.iteritems():
    print k, ':', v
