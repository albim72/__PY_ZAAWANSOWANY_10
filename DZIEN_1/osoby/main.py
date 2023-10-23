from osoba import Osoba
from pracownik import Pracownik


print("_"*45)
os1 = Osoba("Jan",56,88,176)
print(os1)
n = 12
print(f'wiek osoby za {n} lat wynosi {os1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("_"*45)

em1 = Pracownik("Karol",50,80,180,"ABC","dyrektor",12,11200)
print(em1)
n=5
print(f'wiek osoby za {n} lat wynosi {em1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({em1.czypracownik()})')
# em1.kolor_oczu = "zielone"
em1.setoczy("zielony")
print(f'kolor oczu: {em1.getoczy()}')

print("_"*45)







