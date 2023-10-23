from pracownik import Pracownik
from sport import Sport
from ekstra import Empty


class Student(Pracownik,Sport,Empty):
    def __init__(self, imie, wiek, waga, wzost, id_studenta, wydzial, kierunek, rok_stud, 
                 firma, stanowisko, lata_pracy, wynagrodzenie, dyscyplina,lata_upr,best_wynik):
        Pracownik.__init__(self,imie, wiek, waga, wzost, firma, stanowisko, lata_pracy, wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.id_studenta = id_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud
        
    def __repr__(self):
        return  (f'student nr {self.id_studenta}, wydział: {self.wydzial} , '
                 f'kierunek:{self.kierunek}, rok studiów: {self.rok_stud}')

    def czypracownik(self):
        return self.firma != ""
    
    
