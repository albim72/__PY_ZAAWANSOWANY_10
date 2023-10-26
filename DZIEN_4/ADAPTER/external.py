class Musician:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"muzyk {self.name}"

    def play(self):
        return "gra muzykę!"


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"tancerka {self.name}"

    def dance(self):
        return "tańczy przy muzyce!"
