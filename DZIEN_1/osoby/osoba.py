class Osoba:
    def __init__(self,imie,wiek,waga,wzost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzost = wzost
        self.kolor_oczu = "brązowy"
        self.info()

    def info(self):
        print("Utworzono nową instancję klasy Osoba....")
