#Ejercicio6

def inversa(a):
    b=a[::-1]
    return b

cad="hola"
inv=inversa(cad)
print(inv)

assert  inversa(cad) == "aloh"
assert  inversa (cad) != "hola"
