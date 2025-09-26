def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Lemon Chai"
    yield "Cup 3: Ginger Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

# #output: Cup 1: Masala Chai
# Cup 2: Lemon Chai
# Cup 3: Ginger Chai

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

#generator functions

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen
print(next(chai)) 
#output: Cup 1
print(next(chai)) 
#output: Cup 2
print(next(chai)) 
#output: Cup 3
print(next(chai)) 
#throws error