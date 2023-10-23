import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        # print(f'czas startu pomiaru: {starttime}')
        funkcja()
        endtime = time.time()
        # print(f'czas zakończenia pomiaru: {endtime}')
        wynik = endtime - starttime
        print(f"czas wykonania funckji: {wynik} s")
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@usypiacz
@pomiarczasu
def big_lista():
    sum([i**2 for i in range(10_000_000)])

big_lista()
big_lista()
big_lista()
big_lista()
