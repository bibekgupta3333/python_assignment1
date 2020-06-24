# 15. Write a Python program to filter a list of integers using Lambda.

getFilterInt = lambda input_list: list(filter(lambda e: e % 2 != 0, input_list))

if __name__ == "__main__":
    input_int = list(range(1, 101))
    print(getFilterInt(input_int))
