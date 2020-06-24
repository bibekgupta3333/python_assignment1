# 40. Write a Python program to add an item in a tuple.

# tuples does not
def addItemToTuple(input_tuple, *item):
    input_tuple = input_tuple + (*item,)
    return input_tuple


if __name__ == "__main__":
    input_tuple = tuple(range(10))

    print(addItemToTuple(input_tuple, 10, 12))
