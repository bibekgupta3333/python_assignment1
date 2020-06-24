# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def getUniqueList(input_list):
    return list(set(input_list))


if __name__ == "__main__":
    input_list = [1, 2, 3, 3, 3, 3, 4, 5]
    print(getUniqueList(input_list))
