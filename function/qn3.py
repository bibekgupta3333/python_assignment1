# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def getMulOfAllNum(input_list):
    total = 1
    for each in input_list:
        total *= each
    return total


if __name__ == "__main__":
    input_list = list(range(1, 11))
    print(getMulOfAllNum((8, 2, 3, -1, 7)))
