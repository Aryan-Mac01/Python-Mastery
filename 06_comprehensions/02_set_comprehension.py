#Syntax: { expression for item in items if condition }

fav_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Lemon Chai", "Green Tea", "Elaichi Chai"
]

unique_chai = { chai for chai in fav_chais }
print(unique_chai)

len_unique_chai = { chai for chai in fav_chais if len(chai)<8 }
print(len_unique_chai)

recipes = {
    "Masala Chai" : ["Ginger Chai", "cardamom", "clove"],
    "Ginger Chai" : ["cardamom", "milk"],
    "Spicy Chai" : ["Black pepper", "ginger", "clove"]
}

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients }
print(unique_spices)