#Ejercicio 8
def superposicion(a,b):
 igual = False
 for i in a:
  for j in b:
   if i == j:
    igual= True
 return igual




print(superposicion("hola","chu"))

