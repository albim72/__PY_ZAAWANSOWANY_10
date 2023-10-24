from figura import Figura
import math

#napisz klasę Kolo której konstruktor będzie oparty tylko na parametrze a reprezentującym promień koła
#w pliku main policz pole koła dla a = 5.5 (pi*a**2)

class Kolo(Figura):
    def __init__(self, a):
        super().__init__(a,0)

    def policz_pole(self):
        return math.pi*self.a**2



