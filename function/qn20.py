# 20. Write a Python program to find intersection of two given arrays using
# Lambda.


getIntersectionBetweenTwoArrays = lambda input_list1, input_list2: list(
    filter(lambda x: x in input_list1, input_list2))

if __name__ == "__main__":
    input_list1 = list(range(1, 9))
    input_list2 = list(range(5, 15))
    print(getIntersectionBetweenTwoArrays(input_list1, input_list2))
