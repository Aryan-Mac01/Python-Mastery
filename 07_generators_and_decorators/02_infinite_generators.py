def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

for _ in range(3):
    print(next(refill))

# #output: Refill #1
# Refill #2
# Refill #3