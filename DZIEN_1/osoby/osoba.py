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

