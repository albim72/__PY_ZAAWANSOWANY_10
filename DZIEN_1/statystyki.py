liczby = [900,1001,-767,0,57,8,4-3,15,67,97,222,-333,567,789,-876,32,1,-2]

def pokaz_statystyki(dane:tuple)->tuple:
    minimum:int = min(dane)
    maximum:int = max(dane)
    rozstep:int = maximum - minimum
    sr_arytm:float = sum(dane)/len(dane)
    return [minimum, maximum, rozstep, sr_arytm]

wynik = pokaz_statystyki(liczby)
print(type(wynik))
print(wynik)

mini,maxi,roz,sa = pokaz_statystyki(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, średnia arytmrtyczna: {sa}')

a = 8
print(a)
print(type(a))

a = "jesień"
print(a)
print(type(a))

g:float = 8.3324
print(g)
print(type(g))

g= True
print(g)
print(type(g))
