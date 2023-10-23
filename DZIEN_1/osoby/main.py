from osoba import Osoba
from pracownik import Pracownik
from student import Student


print("_"*45)
os1 = Osoba("Jan",56,88,176)
print(os1)
n = 12
print(f'wiek osoby za {n} lat wynosi {os1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')
print(f'bmi ciała wynosi: {os1.bmi():.2f} -> {os1.opis_bmi()}')

print("_"*45)

em1 = Pracownik("Karol",50,80,180,"ABC","dyrektor",12,11200)
print(em1)
n=5
print(f'wiek osoby za {n} lat wynosi {em1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({em1.czypracownik()})')
# em1.kolor_oczu = "zielone"
em1.setoczy("zielony")
print(f'kolor oczu: {em1.getoczy()}')
print(f'bmi ciała wynosi: {em1.bmi():.2f} -> {em1.opis_bmi()}')

print("_"*45)

s1 = Student("Olaf",22,77,177,523423,"informatyka i matematyka",
             "informatyka",3)
print(s1)
n=10
print(f'wiek osoby za {n} lat wynosi {s1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s1.czypracownik()})')
# em1.kolor_oczu = "zielone"
s1.setoczy("piwne")
print(f'kolor oczu: {s1.getoczy()}')


print("_"*45)


s2 = Student("Olga",23,56,168,765756,"fizjoterapia",
             "fizjoterapia sportowa",4,"Medica","praktykantka",1,3000)
print(s2)
n=10
print(f'wiek osoby za {n} lat wynosi {s2.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s2.czypracownik()})')
print(f'kolor oczu: {s2.getoczy()}')

print("_"*45)


s3 = Student("Robert",22,80,178,8768768,"logistyka i transport",
             "transport",3,dyscyplina="biegi ULTRA",lata_upr=6,best_wynik="70km - 9h 12min 2s")
print(s3)
n=10
print(s3.infosport())
print(f'wiek osoby za {n} lat wynosi {s3.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({s3.czypracownik()})')
print(f'kolor oczu: {s3.getoczy()}')
print(f'bmi ciała wynosi: {s3.bmi():.2f} -> {s3.opis_bmi()}')

