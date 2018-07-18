# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).


import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fecha=nacimiento
        pass

    def edad(self):
        h=datetime.datetime.now()
        if (h.month > self.fecha.month) or ((h.month==self.fecha.month) and (h.day>=self.fecha.day)):
            print('Tiene',h.year- self.fecha.year, 'anios')
        else:
            print('Tiene',h.year- self.fecha.year-1,'anios')
        pass

f=datetime.datetime(1997,4,8)
p=Persona(f)
p.edad()


