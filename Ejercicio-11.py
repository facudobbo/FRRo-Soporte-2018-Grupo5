
def divide(x,y):
    try:
        rta= x/y
    except ZeroDivisionError:
        print("No es posible dividir por 0")
    else:
        return rta

while True:
    try:
        x=int(input("Ingrese primer nro:"))
        break
    except ValueError:
        print("No es un nro, vuelva a ingresar")
while True:
    try:
        y=int(input("Ingrese segundo nro:"))
        break
    except ValueError:
        print("No es un nro, vuelva a ingresar")


rta=divide(x,y)
if rta != None:
    print(rta)
