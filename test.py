# from math import fact
#import pytest
from homework2 import(
    fact,
    simple,
    elements,
    group_words
) 

def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(5) == 120
    assert fact(10) == 3628800
    assert fact(12) == 479001600
    assert fact(4) == 24
    assert fact(8) == 40320


def test_simple():
    assert simple(0) == "Ни простое, ни составное"
    assert simple(1) == "Простое"
    assert simple(2) == "Простое"
    assert simple(3) == "Простое"
    assert simple(4) == "Составное"
    assert simple(5) == "Простое"
    assert simple(7) == "Простое"
    assert simple(9) == "Составное"
    assert simple(11) == "Простое"
    assert simple(100) == "Составное"


def test_elements():
    assert elements([1,2,2]) == {1,2}
    assert elements([2,2,2]) == {2}
    assert elements([1,2,3]) == {1,2,3}
    assert elements([1,2,1,2,1,2]) == {1,2}
    assert elements([1]) == {1}
    assert elements([1,2,2,4,3,3,3,3,3,3,3,3,3]) == {1,2,3,4}
    assert elements([2,2,2,1,1,1,1,1,1,]) == {1,2}
    assert elements([1,2,3,1,2,3,1,2,3]) == {1,2,3}
    assert elements([6,7,5,6,5,6,7]) == {5,6,7}
    assert elements([1,2,3,4,5,6,7,8,9]) == {1,2,3,4,5,6,7,8,9}

def test_group_words_empty():
    assert group_words(words = ["cat"]) == {3: ["cat"]}
    assert group_words(words = ["cat", "dog", "bird"]) == {3: ['cat', 'dog'], 4: ['bird']}
    assert group_words(words = ["cat", "dog"]) == {3: ["cat", "dog"]}
    assert group_words(words = ["a", "bb", "ccc"]) == {1: ["a"], 2: ["bb"], 3: ["ccc"]}
    assert group_words(words = ["", "word"]) == {0: [""], 4: ["word"]}
    assert group_words(words = ["1", "12"]) == {1: ["1"], 2: ["12"]}
    assert group_words(words = ["!", "??"]) == {1: ["!"], 2: ["??"]}
    assert group_words(words = ["привет", "мир"]) == {6: ['привет'], 3: ['мир']}
    assert group_words(words = ["cat", "cat", "dog"]) == {3: ["cat", "cat", "dog"]}