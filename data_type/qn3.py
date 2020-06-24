# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def getFirstCharOccuurenceWithDollar(input_str):
    str_list = list(input_str[1:])
    new_list = []
    new_list.append(input_str[0])
    for each in str_list:
        if input_str[0] == each:
            new_list += '$'
        else:
            new_list += each
    return ('').join(new_list)


if __name__ == "__main__":
    in_string = input('please enter the string: ')
    print(getFirstCharOccuurenceWithDollar(in_string))
