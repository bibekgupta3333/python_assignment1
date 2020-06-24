# 6. Write a Python function to check whether a number is in a given range.

def isNumRange(start, end, num):
    if num in range(start, end+1):
        return True
    return False


if __name__ == "__main__":
    start = int(input('enter start: '))
    end = int(input('enter end: '))
    num = int(input('enter num: '))
    print(isNumRange(start, end, num))
