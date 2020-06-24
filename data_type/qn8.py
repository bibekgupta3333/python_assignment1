# 8. Write a Python program to remove the n th index character from a nonempty
# string.


def removeNthIndex(input_str, index_num):
    if input_str != '' and type(index_num) is int:
        input_str = list(input_str)
        input_str.pop(index_num)
        return ('').join(input_str)
    return 'string is empty or index_num is not int type'


if __name__ == "__main__":
    in_string = input('please enter the words and give space: ')
    index_num = int(input('Please enter the index you want to remove: '))
    print(removeNthIndex(in_string, index_num))
