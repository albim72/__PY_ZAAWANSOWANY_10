class UjemneN(Exception):
    def __init__(self,n):
        self.n = n
        
    def __str__(self):
        return f'została zadana wartość n={self.n}. Wartość argumentu silnii nie może być ujemna!'
