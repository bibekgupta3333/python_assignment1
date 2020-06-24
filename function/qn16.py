# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.
getSquareAndCube = lambda input_list: [list(map(lambda e: e ** each, input_list)) for each in range(2, 4)]

if __name__ == "__main__":
    input_list = list(range(1, 11))
    print(getSquareAndCube(input_list))
