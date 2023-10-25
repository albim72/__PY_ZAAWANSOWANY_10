from akwizytor import Akwizytor
from decimal import Decimal

class AkwizytorNaEtacie(Akwizytor):
    """
    Pracownik,którego wynagrodzenie jest połączeniem prowizji od sprzedaży i pensji
    """

    def __init__(self, imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja, pensja):
        super().__init__(imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja)
        self.pensja = pensja

    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota <= Decimal('0.00'):
            raise ValueError('Wynagrodzenie ryczałtowe nie może być ujemne lub równe zero!')
        self._pensja = kwota

    def zrobek(self):
        return super().zrobek() + self.pensja

    def __repr__(self):
        return 'Etatowy: ' + super().__repr__() + f'\n ryczałt: {self.pensja:.2f} zł'
    

    # __str__ -  komunikat tekstowy, rezprezentujący obiekt (komunikat błędu), ma pierwszeństwo przed __repr__
    # __repr__ - reprezentacja tekstowa obiektu


        


