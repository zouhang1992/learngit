class people(object):
    __name = 'jack'
    __age = 12

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
print dir(people)
p = people()
print p.getName(),p.getAge()
print p._people__name, p._people__age
print dir(object)
