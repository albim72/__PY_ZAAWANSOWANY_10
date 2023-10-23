def czytaj_l(lista):
    for i,j in enumerate(lista):
        print(f'element listy: {i+1} -> wartość: {j}')

def czytaj_s(slownik):
    for x,y in slownik.items():
        print(f"klucz: {x} -> wartość: {y}")
