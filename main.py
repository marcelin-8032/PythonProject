from tests.test_electric_vehicle import test_electric_vehicle
from tests.test_generator import (
    test_generator_ex1,
    test_generator_ex2,
    test_generator_ex3,
    test_generator_ex4,
)


def main():
    print("---------Bonnes pratriques-------")
    test_electric_vehicle()
    print("----------Method avancees generators-------")
    test_generator_ex1()
    test_generator_ex2()
    test_generator_ex3()
    test_generator_ex4()


if __name__ == "__main__":
    main()
