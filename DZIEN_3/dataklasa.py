from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x = x

zlicz = Liczba(2)
print(zlicz.x)

@dataclass
class DLiczba:
    x:int

dlicz = DLiczba(4.7)
print(dlicz.x)

@dataclass
class Dane:
    nazwa:str
    licznik:int = 0
    cena:float = 0.0

    # def __init__(self,nazwa,magazyn):
    #     self.nazwa = nazwa
    #     self.magazyn = magazyn

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self,nl):
        self._licznik = nl



p = Dane("pudełko 5",4,11.2)
print(f'produkt: {p.nazwa} -> cena: {p.cena}zł -> do zapłaty: {p.cena*p.licznik} zł')

p.licznik = 16
print(f'produkt: {p.nazwa} -> cena: {p.cena}zł -> do zapłaty: {p.cena*p.licznik} zł')





