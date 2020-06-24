# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


def getGoodStringIfNotFollowPoor(input_str):
    word = input_str.lower().split()
    if 'not' in word:
        indexNot = word.index('not')
        counter = -1
        for each in word[indexNot:]:
            counter += 1
            if 'poor' in str(each):
                word[indexNot+counter] = word[indexNot +
                                              counter].replace('poor', 'good')

                return_str = (' ').join(word).replace(
                    (' ').join(word[indexNot:indexNot+counter]), '')
                return_str = (' ').join(return_str.split())
                return return_str
    return input_str


if __name__ == "__main__":
    in_string = input('please enter the string: ')
    print(getGoodStringIfNotFollowPoor(in_string))
