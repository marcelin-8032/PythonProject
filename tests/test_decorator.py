from decorator import (
    deprecated,
    mesure_execution_time,
    mesure_execution_with_threshold_time,
    singleton,
)
from generator import search


@mesure_execution_time
def test_decorator_ex1():
    TARGET = 500_000
    numbers_list = list(range(1_000_001))
    found_list = search(numbers_list, TARGET)
    print("found_list_ex1", found_list)


@mesure_execution_with_threshold_time(0.05)
def test_decorator_ex2():
    TARGET = 500_000
    numbers_list = list(range(1_000_001))
    found_list = search(numbers_list, TARGET)
    print("found_list_ex2", found_list)


@singleton
class DatabaseConnection:
    def __init__(self):
        print("Creating database connection")


def test_decorator_ex3():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print("Is the two db instance are the same instance: ", db1 is db2)


@deprecated("Use new_method() instead!!!!!")
def test_decorator_ex4():
    print("Executing my old method")
