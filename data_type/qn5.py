# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def getStringWithIng(input_str):
    # checks string len greater than three
    if len(input_str) >= 3:
        # checks string string ends with ing or not
        if 'ing' == input_str[-3:]:
            return input_str + 'ly'
        else:
            return input_str + 'ing'
    return input_str


if __name__ == "__main__":
    in_string = input('please enter the string: ')
    print(getStringWithIng(in_string))
