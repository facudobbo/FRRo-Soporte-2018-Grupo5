# Implementar los metodos de la capa de datos de socios.
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from TP5.Ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)


    def buscar(self, id_socio):
        per=self.session.query(Socio).filter(Socio.id==id_socio).first()
        return per

    def buscar_dni(self, dni_socio):

        per=self.session.query(Socio).filter(Socio.dni==dni_socio).first()
        return per

    def todos(self):

        lp = self.session.query(Socio).all()
        return lp

    def borrar_todos(self):
        try:
            rta=True
            per=self.session.query(Socio).all()
            for s in per:
                self.session.delete(s)
            self.session.commit()
        except:
            rta=False

        return rta

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        try:
            soc=self.session.query(Socio).filter(Socio.id==id_socio).first()
            self.session.delete(soc)
            self.session.commit()
            rta=True
        except:
            rta=False
        return rta


    def modificacion(self, socio):
        self.session.query(Socio).filter(Socio.id == socio.id).update({Socio.dni:socio.dni, Socio.nombre:socio.nombre, Socio.apellido:socio.apellido})
        self.session.commit()

        return socio


def pruebas():
    # alta
    datos = DatosSocio()
    datos.borrar_todos()


    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0
    

    # baja
    assert datos.baja(socio.id) == True


    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni

    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0
    assert datos.borrar_todos()== True



if __name__ == '__main__':
    pruebas()
