# 28. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


def addKeyToDict(input_dict, key, value):
    input_dict[key] = value
    return input_dict


if __name__ == "__main__":
    input_dict = {0: 10, 1: 20}
    key = 2
    value = 30
    print(addKeyToDict(input_dict, key, value))
    key = 3
    value = 30
    print(addKeyToDict(input_dict, key, value))
