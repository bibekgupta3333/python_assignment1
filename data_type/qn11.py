# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

def getOccurenceWord(input_str):
    input_str = input_str.split()
    obj = {}
    for each in input_str:
        if obj.get(each) is None:
            obj[each] = 0
        obj[each] += 1
    return obj


if __name__ == "__main__":
    in_string = input('please enter the words: ')
    print(getOccurenceWord(in_string))
