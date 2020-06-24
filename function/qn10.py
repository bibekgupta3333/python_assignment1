# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def getEvenNumberFromList(input_list):
    return [each for each in input_list if each % 2 == 0]


if __name__ == "__main__":
    input_list = list(range(1, 10))
    print(getEvenNumberFromList(input_list))
