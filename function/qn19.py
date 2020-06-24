# 19. Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce

getFibonacciSeries = lambda num: reduce(lambda x, _: x+[x[-1]+x[-2]], range(num-2), [0, 1])

if __name__ == "__main__":
    num = int(input('please enter a number : '))
    print(getFibonacciSeries(num))
