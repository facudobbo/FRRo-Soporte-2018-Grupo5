# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import cmath

class Circulo:

    def __init__(self, radio):
        self.rad=radio

    def area(self):
        return cmath.pi * self.rad *self.rad

    def perimetro(self):
        return 2* cmath.pi* self.rad

c=Circulo(1)
print(c.area())
print(c.perimetro())

assert (c.area()==3.141592653589793)
assert (c.perimetro()==6.283185307179586)
