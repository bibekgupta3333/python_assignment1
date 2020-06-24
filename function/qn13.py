# 13. Write a Python program to sort a list of tuples using Lambda.

getSortedTuple = lambda input_tuple: sorted(input_tuple)


if __name__ == "__main__":
    input_tuple = list({'z': 1, 'b': 12, 'a': 123}.items())
    print(getSortedTuple(input_tuple))
