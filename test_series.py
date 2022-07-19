import pytest
import pytest_watch
from series import fibonacci, lucas, sum_series


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_four():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_five():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_six():
    actual = fibonacci(18)
    expected = 2584
    assert actual == expected


def test1_one():
    actual = lucas(1)
    expected = 2
    assert actual == expected


def test1_two():
    actual = lucas(2)
    expected = 1
    assert actual == expected


def test1_three():
    actual = lucas(3)
    expected = 3
    assert actual == expected


def test1_four():
    actual = lucas(5)
    expected = 7
    assert actual == expected


def test1_five():
    actual = lucas(10)
    expected = 76
    assert actual == expected


def test1_six():
    actual = lucas(18)
    expected = 3571
    assert actual == expected


def test2_one():
    actual = sum_series(1)
    expected = 2
    assert actual == expected


def test2_two():
    actual = sum_series(2)
    expected = 2
    assert actual == expected


def test2_three():
    actual = sum_series(3)
    expected = 5
    assert actual == expected


def test2_four():
    actual = sum_series(5)
    expected = 12
    assert actual == expected

def test2_five():
    actual = sum_series(10)
    expected = 131
    assert actual == expected


def test2_six():
    actual = sum_series(18)
    expected = 6155
    assert actual == expected
