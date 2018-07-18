#Ejercicio11

def cantD (a):
    cant=0
    cadena=str(a)
    for i in cadena:
        if i.isnumeric():
            cant=cant+1

    return cant

print(cantD(300))

assert cantD(300) == 3
assert cantD(300) != 5

