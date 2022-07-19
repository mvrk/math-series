import pytest
import pytest_watch


def fibonacci(n):
    if n < 0:
        print("Please enter a positive integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    if n < 0:
        print("Please enter a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, p=0, q=1):

    if n < 0:
        print("Please enter a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 2
    else:
        return fibonacci(n - 2) + fibonacci(n - 1) + lucas(n - 2) + lucas(n - 1)


if __name__ == "__main__":
    n = input("Please enter a number: ")
    print(f"The {n}th fibonacci number is {fibonacci(int(n))}, the {n}th lucas number is {lucas(int(n))}, the sum of those two is {sum_series(int(n))}.")
