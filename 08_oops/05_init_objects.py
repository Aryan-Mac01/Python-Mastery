class Chaiorder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} ml of {self.type} chai"
    
order = Chaiorder("Masala", 200)
print(order.summary())

order_two = Chaiorder("Ginger", 220)
print(order_two.summary())