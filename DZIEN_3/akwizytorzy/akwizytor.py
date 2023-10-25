from decimal import Decimal

class Akwizytor:
    """
    Pracownik,którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self,noweimie):
        self._imie = noweimie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nowenaz):
        self._nazwisko = nowenaz

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, noweubez):
        self._nr_ubezpieczenia = noweubez


    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError("Wartość sprzedaży nie może być ujemna")
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self,procent):
        if not(Decimal('0.0')<procent<=Decimal('30.0')):
            raise ValueError('Prowizja nie może być wartością 0 lub ujemną i nie może przekraczać 30%')
        self._prowizja = procent

    def zrobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))

    def __repr__(self):
        return ('Akwizytor: ' +
                f'numer ubezpieczenia: {self._nr_ubezpieczenia}\n'+
                f'{self.imie} {self.nazwisko}\n' +
                f'sprzedaż: {self.sprzedaz:.2f}\n' +
                f'prowizja: {self.prowizja:.2f}%\n')


