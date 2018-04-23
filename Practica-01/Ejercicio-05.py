#Ejercicio5
def multip(a):
    b=1
    for i in a:
        b=b*i
    return b


lista=[2,3,5]
print(multip(lista))

assert  multip(lista) ==30
assert  multip(lista) != 35


