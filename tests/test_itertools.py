from itertools_excercise import loop_twice_over_generator
from memory_profiler import profile

@profile
def test_itertools_ex1():
    gen = (x for x in range(3))
    loop_twice_over_generator(gen)