from pojazd import Pojazd

pj = Pojazd()
odl = 578
jd = 51
cn = 6.14

print(f'spalanie [l/100km]: {pj.spalanie(odl,jd):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {pj.kosztyprzejazdu(odl,jd,cn):.2f} zł')
print(pj.dane_silnika("diesel",2.2))
print(pj.stan("samochód nie był nigdy uszkodozny",245600,"liczba remontów: 12"))
