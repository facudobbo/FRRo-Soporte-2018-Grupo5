#Ejercicio3
def longitud(a):
    b=0
    for j in a:
        b=b+1
    return b

lista=["HOLA","JAJA"]
print(longitud(lista))
cadena="CHAU"
print(longitud(cadena))



assert longitud(lista) == 2
assert longitud(lista) != 6
assert longitud(cadena) == 4
assert longitud(cadena) != 2




