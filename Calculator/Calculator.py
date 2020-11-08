from Calculator.Addition import addition
from Calculator.Subtraction import subtract
from Calculator.Multiplication import multipli
from Calculator.Division import division
from Calculator.Square import square
from Calculator.SquareRoot import root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multipli(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = root(a)
        return self.result