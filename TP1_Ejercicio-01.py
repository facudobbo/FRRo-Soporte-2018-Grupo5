#Ejercicio1

def maxi(a,b):
    if a>b:
        return a
    else:
        return b

x=maxi(9,4)
print(x)

assert maxi(9,4) == 9
assert maxi (9,4)!= 4
