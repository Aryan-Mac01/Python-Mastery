class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "medium"
print(cutting.temperature)
print("Direct look into the class", Chai.temperature)

del cutting.temperature
print(cutting.temperature) #output is still 'hot' because it falls back to the attribute 'temperature' in class Chai
del cutting.cup
print(cutting.cup) #this will through an error because it has no attribute to fall back to