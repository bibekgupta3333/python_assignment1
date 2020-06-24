# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def isPrimeNumber(num):
    counter = 0
    for each in range(1, num+1):
        if num % each == 0:
            counter += 1
    if counter == 2:
        return True
    return False


if __name__ == "__main__":
    num = int(input('Enter a Number to check prime: '))
    print(isPrimeNumber(num))
