odp = input("Czy Ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n) ")
if odp.lower() == "t":
    required = True
else:
    required = False
    
def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def brak(self):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak
            
