

def programa():
    b=0
    i=0
    a=[]
    b=input("Ingrese un numero")
    while b != 'fin':
        if b.isnumeric:
          a.append(b)
        b=input("Ingrese un numero")
    return a





b=programa()
print(max(b))
print(min(b))


