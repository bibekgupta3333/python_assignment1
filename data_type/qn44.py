# 44. Write a Python program to slice a tuple.


def sliceTuple(input_tuple, to, end):
    return input_tuple[to: end]


if __name__ == "__main__":
    input_tuple = tuple(range(10))
    to = 1
    end = 5
    print(sliceTuple(input_tuple, to, end))
