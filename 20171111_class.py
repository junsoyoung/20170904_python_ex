total = 0

class Service:

    def __init__(self, name):
        self.name = name
        global name2
        name2 = name

    secret = "sonya is Jun.Soyoung."
    def add(self, a, b):
        result = a+b
        global total
        total += result
        print( "%s, %d + %d = %d, Total = %d, %s" % (self.name, a, b, result, total, name2 ))


jun = Service("soyoung")
jun2 = Service("sonya")
print( jun.add( 4, 4))
print( jun2.add( 1,1))
