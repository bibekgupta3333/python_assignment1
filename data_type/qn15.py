# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_sting_middle(braces, strings):

    return f"{braces[0:2]}{strings}{braces[2:4]}"


if __name__ == "__main__":
    braces = input('please enter brace: ')
    strings = input('please enter the content to surrounded by strings: ')
    print(insert_sting_middle(braces, strings))
