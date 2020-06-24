# 18. Write a Python program to check whether a given string is number or not
# using Lambda.
isGivenStringANumber = lambda input_string: input_string.isnumeric()

if __name__ == "__main__":
    input_string = input('please enter a string to check whether it is number or not: ')
    print(isGivenStringANumber(input_string))
