# 1
# Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
import string


def countString(input_str):
    obj = {}
    for each in input_str.lower():
        if each in string.ascii_lowercase:
            if obj.get(each) == None:
                obj[each] = 0
            obj[each] += 1
    return obj


if __name__ == "__main__":
    in_string = input('please enter the string to count: ')
    print(countString(in_string))
