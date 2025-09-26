def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# output: Masala Chai
# Ginger Chai
# Matcha
# Oolong

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close() #closing the generator (memory cleanup)

# output: Waiting for chai order
# Stall closed, No more chai
