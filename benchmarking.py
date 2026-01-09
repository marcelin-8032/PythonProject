import random
from memory_profiler import profile

@profile
def compute_pi(ndata=100_000):
    x_coord = (random.random() for i in range(ndata))
    y_coord = (random.random() for i in range(ndata))
    cpt = 0
    for x, y in zip(x_coord, y_coord):
        if x**2+y**2 < 1:
            cpt += 1
    return 4 * cpt / ndata



@profile
def compute_pi_list(ndata=100_000):
    x_coord = [random.random() for i in range(ndata)]
    y_coord = [random.random() for i in range(ndata)]
    cpt = 0
    for x, y in zip(x_coord, y_coord):
        if x**2+y**2 < 1:
            cpt += 1
    return 4 * cpt / ndata


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

