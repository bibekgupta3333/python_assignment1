# 22. Write a Python program to remove duplicates from a list.


def getUniqueList(input_list):
    return list(set(input_list))


if __name__ == "__main__":
    input_list = [1, 3, 3, 5, 43, 1, 2, 3, 4, 6, 6, 7, 4, 4, 7, 7, 3, 4]
    print(getUniqueList(input_list))
