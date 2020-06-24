# 38. Write a Python program to remove a key from a dictionary.


def removeKeyFromDict(input_dict, key=None):
    if key is not None:
        input_dict.pop(key)
        return input_dict
    input_dict.popitem()
    return input_dict


if __name__ == "__main__":
    input_dict = {1: 10, 2: 20, 3: 30, 'b': 40}
    print(removeKeyFromDict(input_dict, 2))  # with key
    print(removeKeyFromDict(input_dict))  # without key
