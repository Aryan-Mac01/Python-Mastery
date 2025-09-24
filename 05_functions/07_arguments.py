# chai_type = "plain"

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type = "Irani"
#     kitchen()

# front_desk()

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetner = "Honey", foam = "yes")

#output
# Ingredients('Cinnamon', 'Cardamom')
# Extras {'sweetner': 'Honey', 'foam': 'yes'}