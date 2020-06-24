# 36. Write a Python program to sum all the items in a dictionary.
import string


def getSumAllDictItem(input_dict):
    totalSum = 0
    for k, v in input_dict.items():
        if type(v) is int:
            totalSum += v
    return totalSum


if __name__ == "__main__":
    input_dict = dict(zip(list(string.ascii_lowercase), list(range(1, 27))))

    print(getSumAllDictItem(input_dict))
