# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def countUpperLowerLetter(input_string):
    upper = 0
    lower = 0
    for each in input_string:
        if each.isupper() and ord(each) in range(ord('A'), ord('Z')+1):
            upper += 1
        if each.islower() and ord(each) in range(ord('a'), ord('z')+1):
            lower += 1
    return f'No. of Upper case characters :{upper}  \nNo. of Lower case Characters : {lower}'


if __name__ == "__main__":
    input_string = input('enter string: ')
    print(countUpperLowerLetter(input_string))
