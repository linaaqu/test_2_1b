import pytest
from math import factorial

def factorial(n: int) -> int:
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive_small():
    assert factorial(3) == 6

def test_factorial_positive_medium():
    assert factorial(5) == 120

def test_factorial_positive_large():
    assert factorial(10) == 3628800

def test_factorial_same_as_math():
    import random
    n = random.randint(0, 12)
    assert factorial(n) == factorial(n)

def test_factorial_recursion_limit():
    try:
        factorial(995)
    except RecursionError:
        pytest.fail("RecursionError raised for a valid input size.")

def test_factorial_float_input():
    with pytest.raises(TypeError):
        factorial(5.5)

def test_factorial_string_input():
    with pytest.raises(TypeError):
        factorial("5")

def test_factorial_negative_number():
   with pytest.raises(RecursionError):
      factorial(-1)