#Ejercicio7

def es_palindromo(a):
    b=a[::-1]
    if a==b:
        return True
    else:
        return False
cad="radar"
cad2="radarrr"
print(es_palindromo(cad))
print(es_palindromo(cad2))




