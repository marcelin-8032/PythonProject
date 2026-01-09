from datetime import date, timedelta
import math
import timeit


def generate_dates_2026(filename="dates_2026.txt"):

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    start = date(2026, 1, 1)
    end = date(2026, 12, 31)
    delta = timedelta(days=1)

    with open(filename, "w", encoding="utf-8") as file:
        current = start
        while current <= end:
            weekd = weekdays[current.weekday()]
            file.write(f"{current.strftime('%d/%m/%Y')} {weekd}\n")
            current += delta


def benchmark(func, repeat=3, number=100):

    times = timeit.repeat(stmt=func, repeat=repeat, number=number)

    best = min(times) / number
    avg = sum(times) / (repeat * number)

    print(f"Best time : {best:.8f} sec per run")
    print(f"Average time : {avg:.8f} sec per run")


def primes_naive():
    primes = []
    for n in range(2, 1001):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes


def primes_optimized():
    primes = []
    for n in range(2, 1001):
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        else:
            primes.append(n)
    return primes
