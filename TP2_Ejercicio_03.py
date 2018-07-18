# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

import random
class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nom=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.alt=altura
        self.dni= self.generar_dni()


    def es_mayor_edad(self):
        if self.edad>= 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')

    # llamarlo desde __init__
    def generar_dni(self):
        return random.randrange(10000000,99999999)


    def print_data(self):
        print('\n',self.nom,'\n',self.dni,'\n',self.edad,'\n',self.sexo,'\n',self.peso,'\n',self.alt)

p=Persona('Caro',21,'M',1,1)
p.es_mayor_edad()
p.print_data()
#El dni es aleatorio
assert(p.nom=='Caro')
assert(p.edad==21)
assert(p.sexo=='M')
assert(p.peso==1)
assert(p.alt==1)
