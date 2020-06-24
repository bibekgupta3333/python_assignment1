# 10. Write a Python program to remove the characters which have odd index
# values of a given string.


def getRemove(input_str):
    input_str = list(input_str)
    new_str = []
    for each in range(len(input_str)):
        if each % 2 != 0:
            new_str.append(input_str[each])
    input_str = new_str
    return ('').join(input_str)


if __name__ == "__main__":
    in_string = input('please enter the words: ')
    print(getRemove(in_string))
