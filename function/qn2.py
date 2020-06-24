# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def getSumOfAllNum(input_list):
    total = 0
    for each in input_list:
        total += each
    return total


if __name__ == "__main__":
    input_list = list(range(1, 11))
    print(getSumOfAllNum(input_list))
