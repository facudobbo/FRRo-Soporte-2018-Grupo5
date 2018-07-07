# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.ba=base
        self.al=altura


    def area(self):
        return self.ba * self.al

r=Rectangulo(5,2)

print(r.area())

assert(r.area()==10)
