def czytaj_l(lista):
    for i,j in enumerate(lista):
        print(f'element listy: {i+1} -> wartość: {j}')

def czytaj_s(slownik):
    for x,y in slownik.values():
        print(f"klucz: {x} -> wartość: {y}")
