#przykład 1

def witaj(imie):
    return f'Miło Cię znowu widzieć {imie}'

def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'

def bonus(punkty,bonus):
    if punkty > 50:
        return punkty + bonus
    else:
        return punkty

#funkcja wyższego rzędu
def osoba(funkcja,*args):
    return funkcja(*args)


print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Ela",67,99))
print(osoba(bonus,88,20))

#przykład 2

def rejestracja(oplata):
    def lista(nr):
        return f"jesteś na liście zawodników {nr}. Opłacone."
    def brak():
        return "brak opłaty. Uzupełnij w ciągu 3 dni..."
    def error():
        return "błędny kod wpłaty..."

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)(456))
print(rejestracja(22)())
print(rejestracja(0)())

#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("zakończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f'zawijanie czekoladek w {w_co}')

zw = startstop(zawijanie)
print(zw)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na torcie urodzinowym!')

dmuchanie("świeczek")

@startstop
def fx(n):
    print(f'wynik = {n*2-1}')

fx(9)

liczby = [45,12,78,90,24,-34,0,23,245,100,4,6,7,3,11,-3,-110]
