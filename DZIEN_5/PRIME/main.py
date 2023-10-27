import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_000),(95_000,133_000)]

def synchronicznie():
    starttime = time.time()
    for pair in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_suma)
    endtime=time.time()
    print(f'całkowity czas wyzanczenia sum - synchronicznie: {endtime-starttime} s')

def main():
    synchronicznie()

if __name__ == '__main__':
    main()
