from app.fizzbuzz import fizzbuzz

from app.fizzbuzz import (
    fizzbuzz1,
    fizzbuzz2,
)

def test_works_with_1():
    # Arrange
    num = 1
    expected_answer = ["1"]

    # Act
    answer = fizzbuzz(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_works_with_2():
    # Arrange
    num = 2
    expected_answer = ["1", "2"]

    # Act
    answer = fizzbuzz(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_works_with_3():
    # Arrange
    num = 3
    expected_answer = ["1", "2", "Fizz"]

    # Act
    answer = fizzbuzz(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_works_with_5():
    # Arrange
    num = 5
    expected_answer = ["1", "2", "Fizz", "4", "Buzz"]

    # Act
    answer = fizzbuzz(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_works_with_15():
    # Arrange
    num = 15
    expected_answer = [
        "1", 
        "2", 
        "Fizz", 
        "4", 
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
        ]

    # Act
    answer = fizzbuzz(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz1_works_with_1():
    # Arrange
    num = 1
    expected_answer = ["1"]

    # Act
    answer = fizzbuzz1(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz1_works_with_3():
    # Arrange
    num = 3
    expected_answer = ["1", "2", "Fizz"]

    # Act
    answer = fizzbuzz1(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz1_works_with_5():
    # Arrange
    num = 5
    expected_answer = ["1", "2", "Fizz", "4", "Buzz"]

    # Act
    answer = fizzbuzz1(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz1_works_with_15():
    # Arrange
    num = 15
    expected_answer = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz"]

    # Act
    answer = fizzbuzz1(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz2_works_with_1():
    # Arrange
    num = 1
    expected_answer = ["1"]

    # Act
    answer = fizzbuzz2(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz2_works_with_3():
    # Arrange
    num = 3
    expected_answer = ["1", "2", "Fizz"]

    # Act
    answer = fizzbuzz2(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz2_works_with_5():
    # Arrange
    num = 5
    expected_answer = ["1", "2", "Fizz", "4", "Buzz"]

    # Act
    answer = fizzbuzz2(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]


def test_fizzbuzz2_works_with_15():
    # Arrange
    num = 15
    expected_answer = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz"]

    # Act
    answer = fizzbuzz2(num)

    # Assert
    assert len(answer) == len(expected_answer)

    for index in range(0, len(expected_answer)):
        assert answer[index] == expected_answer[index]
