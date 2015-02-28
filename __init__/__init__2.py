class  Fruit(object):
    #code
    def __init__(self, name, color, flavor):
        #set values for attributes
        self.name = name
        self.color = color
        self.flavor = flavor
        print "The", self.name, "is", self.color, "and tastes", self.flavor, "."


fir = Fruit("banana", "amarilla", "dulce")

