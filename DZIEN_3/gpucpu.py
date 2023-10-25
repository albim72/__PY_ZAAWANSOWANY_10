from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def cpufunction(a):
    for i in range(100_000_000):
        a[i] += 1

@jit(target_backend='cuda')
def gpufunction(a):
    for i in range(100_000_000):
        a[i] += 1

if __name__ == '__main__':
    n = 100_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    cpufunction(a)
    print(f'czas działania na CPU: {timer()-start}')

    start = timer()
    gpufunction(a)
    print(f'czas działania na GPU: {timer() - start}')

