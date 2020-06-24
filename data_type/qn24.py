# 24. Write a Python program to clone or copy a list.


def getCopyList(input_list):
    if isinstance(input_list, list):
        return input_list[:]
    else:
        return "please give a list as argument"


if __name__ == "__main__":
    input_list = []
    print(getCopyList(input_list))
