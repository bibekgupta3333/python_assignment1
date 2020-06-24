# 23. Write a Python program to check a list is empty or not.


def isListEmpty(input_list):
    if isinstance(input_list, list):
        return not bool(input_list)
    else:
        return "please give a list as argument"


if __name__ == "__main__":
    input_list = []
    print(isListEmpty(input_list))
