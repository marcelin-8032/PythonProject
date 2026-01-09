
from itertools_excercise import loop_twice_over_generator


def test_itertools_ex1():
    gen = (x for x in range(3))
    loop_twice_over_generator(gen)