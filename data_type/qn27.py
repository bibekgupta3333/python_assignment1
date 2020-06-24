# 27. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


def getListReplacedWithAnotherAtLastItem(input_list1, input_list2):
    input_list1.pop(-1)
    input_list1 += input_list2[:]
    return input_list1


if __name__ == "__main__":
    input_list1 = [1, 3, 5, 7, 9, 10]
    input_list2 = [2, 4, 6, 8]

    print(getListReplacedWithAnotherAtLastItem(input_list1, input_list2))
