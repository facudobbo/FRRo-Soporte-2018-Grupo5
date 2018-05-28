

import datetime
class Ejercicio:

    def __init__(self,fecha):
        self.fecha=fecha

    def inicio(self):
        if self.fecha.month<=6:
            anio=self.fecha.year -1
            fe=datetime.datetime(anio,7,1)

        else:
            fe=datetime.datetime(self.fecha.year,7,1)
        return fe

    def fin (self):
        if self.fecha.month>5:
            anio=self.fecha.year + 1
            fe=datetime.datetime(anio,6,30)

        else:
            fe=datetime.datetime(self.fecha.year,6,30)
        return fe




f=datetime.datetime(2017,5,1)
e=Ejercicio(f)

print(e.fin())

