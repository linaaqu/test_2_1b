from homework2 import(
elements
)
import pytest

def elements(input_list):
    return list(set(input_list))

def test_elements_empty_list():
    """Test with an empty list."""
    assert elements([]) == []

def test_elements_unique_list():
    assert elements([1, 2, 3]) == [1, 2, 3]

def test_elements_duplicate_elements():
    assert set(elements([1, 2, 2, 3, 4, 4, 5])) == {1, 2, 3, 4, 5}

def test_elements_mixed_data_types():
    assert set(elements([1, "a", 2.0, "a", 1])) == {1, "a", 2.0}

def test_elements_already_unique():
    input_list = [10, 20, 30, 40, 50]
    assert elements(input_list) == input_list

def test_elements_all_duplicates():
    assert elements([7, 7, 7, 7, 7]) == [7]

def test_elements_negative_numbers():
    assert set(elements([-1, -2, -2, -3, -4, -1])) == {-4, -3, -2, -1}

def test_elements_zero():
    assert set(elements([0, 0, 1, 2, 0, 3])) == {0, 1, 2, 3}

def test_elements_strings_with_duplicates():
    assert set(elements(["apple", "banana", "apple", "orange"])) == {"apple", "banana", "orange"}

def test_elements_large_list():
    large_list = list(range(1000)) + list(range(500))
    assert len(elements(large_list)) == 1000