from multiprocessing import Pool, cpu_count
from time import sleep, time, ctime
import logging


def factorize(*args):
    result = []
    j = 1
    for number in args:
        factors = []
        for j in range(1, number + 1):
            if number % j == 0:
                factors.append(j)
        result.append(factors)
    return result


def callback(result):
    print(f"Result in callback: {result}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    numbers = (128, 255, 99999, 10651060)
    factors_list = factorize(*numbers)
    factors_list = factorize(*numbers)
    print(f"Count CPU: {cpu_count()}")
    for factors in factors_list:
        print(factors)
