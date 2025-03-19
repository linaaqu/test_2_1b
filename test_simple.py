from homework2 import(
simple
)
import pytest

def test_simple_zero():
    assert simple(0) == "Ни простое, ни составное"

def test_simple_one():
    assert simple(1) == "Составное"

def test_simple_two():
    assert simple(2) == "Простое"

def test_simple_three():
    assert simple(3) == "Простое"

def test_simple_four():
    assert simple(4) == "Составное"

def test_simple_five():
    assert simple(5) == "Простое"

def test_simple_six():
    assert simple(6) == "Составное"

def test_simple_seven():
    assert simple(7) == "Простое"

def test_simple_large_prime():
    assert simple(101) == "Простое"

def test_simple_large_composite():
    assert simple(100) == "Составное"