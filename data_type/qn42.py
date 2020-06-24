# 42. Write a Python program to convert a list to a tuple.


def convertListToTuple(input_tuple):
    return list(input_tuple)


if __name__ == "__main__":
    input_tuple = tuple(range(10))
    print(convertListToTuple(input_tuple))
