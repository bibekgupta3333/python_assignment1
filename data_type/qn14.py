# 14. Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag, content):
    return f"<{tag}> {content} </{tag}>"


if __name__ == "__main__":
    tag = input('please enter tag: ')
    content = input('please enter the content to surrounded by tag: ')
    print(add_tags(tag, content))
