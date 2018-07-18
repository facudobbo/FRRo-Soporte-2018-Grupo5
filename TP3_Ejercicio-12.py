#Ejercicio 12
#Con Alchemy usando SQLite  cree un modelo persona  con los campos del ejercicio 1 .
# Hacer un programa que muestre la opción 1 Alta ,2 Listar ,  3 Baja .
# La Opcion 1 Alta  ingresa una persona a la tabla .
# La Opcion 2 Listar muestra la el listado de las persona.
# La Opcion 3 se ingresa idpersona para borrarla borra .
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    fechaNac= Column(String(8), nullable=False)
    dni= Column(String(10),nullable=False)
    altura= Column(Integer)

engine = create_engine('sqlite:///sqlalchemy_ejemplo0.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def creaTabla():
    Base.metadata.create_all(engine)

def insertaReg():
    oper = Persona()
    oper.nombre = input('Ingrese Nombre:')
    oper.fechaNac=input('Ingrese Fecha de Nacimiento:')
    oper.dni=int(input('Ingrese DNI'))
    oper.altura=input('Ingrese Altura')
    session.add(oper)
    session.commit() #---<<<<Graba

def consulta():
    lp = session.query(Persona).all() #--- lista
    if lp:
        print('Lista de personas:')
        for p in lp:
            print(p.id, p.nombre,p.fechaNac, p.dni, p.altura)
    else:
        print("No hay personas")

def baja():
    id=int(input("Ingrese ID:"))
    per=session.query(Persona).filter(Persona.id==id).first()
    if per:
        session.delete(per)
        session.commit()
    else:
        print("No existe persona con ese ID")

if __name__ == '__main__':
    creaTabla()
    rta=0
    while rta!=4:
        rta=int (input('1-Alta \n 2-Listado \n 3-Baja\n 4-Salir\n'))
        if rta==1:
            insertaReg()
        elif rta==2:
            consulta()
        elif rta==3:
            baja()
        else: print("Opcion incorrecta")
