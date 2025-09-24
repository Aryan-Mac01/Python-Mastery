def pure_function(cups):
    return cups * 10

total_chai = 0

#not recommended
def impure_function(cups):
    global total_chai
    total_chai += cups

def recursive(n):
    if n == 0:
        return "All cups poured"
    return recursive(n-1)
print(recursive(3))


chai_types = ["light", "strong", "ginger", "strong"]

strong_chai = list(filter(lambda chai: chai=="strong", chai_types))
#strong_chai = ["strong", "strong"]
