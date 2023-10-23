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
