# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def getReverseOfString(input_string):
    new_list = []
    for each in range(len(input_string)-1, -1, -1):
        new_list += input_string[each]
    return ('').join(new_list)


if __name__ == "__main__":
    input_string = input('enter string: ')
    print(getReverseOfString(input_string))
