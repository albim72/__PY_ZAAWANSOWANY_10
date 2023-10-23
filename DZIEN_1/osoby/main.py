from osoba import Osoba


print("_"*45)
os1 = Osoba("Jan",56,88,176)
print(os1)
n = 12
print(f'wiek osoby za {n} lat wynosi {os1.wiekza_n_lat(n)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("_"*45)


