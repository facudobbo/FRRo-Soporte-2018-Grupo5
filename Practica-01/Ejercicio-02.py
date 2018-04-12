#Ejercicio2

def max_de_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

x=max_de_tres(6,5,6)
print(x)
