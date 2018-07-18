#Ejercicio13

def Esprimo (num):
    cont=0
    divisor=1
    while divisor<(num+1):
        if num % divisor == 0:
            cont=cont+1
        divisor=divisor+1

    if cont == 2:
        c="Es PRIMO"
    else:
        c="No es PRIMO"

    return c

a=Esprimo(3)
print(a)

assert Esprimo(3) == "Es PRIMO"
assert Esprimo(3) != "No es PRIMO"




