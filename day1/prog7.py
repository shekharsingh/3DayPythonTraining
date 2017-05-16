class PackageManager(object):
    def __init__(self, name, version):
        self.__name = name  # private attribute
        self.version = version

    def __get_infomation(self):  # private method
        print 'name : ', self.__name
        print 'version : ', self.version

    def wrapper(self):  # to access private method
        self.__get_infomation()


pm = PackageManager('pm', '2.2.11')
# pm.get_infomation()
pm.wrapper()
# print pm.__name   -> can't be used
