from time_excercise import (
    generate_dates_2026,
    primes_naive,
    benchmark,
    primes_optimized,
)


def test_time_ex1():
    generate_dates_2026()


def test_time_prime_naives_ex2():
    benchmark(primes_naive)


def test_time_prime_optimized_ex2_2():
    benchmark(primes_optimized)
