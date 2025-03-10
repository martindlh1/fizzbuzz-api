# tests/test_main.py
from src.fizzbuzz import generate_fizzbuzz


def test_generate_fizzbuzz():
    # Test case 1
    result = generate_fizzbuzz(2, 5, 1, 10)
    expected = ['1', 'fizz', '3', 'fizz', 'buzz', 'fizz', '7', 'fizz', '9', 'fizzbuzz']
    assert result == expected

    # Test case 2
    result = generate_fizzbuzz(3, 5, 1, 15)
    expected = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    assert result == expected
