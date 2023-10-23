from osoba import Osoba

class Pracownik(Osoba):
    def __init__(self, imie, wiek, waga, wzost, firma, stanowisko, lata_pracy, wynagrodzenie):
        super().__init__(imie, wiek, waga, wzost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.lata_pracy = lata_pracy
        self.wynagrodzenie = wynagrodzenie
        
    def __repr__(self):
        return f'dane pracownika -> {self.firma}, stanowisko: {self.stanowisko}, wynagordzenie: {self.wynagrodzenie} zł'

    def czypracownik(self):
        return True
        
