# 35. Write a Python program to iterate over dictionaries using for loops.


def iterateDict(input_dict):
    for k, v in input_dict.items():
        print(f'{k}:{v}')


if __name__ == "__main__":
    input_dict = {1: 10, 2: 20}
    iterateDict(input_dict)
