class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B,C):
    pass 
#output: "B: Masala blend" because B is called first

class D(C,B):
    pass 
#output: "C: Herbal blend" because C is called first

cup = D()
print(cup.label)