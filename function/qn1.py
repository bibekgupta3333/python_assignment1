# 1. Write a Python function to find the Max of three numbers.


def getMaxOfThreeNumber(num1, num2, num3):
    li = [num1, num3, num2]
    return max(li)


if __name__ == "__main__":

    print(getMaxOfThreeNumber(1, 10, 123))
