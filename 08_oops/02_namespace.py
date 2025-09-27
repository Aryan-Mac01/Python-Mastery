class Chai:
    origin = "India" #property of class 'Chai'

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

#creating objects of class Chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)
masala.is_hot = False
masala.flavor = "Spice" #property present only in the namespace of the object

print("Class: ", Chai.is_hot) #True
print("Masala: ", masala.is_hot) #False

#The value is changed in the namespace of the object.