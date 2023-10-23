from bfunkcje.readdata import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik

    def czytaj_lista(self):
        return czytaj_l(self.lista)

    def czytaj_slownik(self):
        return czytaj_s(self.slownik)
