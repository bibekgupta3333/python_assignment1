# 43. Write a Python program to remove an item from a tuple.


def removeKeyFromTuple(input_tuple):
    input_tuple = input_tuple[-len(input_tuple):-1]
    return input_tuple


if __name__ == "__main__":
    input_tuple = tuple(range(10))
    input_tuple = removeKeyFromTuple(input_tuple)
    print(removeKeyFromTuple(input_tuple))
