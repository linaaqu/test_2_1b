from homework2 import(
group_words
)
import pytest

def test_group_words_empty():
    assert group_words([]) == {}

def test_group_words_one_word():
    assert group_words(["cat"]) == {3: ["cat"]}

def test_group_words_different_lengths():
    assert group_words(["cat", "dog", "bird"]) == {3: ["cat", "dog", "bird"]}

def test_group_words_same_length():
    assert group_words(["cat", "dog"]) == {3: ["cat", "dog"]}

def test_group_words_mixed_lengths():
    assert group_words(["a", "bb", "ccc"]) == {1: ["a"], 2: ["bb"], 3: ["ccc"]}

def test_group_words_empty_string():
    assert group_words(["", "word"]) == {0: [""], 4: ["word"]}

def test_group_words_numbers():
    assert group_words(["1", "12"]) == {1: ["1"], 2: ["12"]}

def test_group_words_special_chars():
    assert group_words(["!", "??"]) == {1: ["!"], 2: ["??"]}

def test_group_words_unicode():
    assert group_words(["привет", "мир"]) == {6: ["привет", "мир"], 3: ["мир"]}

def test_group_words_duplicates():
    assert group_words(["cat", "cat", "dog"]) == {3: ["cat", "cat", "dog"]}