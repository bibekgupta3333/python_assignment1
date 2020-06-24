# 18. Write a Python program to get the largest number from a list.

def getlargestNumber(sequences):
    max_num = sequences[0]
    for each in sequences:
        if type(each) is int or type(each) is float:
            if(max_num < each):
                max_num = each

    return max_num


if __name__ == "__main__":
    list_item = [1, 3, 4, 5, 6, 7, 1237, '12', 'addgads', 100.5, 100.3]
    print(getlargestNumber(list_item))
