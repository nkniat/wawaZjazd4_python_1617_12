def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def compare_floats(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def fizzbuzz(number):
    if isinstance(number, int) and number > 0:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)
    return None

