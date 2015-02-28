#http://learntofish.wordpress.com/2011/12/06/tutorial-object-oriented-programming-in-python-part-2/

class Person:
    #attributes
    name = "no name yet"
    age = 0
    #methods constructor
    def __init__(self, x, y):
        self.name = x
        self.age = y
        print "You have just created a Person object."
    ##
    def talk(self):
        print "Hi! My name is", self.name, "and I am", self.age, "years old."
    ##
    def setFoodAndMusic(self, x, y):
        self.food = x
        self.music = y
    ##
    def tellmore(self):
        print "I like eating", self.food, "and I love listening to", self.music
    


p = Person("luis", "25")
p.talk()
p.setFoodAndMusic("salmon", "minimal-tech")
p.tellmore()