from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class DuzaFirma:
    def __repr__(self):
        return "Właściciel firmy, otrzymuje wypłatę na podstawie zysków firmy z poprzedniego roku"

    def zarobek(self):
        return Decimal('10_000_000')

# print(dir(Akwizytor))
# print(help(Akwizytor.__repr__))

df = DuzaFirma()
s = Akwizytor('Jan','Kot',58734857,Decimal('456700.0'),Decimal('8.9'))
c = AkwizytorNaEtacie('Olga','Nowak',6457557,Decimal('513900.0'),
                      Decimal('7.2'),Decimal('4500.0'))

pracownicy = [c,s,df]

for pr in pracownicy:
    print(pr)
    print(f'{pr.zarobek():,.2f} zł\n')
