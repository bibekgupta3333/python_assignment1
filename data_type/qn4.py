# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


def getSwapFirstTwoCharOfString(input_str1, input_str2):
    input_str1 = list(input_str1.split()[0])
    input_str2 = list(input_str2.split()[0])
    input_str1[0:2], input_str2[0:2] = input_str2[0:2], input_str1[0:2]

    return ('').join(input_str1) + ' ' + ('').join(input_str2)


if __name__ == "__main__":
    in_string1 = input('please enter the string1: ')
    in_string2 = input('please enter the string2: ')
    print(getSwapFirstTwoCharOfString(in_string1, in_string2))
