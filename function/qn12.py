# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.
import random


def multiplyWithRandomNumber(num): return num*random.randint(1, 100)


if __name__ == "__main__":
    print(multiplyWithRandomNumber(10))
