from tests.test_decorator import (
    test_decorator_ex1,
    test_decorator_ex2,
    test_decorator_ex3,
    test_decorator_ex4,
)
from tests.test_electric_vehicle import test_electric_vehicle
from tests.test_generator import (
    test_generator_ex1,
    test_generator_ex2,
    test_generator_ex3,
    test_generator_ex4,
)
from tests.test_itertools import test_itertools_ex1
from tests.test_regular_expression import (
    test_regular_expression_ex1,
    test_regular_expression_ex2,
    test_regular_expression_ex3,
    test_regular_expression_ex4,
)
from tests.test_time import (
    test_time_ex1,
    test_time_prime_naives_ex2,
    test_time_prime_optimized_ex2_2,
)


def main():
    print("---------Bonnes pratriques-------")
    test_electric_vehicle()

    print("----------Method avancees generators-------")
    test_generator_ex1()
    print("-----------------")
    test_generator_ex2()
    print("-----------------")
    test_generator_ex3()
    print("-----------------")
    test_generator_ex4()

    print("----------Method avancees décorateurs-------")
    test_decorator_ex1()
    print("-----------------")
    test_decorator_ex2()
    print("-----------------")
    test_decorator_ex3()
    print("-----------------")
    test_decorator_ex4()

    print("----------time-------")
    test_time_ex1()
    print("-----------------")
    test_time_prime_naives_ex2()
    print("-----------------")
    test_time_prime_optimized_ex2_2()

    print("----------regular_expression-------")
    test_regular_expression_ex1()
    print("-----------------")
    test_regular_expression_ex2()
    print("-----------------")
    test_regular_expression_ex3()
    print("-----------------")
    test_regular_expression_ex4()
    
    print("----------Itertools-------")
    test_itertools_ex1()


if __name__ == "__main__":
    main()
