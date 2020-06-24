# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.

isGivenStringStartWithChar = lambda input_string, input_char: input_string.lower().startswith(input_char.lower())

if __name__ == "__main__":
    input_string = input('please enter a string: ')
    input_char = input('please enter a char to check starts with: ')
    print(isGivenStringStartWithChar(input_string, input_char))
