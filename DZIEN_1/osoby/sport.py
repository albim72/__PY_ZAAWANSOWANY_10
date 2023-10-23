class Sport:
    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.dyscyplina_sportu = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik

    def __repr__(self):
        return f'dyscyplina: {self.dyscyplina_sportu}, lata uprawiania: {self.lata_upr}, życiówka: {self.best_wynik}'


        
