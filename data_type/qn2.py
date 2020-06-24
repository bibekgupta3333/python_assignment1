# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String


def getStartEndCharString(input_str):
    if len(input_str) >= 2:
        return input_str[0:2]+input_str[-2:]
    return 'Empty String'


if __name__ == "__main__":
    in_string = input('please enter the string to get start and end: ')
    print(getStartEndCharString(in_string))
