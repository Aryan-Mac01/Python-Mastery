#first way
file = open("order.txt", "w")
try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()

#second way
with open("orders.txt", "w") as file:
    file.write("ginger tea - 4 cups")