import itertools
import sys
import time
from generator import (
    fib,
    generate_large_file,
    read_file_generator,
    read_file_list,
    reverse,
    search,
)


def test_generator_ex1():
    rev = reverse([1, 2, 3])
    for number in rev:
        print(number)


def test_generator_ex2():
    print(fib(3))
    print(fib(6))
    print(fib(10))


def test_generator_ex3():
    filename = "larg_file.txt"

    # generate file
    generate_large_file(filename, lines=1_000_000)
    list_content = read_file_list(filename)
    generator_content = read_file_generator(filename)

    # compare the sizes
    print("Size of list: ", sys.getsizeof(list_content), "bytes")
    print("Size of generator: ", sys.getsizeof(generator_content), "bytes")

    # verifiy elements
    print("\nfirst 5 elements from list: ")
    print(list_content[:5])

    print("\nfirst 5 elements from generator: ")
    print(list(itertools.islice(generator_content, 5)))


def test_generator_ex4():

    TARGET = 500_000

    numbers_list = list(range(1_000_001))

    # search in list
    start = time.perf_counter()
    found_list = search(numbers_list, TARGET)
    exec_time_list = time.perf_counter() - start

    # search in generator
    numbers_gen = (i for i in range(1_000_001))

    start = time.perf_counter()
    found_gen = search(numbers_gen, TARGET)
    exec_time_gen = time.perf_counter() - start

    print("Found in list: ", found_list)
    print("Time (list): ", exec_time_list)

    print("Found in gen: ", found_gen)
    print("Time (gen): ", exec_time_gen)
