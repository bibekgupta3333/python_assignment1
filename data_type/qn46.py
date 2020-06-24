# 46. Write a Python program to find the length of a tuple

def getLengthOfTuple(input_tuple):
    return len(input_tuple)


if __name__ == "__main__":
    input_tuple = tuple(range(1, 10))
    print(getLengthOfTuple(input_tuple))
