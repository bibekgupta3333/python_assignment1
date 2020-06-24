# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


def addStringAtBegginingOfItemsInList(input_list, input_string):
    counter = 0
    while counter in range(len(input_list)):
        input_list[counter] = str(input_string) + str(input_list[counter])
        counter += 1
    return input_list


if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    input_string = 'emp'
    print(addStringAtBegginingOfItemsInList(input_list, input_string))
