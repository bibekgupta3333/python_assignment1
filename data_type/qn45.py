# 46. Write a Python program to find the index of an item of a tuple.


def getIndexOfTuple(input_tuple, item):
    return input_tuple.index(item)


if __name__ == "__main__":
    input_tuple = tuple(range(1, 10))
    item = 1
    print(getIndexOfTuple(input_tuple, item))
