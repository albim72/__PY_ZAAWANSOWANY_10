from external import Musician,Dancer

class Club:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Klub {self.name}"

    def organize_event(self):
        return "koncert muzyki z oprawą taneczną..."
