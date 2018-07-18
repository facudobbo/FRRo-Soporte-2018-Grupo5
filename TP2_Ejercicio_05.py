# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from Ejercicio_04 import Estudiante
estudiantes=[]

def organizar_estudiantes(estudiantes):
    isi=0
    im=0
    iq=0
    ie=0
    ic=0
    for i in estudiantes:
        if i.carrera=='ISI':
            isi=isi+1
        elif i.carrera=='IQ':
            iq=iq+1
        elif i.carrera=='IM':
            im=im+1
        elif i.carrera=='IE':
            ie=ie+1
        elif i.carrera=='IC':
            ic=ic+1
    dicc={'ISI':isi, 'IQ':iq, 'IM':im,'IE':ie, 'IC':ic }
    return  dicc

b=Estudiante('Facu',21,'H',0,0,'ISI',2015,10,5)
c=Estudiante('Rafa',21,'H',0,0,'ISI',2015,10,5)
d=Estudiante('Cami',20,'M',0,0,'IE',2015,15,5)

estudiantes.append(d)
estudiantes.append(b)
estudiantes.append(c)

dicc=organizar_estudiantes(estudiantes)
print(list(dicc.keys()))

assert (list(dicc.keys())==['ISI', 'IQ', 'IM', 'IE', 'IC'])
