# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

def getLowerUpperCaseOfString(input_str):

    return f"Uppercase: {input_str.upper()} \nLowercase: {input_str.lower()} "


if __name__ == "__main__":
    in_string = input('please enter the words: ')
    print(getLowerUpperCaseOfString(in_string))
