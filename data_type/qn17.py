# 17. Write a Python program to multiplies all the items in a list.

def getItemMultipliedInList(num, sequences):
    return [each*num for each in sequences]


if __name__ == "__main__":
    list_item = [1, 3, 4, 5, 6, 7, 7, '12', 'addgads', 100.2]
    num = 6
    print(getItemMultipliedInList(num, list_item))
