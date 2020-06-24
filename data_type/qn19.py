# 19. Write a Python program to get the smallest number from a list.

def getSmallestNumber(sequences):
    min_num = sequences[0]
    for each in sequences:
        if type(each) is int or type(each) is float:
            if(min_num > each):
                min_num = each

    return min_num


if __name__ == "__main__":
    list_item = [1, 3, 4, 5, 0.1, 6, 7, 1237, '12', 'addgads', 100.5, 100.3]
    print(getSmallestNumber(list_item))
