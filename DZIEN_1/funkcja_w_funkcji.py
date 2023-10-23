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


