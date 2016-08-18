class bird(object):
    feather = True

class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def getAdult(self):
        if self.age > 16:
            return True
        else :
            return False

    adult = property(getAdult)


c = chicken(12)

print c.adult

d = chicken(17)

print d.adult
