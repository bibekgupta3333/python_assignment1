# 41. Write a Python program to convert a tuple to a string.


def convertTupleToString(input_tuple):
    return ('').join(str(each) for each in input_tuple)


if __name__ == "__main__":
    input_tuple = tuple(range(10))

    print(convertTupleToString(input_tuple))
