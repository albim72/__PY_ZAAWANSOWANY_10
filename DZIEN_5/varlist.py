import threading
from globalvar import n

def worker(num,shared_variable):
    shared_variable[0] = shared_variable[0] + 1
    # shared_variable.append(num)
    print(f"Wątek {threading.current_thread().name} zwiekszył zmienną współdzieloną do {shared_variable} "
          f"dodając wartość {num}")


shared_variable = [0]

threads = []
for i in range(1000):
    t = threading.Thread(target=worker,args=(i,shared_variable))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Zmienna współdzielona po zakończeniu pracy wszystkich wątków: {shared_variable}")
