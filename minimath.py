from math import sqrt


class MyMath:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def substraction(a, b):
        return a - b

    @staticmethod
    def pow(a, b):
        return a ** b

    @staticmethod
    def sqrt(a):
        return sqrt(a)   
    

print(MyMath.subtraction(10, 10))
print(MyMath.addition(10, 10))
print(MyMath.pow(10, 10))
print(MyMath.division(10, 10))
print(MyMath.multiplication(10, 10))
print(MyMath.sqrt(100))
