# 30. Write a Python script to check whether a given key already exists in a
# dictionary.


def isKeyInDict(input_dict, input_key):
    return bool(input_dict.get(input_key))


if __name__ == "__main__":
    input_dict = {1: 10, 2: 20}
    input_key = 4
    print(isKeyInDict(input_dict, input_key))
