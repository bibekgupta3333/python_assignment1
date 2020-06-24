# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def getFirstLastSameCharCount(input_list):
    counter = 0
    for each in input_list:
        if len(str(each)) >= 2:
            if each[0] == each[-1]:
                counter += 1
    return counter


if __name__ == "__main__":
    input_list = ['abc', 'xyz', 'aba', '11', '1221']
    print(getFirstLastSameCharCount(input_list))
