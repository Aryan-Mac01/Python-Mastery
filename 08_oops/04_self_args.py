class Chaicup:
    size = 150

    #method
    def describe(self):
        return f"A {self.size} ml cup chai"
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe()) #this throughs an error 'missing args'

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))