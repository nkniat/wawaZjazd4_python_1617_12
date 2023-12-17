from cw5a_funkcje import *

def test_0():
    assert add(2, 2) == 4
    assert add(-2, -4) == -6
    assert add(2.1, 0.9) == 3


def test_1():
    assert multiply(2,2) == 4
    assert multiply(134,0) == 0
    #assert multiply(100, 1.1) == 110, "Test mnożenia zmiennoprzecinkowego niezaliczony"
    assert compare_floats(multiply(100, 1.1), 110)

def test_2():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"


def test_3():
    assert fizzbuzz(0) == None
    assert fizzbuzz("kot") == None
