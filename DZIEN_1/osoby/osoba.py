class Osoba:
    def __init__(self,imie,wiek,waga,wzost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzost = wzost
        self.kolor_oczu = "brązowy"
        self.info()

    def __repr__(self):
        return f"jestem reprezentacją tekstową obiektu klasy Osoba -> imie: {self.imie}"

    def info(self):
        print("Utworzono nową instancję klasy Osoba....")

    def wiekza_n_lat(self,n):
        return self.wiek + n

    def czypracownik(self):
        return False

    def getoczy(self):
        return self.kolor_oczu

    def setoczy(self,nowy):
        self.kolor_oczu = nowy

    
    def bmi(self):
        return self.waga/(self.wzost/100)**2
    
    def opis_bmi(self):
        if self.bmi()<18.5:
            return "niedowaga"
        elif self.bmi() <=25:
            return "waga prawidłowa"
        elif self.bmi() <=30:
            return "nadwaga"
        elif self.bmi() <=35:
            return "otyłość I"
        elif self.bmi() <=40:
            return "otyłość II"
        else:
            return "otyłość III"


