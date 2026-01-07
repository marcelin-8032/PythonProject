from collections.abc import Sequence


# Excercise 1
def reverse(sequence: Sequence):
    for item in sequence[::-1]:
        yield item


# Excercise 2
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n):
    for i, value in enumerate(fib_generator()):
        if i == n:
            return value


# Excercise 3
def generate_large_file(filename, lines=1_000_000):
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(lines):
            f.write(f"Line number {i}\n")


# case 1 read from list
def read_file_list(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


# case 2 read from generator
def read_file_generator(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line


# Excercise 4
def search(sequence, target):
    for item in sequence:
        if isinstance(item, int):
            if item == target:
                return True
        elif isinstance(item, str):
            number = int(item.strip().split()[-1])
            if number == target:
                return True
    return False
