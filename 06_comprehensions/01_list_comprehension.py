#Syntax: [ expression for item in items if condition ]

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [ tea for tea in menu if "Iced" in tea]

print(iced_tea)