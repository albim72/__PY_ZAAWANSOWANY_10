class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołanie funkcji __str__()")
        if self.message:
            return f'{self.__class__.__name__}: {self.message}'
        else:
            return f'{self.__class__.__name__}: Brak informacji'


n = input("podaj literę alfabetu: (a-z) ")
try:
    if n == "a":
        raise MojaKlasaBledu("a jest już zarezerwowane....")
    else:
        print("dobry wybór!")
except MojaKlasaBledu as mkb:
    print(mkb)
