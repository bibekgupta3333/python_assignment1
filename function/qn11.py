# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

add15 = lambda num: num + 15

multiplyTwoNumber = lambda num1, num2: print(num1 * num2)

if __name__ == "__main__":
    print(add15(1))
    multiplyTwoNumber(10, 10)
