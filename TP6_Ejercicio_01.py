# Implementar los metodos de la capa de negocio de socios.

from TP5.TP5_Ejercicio_01 import Socio
from TP5.TP5_Ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio=self.datos.buscar(id_socio)
        return socio



    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio=self.datos.buscar_dni(dni_socio)
        return socio

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios=self.datos.todos()
        return socios

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.datos.alta(socio)
            return True
        except:
            return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        rta= self.datos.baja(id_socio)
        return rta

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):

            rta=self.datos.modificacion(socio)
            if not rta:
                return False
            else:
                return True

        else:
            raise LongitudInvalida
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        i=0
        socios=self.datos.todos()
        for s in socios:
            if s.dni==socio.dni:
                raise DniRepetido
                return False

        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre) > NegocioSocio.MAX_CARACTERES) or (len(socio.nombre) < NegocioSocio.MIN_CARACTERES):
            raise LongitudInvalida
            return False
        elif (len(socio.apellido) > NegocioSocio.MAX_CARACTERES) or (len(socio.apellido) < NegocioSocio.MIN_CARACTERES):
            raise LongitudInvalida
            return False
        else:
            return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos())>self.MAX_SOCIOS:
            raise MaximoAlcanzado
            return False
        else:
            return True



