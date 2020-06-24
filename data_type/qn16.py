# 16. Write a Python program to sum all the items in a list.

def getSumOfNumFromList(sequences):
    totalSum = 0
    for each in sequences:
        if type(each) is int or type(each) is float:
            totalSum += each

    return totalSum


if __name__ == "__main__":
    list_item = [1, 3, 4, 5, 6, 7, 7, '12', 'addgads', 100.2]
    print(getSumOfNumFromList(list_item))
