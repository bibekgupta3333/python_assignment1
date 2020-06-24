# 34. Write a Python script to merge two Python dictionaries.


def mergeTwoDict(input_dict1, input_dict2):
    input_dict1.update(input_dict2)
    return input_dict1


if __name__ == "__main__":
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}

    print(mergeTwoDict(dic1, dic2))
