# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import random
import datetime
class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nom=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.alt=altura
        self.dni= self.generar_dni()

    def generar_dni(self):
        return random.randrange(10000000,99999999)


class Estudiante(Persona):

    def __init__(self,nombre,edad,sexo,peso,altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self,nombre,edad,sexo,peso,altura)
        self.carrera=carrera
        self.anio=anio
        self.cant_materias=cantidad_materias
        self.apro=cantidad_aprobadas

    def avance(self):
        a=self.apro/self.cant_materias*100
        print('Porcentaje de la carrera aprobada:',a,'%')

    # implementar usando modulo datetime
    def edad_ingreso(self):
       b=datetime.date.today()
       print('Ingreso a los:',self.edad-(b.year-self.anio))
e=Estudiante('Caro',25,'M',1,1,'ISI',2010,40,10)
e.avance()
e.edad_ingreso()
