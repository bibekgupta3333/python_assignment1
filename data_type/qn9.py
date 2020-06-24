# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.


def getFirstAndLastCharExchangeStr(input_str):
    input_str = input_str.split()
    input_str[0] = list(input_str[0])
    input_str[-1] = list(input_str[-1])
    input_str[0][0], input_str[-1][-1] = input_str[-1][-1], input_str[0][0]
    input_str[0] = ('').join(input_str[0])
    input_str[-1] = ('').join(input_str[-1])

    return (' ').join(input_str)


if __name__ == "__main__":
    in_string = input('please enter the words and give space: ')
    print(getFirstAndLastCharExchangeStr(in_string))
