#Ejercicio10

def mas_larga(a,b):
    c=0
    for j in a:
        c=c+1
    d=0
    for i in b:
        d=d+1
    if c>d:
        return a
    else:
        return b
cad1="hola"
cad2="Holaaaa"
print(mas_larga(cad1,cad2))

assert  mas_larga(cad1, cad2) == "Holaaaa"
assert  mas_larga(cad1, cad2) != "hola"


