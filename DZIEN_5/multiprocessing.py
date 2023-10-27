import multiprocessing
import time

def print_cube(num):
    time.sleep(3)
    print(f"Cube: {num**3}")

def print_square(num):
    print(f"Square: {num**2}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_square,args=(10,))
    p2 = multiprocessing.Process(target=print_cube,args=(10,))
    p1.start()
    p2.start()

    # p1.join(timeout=2)
    # p2.join()

    if p1.is_alive():
        p1.kill()

    print("Zakończono!")
